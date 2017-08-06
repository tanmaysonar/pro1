#!/usr/bin/env python

import requests
import json

# main api url
url = 'https://api.github.com/users/'


# put your username/password here
#auth = ('myUsername', 'myPassword')

# request an authorization token from the server
#response = requests.get(url + '/user/authentication',
#                        auth=auth, verify=False).json()

# get the token from the response
#token = response['authToken']['token']

# to make an api call using this token, 
# add a token parameter to the request
#params = {
#    'token': token,
#   'start': '2014-01-15',
#   'end': '2014-02-01',
#   'geoJSON': 1,
#   'limit': 10
#}
name = raw_input("What is your name? ")

if name != "":
	response = requests.get(url + name).json()
else:
	print "Please enter a GITHub username."
# response contains the geoJSON object,
# pretty print it to the console
#print json.dumps(response, indent=4)
dic = {}
dic = response

for k,v in dic.iteritems():
	print str(k) + ':' + str(v)

if response['login'] != None:
	print "+++++++++++++++++++++++++++++++++++++++++"
	print "My master's name is "+response['login']
	if response['bio'] != None:
		print "++++++++++++"
		print "And his identity is: "+response['bio']
		print "+++++++++++++++++++++++++++++++++++++++++"
	else:
		print "He is too lazy to write a bio"
else:
	print "This is not my master!!!!"