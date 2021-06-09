import mariadb

config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'asistencialg4p2'
}

DB = mariadb.connect(**config)
DB.autocommit = True