#!/usr/bin/python

from configparse import configParser
import psycopg2
import json

def reply(message):
	print json.dumps(message)
	exit()
#enddef

def readConfig(file_name='db.ini', section='postgresql'):
    	parser = ConfigParser()
    	parser.read(filei_name)
 
    	db = {}
    	if parser.has_section(section):
        	params = parser.items(section)
        	for param in params:
            		db[param[0]] = param[1]
    	else:
		error = 'Section {0} not found in the {1} file'.format(section, filename)
		reply({"error": error})
    	return db
#enddef

if __name__ == '__main__':
	
	if len(sys.argv) == 1: 
		reply({"error":"Require restaurant id"})
	#endif 

	db = readConfig()
	conn = None
   	try:
        	params = config()
        	conn = psycopg2.connect(host="localhost",database=db["dbname"], user=db["username"], password=db["pass"])
	        cur = conn.cursor()
	except (Exception, psycopg2.DatabaseError) as error:
		reply({"error":"Couldn't connect to database"})
		
	query = "select item_name, price from restaurant_items where id="+sys.argv[1]
	cur.execute(query)
	results = cur.fetchall()

	items = {}
	items["status_code"] = 200
	items["content"] = []
	for item in results:
		items["content"].append({"item_name": item["item_name"], "price": item["price"]})
	
	## Convert array to json
	print json.dump(items)
#endif			
