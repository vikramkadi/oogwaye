from app.services import mongo
import uuid

def upsert_report(data):
	try:
		print mongo.mongo_client
		print mongo.mongo_db
		report_id = data.get('report_id')
		print ('Report-id is' + str(report_id))
		if exists(report_id):
			old_report = query(report_id)
			data['_id'] = old_report['_id']
			report_coll().save(data)
		else:
			report_id = gen_uuid()
			data['report_id'] = report_id
			report_coll().save(data)
		return (True, report_id)
	except Exception, e:
		print e
		return (False, e)
	
def exists(report_id):
	if report_id and query(report_id):
		return True
	else:
		return False

def gen_uuid():
	return str(uuid.uuid4())
	
def query(report_id):
	return report_coll().find_one({"report_id":report_id})

def report_coll():
	if 'report' in mongo.mongo_db.collection_names():
		return mongo.mongo_db['report']
	else:
		mongo.mongo_db.create_collection('report')	
		return mongo.mongo_db['report']