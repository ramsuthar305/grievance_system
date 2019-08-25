# -*- coding: utf-8 -*-
import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://root:22oct1997@165.22.100.196:27017/nibodh')

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20
PAGINATION_LIMIT = 200
PAGINATION_DEFAULT = 200
#DEBUG = True

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.

MONGO_QUERY_BLACKLIST = ['$where']

grievance = {

'item_title': 'grievance',


        'grievance_id': {
            'type': 'number',
            'required': True,
            'unique': True,

        },
        'user_id': {
            'type': 'string',
            'required':True,
        },
        'image_link': {
            'type': 'string',
        },
        'grievance_type': {
            'type': 'string',
            'required':True,
        },
        'area': {
            'type': 'string',
            'required':True,
        },
        'latitude': {
            'type': 'string',
        },
        'longitude': {
            'type': 'string',
        },
        'assigned_authority': {
            'type': 'string',
        },
        'assigned_date': {
            'type': 'string',
        },
        'status': {
            'type': 'string',
        },
        'timestamp': {
            'type': 'string',
        },

}

grievance_users = {

'item_title': 'grievance_users',


        'user_id': {
            'type': 'number',
            'required': True,
            'unique': True,
        },
        'goverment_id':{
            'type':'string',
        },
        'user_name':{
            'type':'string',
        },
        'user_email':{
            'type':'string',
        },
        'user_password':{
            'type':'string',
        },
        'user_otp':{
            'type':'string',
        },
        'user_points':{
            'type':'string',
        },
}


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'grievance': grievance,
    'grievance_users':grievance_users

}
