#coding=utf8
import pymongo;
import re;
import sys;
'''
Created on 2013-11-7

@author: guoxiong.yuan
'''
def mongo_find(col, query, projection=None, sort=None, limit=2147483647, batch_size=100):
	cursor = col.find(spec=query, fields=projection, sort=sort, limit=limit   );
	if batch_size>0:
		cursor.batch_size(batch_size);
	return cursor;

def mongo_find_one(col, query, projection=None, sort=None):
	return col.find_one(spec_or_id=query, fields=projection, sort=sort);

def mongo_save(col, obj):
	col.save(obj);   
    
def mongo_update(col, query,document,  multi=False):
	if "_id" in query:
		col.update({"_id":query["_id"]}, document, multi=multi);
	else:
		col.update(query,document,  multi=multi)
    
    
def mongo_remove(col, doc):
	if "_id" in doc:
		col.remove({"_id":doc["_id"]});
	else:
		col.remove(doc);
		
		
def translate_filename(filename):
	filename = re.sub(r'/|\\|\"|\<|>|\?|:', "-", filename);
	filename = re.sub(r'\s', "", filename);
	filename = filename.replace('*',  u'＊');
	return filename;
	
	
	
    
