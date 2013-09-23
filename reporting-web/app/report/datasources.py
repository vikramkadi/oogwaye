import json
from sqlalchemy import create_engine
datasources = []
db_engines = {}
def init_datasources(f):
    global datasources
    with open(f) as dsfile:
        datasources_store = json.load(dsfile)
        datasources = datasources_store['data_sources']

def init_db_engines():
    global db_engines
    for ds in datasources:
        if ds['vendor'] == 'mysql':
            db_engines[ds['id']] = create_engine('mysql+mysqlconnector://' + str(ds['user']) + ':' + str(ds['password']) + '@' + str(ds['host']) + '/' + str(ds['db_schema_name']))

def lookup_engine(db_id):
    return db_engines.get(db_id)
