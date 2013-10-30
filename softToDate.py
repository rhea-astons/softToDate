#        coding: utf-8

from bs4 import BeautifulSoup as bs
import urllib
import re
import argparse as ap
import pyodbc
import ConfigParser as cp

class Software:
	def __init__(self, name, version):
		self.name = name
		self.version = version

	def getLatestVersion(self):
		params = urllib.urlencode({'q': self.name})
		f = urllib.urlopen("http://www.filehippo.com/search?%s" % params)
		html = f.read()
		parsed_html = bs(html)
		results = parsed_html.find('div', attrs={'class':'searchmiddle'})

		if results.find('table'):
			first_result = results.find('table').find('h2').find('a').contents[0].strip()
			self.latestVersion = re.search('\d+\.\d*(\.\d+)*', first_result).group(0).strip()
		else:
			self.latestVersion = 'not found'

def parseTextFile(file):
	softs = []
	for appName in open(file, 'r'):
		softs.append(Software(appName.rstrip('\r\n'), '1.0'))
	return softs

def main():
	# Arguments parsing
	parser = ap.ArgumentParser(description='Software version checkker')
	parser.add_argument('-f', '--file',
		metavar='SOFTWARES_FILE',
		default='softwares.txt',
		help='path to text file containing software information')
	parser.add_argument('--sql',
		metavar='DB_CONFIG_FILE',
		help='path to database config file')
	args = parser.parse_args()
	softwareFile = args.file

	# Database mode
	if args.sql != None:
		try:
			config = cp.RawConfigParser(allow_no_value=True)
			config.read('.mr.developer.cfg')
			server = config.get('SQL', 'server')
			database = config.get('SQL', 'database')
			user = config.get('SQL', 'user')
			pwd = config.get('SQL', 'pwd')
			query = config.get('SQL', 'query')
		except Exception as detail:
			print "ERROR: configuration file format (", detail, ")"
			exit(1)

		try:
			conStr = 'DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (server, database, user, pwd)
			con = pyodbc.connect(conStr)
		except Exception as detail:
			print "ERROR: can't connect to database (", detail, ")"
			exit(1)

		try:
			cursor = con.cursor()
			cursor.execute(query)
			rows = cursor.fetchall()
		except Exception as detail:
			print "ERROR: query failed (", detail, ")"
			exit(1)

		softwares = []
		for row in rows:
			softwares.append(Software(row.nom, '1.0'))

		print len(softwares), 'softwares found in database'

	# Filetext mode
	else:
		softwares = parseTextFile(softwareFile)
		print len(softwares), 'softwares found in file'

	# WORK
	for software in softwares:
		software.getLatestVersion()
		print software.name, '>', software.latestVersion


if __name__ == '__main__':
	app = main()