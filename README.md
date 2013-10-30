# softToDate
#### Requirements
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

#### Usage
softToDate.py [-h] [-f SOFTWARES_FILE] [--sql DB_CONFIG_FILE]

Software version checkker

optional arguments:
  -h, --help            show this help message and exit
  -f SOFTWARES_FILE, --file SOFTWARES_FILE
                        path to text file containing software information
  --sql DB_CONFIG_FILE  path to database config file

##### Database configuration file example
[SQL]
server = localhost
database = mydb
user = username
pwd = password
query = SELECT names FROM softwares