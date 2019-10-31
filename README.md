# mortgageapplife1
install python
install flask
install flask_sqlalchemy
#################################################

﻿# database configurations on localhost [SQLALCHEMY_DATABASE_URI]
#Postgres:

postgresql://scott:tiger@localhost/mydatabase

#MySQL:

mysql://scott:tiger@localhost/mydatabase

#Oracle:

oracle://scott:tiger@127.0.0.1:1521/sidname

#SQLite (note that platform path conventions apply):

#Unix/Mac (note the four leading slashes)
sqlite:////absolute/path/to/foo.db
#Windows (note 3 leading forward slashes and backslash escapes)
sqlite:///C:\\absolute\\path\\to\\foo.db
#Windows (alternative using raw string)
r'sqlite:///C:\absolute\path\to\foo.db'

##################################################
#Create table with:
$ python
>>> from app import db
>>> db.create_all()
>>>exit()


﻿# how to run
with, $ python app.py
