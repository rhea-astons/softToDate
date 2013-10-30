# softToDate
#### Requirements
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

#### Usage
softToDate.py [-h] [-f SOFTWARES_FILE] [--sql DB_CONFIG_FILE]

	-h, --help            			show this help message and exit

	-f, --file	SOFTWARES_FILE 		path to text file containing software information

	--sql 		DB_CONFIG_FILE		path to database config file

##### Database configuration file example
	[SQL]
	server = localhost
	database = mydb
	user = username
	pwd = password
	query = SELECT soft_name as name, soft_vers as version FROM software_table

##### Software file example
one software per line, name and version comma separated

	Notepad++,6.5
	Firefox,26.0
	PDF Creator,5.1
	CD Burner XP Pro,4.5
	PDF Split & Merge,1.7
	Mathtype,6.9