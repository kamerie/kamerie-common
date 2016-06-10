from pymongo import MongoClient
from pymongo.results import InsertOneResult, InsertManyResult
from bson.objectid import ObjectId
import re

FIELD_ID = '_id'
FIELD_SEASON = 'season'
FIELD_EPISODE = 'episode'
FIELD_NAME = 'name'
FIELD_SANITIZED_NAME = 'sanitized_name'
FIELD_SERIES_ID = 'series_id'

db = MongoClient('mongodb://localhost:27017').kamerie


def attrs_to_db_set(attributes):
    setter = {
        '$set': {},
        '$currentDate': {'lastModified': True}
    }

    for key, value in attributes.iteritems():
        setter['$set'][key] = value

    return setter


def query_by_id(item):
    if hasattr(item, 'db_info') and item.db_info is not None:
        item = item.db_info

    if str(item) == item:
        return {'_id': ObjectId(item)}

    if isinstance(item, InsertOneResult):
        return {'_id': item.inserted_id}

    if '_id' in item:
        if isinstance(item['_id'], ObjectId):
            return {'_id': item['_id']}
        elif '$oid' in item['_id']:
            return {'_id': ObjectId(item['_id']['$oid'])}
        else:
            return {'_id': ObjectId(item['_id'])}


def sanitize_name(name):
    return re.sub(r'\W', '', name).lower()
