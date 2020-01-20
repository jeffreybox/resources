import json
import requests

"""API"""
api_username = 'username'
api_password = 'password'
#endpoint = 'scorecord'

authUrl ='https://cvcoxreportsapi.creativevirtual15.com/vstats/config/cox'
getUrl ='https://cvcoxreportsapi.creativevirtual15.com/vstats/config/cox' # + endpoint + "/"+ another_endpoint
payload = {'username': api_username, 'password': api_password}

"""Hide warnings for the 'InsecureRequestWarning' for each API hit"""
requests.packages.urllib3.disable_warnings()

"""API CALL -> JSON"""
s = requests.session()
s.post(authUrl, verify=False, data=payload)
r = s.get(getUrl)
my_json = r.json()

"""PRETTY PRINT THE JSON"""
parsed = json.loads(my_json)
print(json.dumps(parsed, indent=4, sort_keys=True))

"""EXAMPLE GETTING INTO NESTS"""
print(parsed['excelReports']['Semantic Trigger']['subType'])