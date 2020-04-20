from pymongo import MongoClient

def connectionDB(host, port, database):
    try:
        client = MongoClient(host, port)
        db = client.get_database(database)
        return db
    except :
        raise

_host_db_cryptocoins ='db_cryptocoins'
_port_db_cryptocoins = 27017
_cryptocoins = 'cryptocoins'

db_cryptocoins = connectionDB(_host_db_cryptocoins, _port_db_cryptocoins, _cryptocoins)
