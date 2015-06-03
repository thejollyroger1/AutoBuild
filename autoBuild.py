#/usr/bin/python
#This script is a WIP and the purpose is to spin up a server from the API on any account and inject my server setup script.

import json
import requests

def rackspace_auth(user_name,api_key):
    url = "https://identity.api.rackspacecloud.com/v2.0/tokens"
    data = json.dumps({"auth": {"RAX-KSKEY:apiKeyCredentials": {"username": user_name, "apiKey": api_key}}})
    headers = {'Content-type': 'application/json'}
    request = requests.post(rackspace_auth, data=auth_data, headers=auth_headers)
    token = auth_request.json()['access']['token']['id']
    return token

def create_server(name,ram,flavor,region,account_id):
    token = rackspace_auth(user_name,api_key)
    url = "https://" + region + ".servers.api.rackspacecloud.com/v2/" + account_id
    headers = ({"Accept: application/json"}, {"Content-Type: application/json"}, {"User-Agent: python-novaclient"}, {"X-Auth-Token": token})
    data = json.dumps({"server": {"name": "SeanTest1", "imageRef": image_id, "flavorRef": "performance1-1", "max_count": 1, "min_count": 1, "networks": [{"uuid": "00000000-0000-0000-0000-000000000000"}, {"uuid": "11111111-1111-1111-1111-111111111111"}]}})
    
