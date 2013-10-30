#        coding: utf-8

from bs4 import BeautifulSoup as bs
import urllib
import re


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


if __name__ == '__main__':
	softwares = parseTextFile('softwares.txt')
	print len(softwares), 'softwares found'
	for software in softwares:
		software.getLatestVersion()
		print software.name, '>', software.latestVersion