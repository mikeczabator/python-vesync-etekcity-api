import requests
import hashlib
import json

requests.packages.urllib3.disable_warnings()

BASE_URL = "https://smartapi.vesync.com"

class VesyncApi:
    def __init__(self, username, password):
        payload = json.dumps({"account":username,"devToken":"","password":hashlib.md5(password.encode('utf-8')).hexdigest()})
        account = requests.post(BASE_URL + "/vold/user/login", verify=False, data=payload).json()
      
        if "error" in account:
            raise RuntimeError("Invalid username or password")
        else:
            self._account = account
        self._devices = []

    def get_devices(self):
        self._devices = requests.get(BASE_URL + '/vold/user/devices', verify=False, headers=self.get_headers()).json()
        return self._devices

    def turn_on(self,id):
        requests.put(BASE_URL + '/v1/wifi-switch-1.3/' + id + '/status/on', verify=False, data={}, headers=self.get_headers())

    def turn_off(self, id):
        requests.put(BASE_URL + '/v1/wifi-switch-1.3/' + id + '/status/off', verify=False, data={}, headers=self.get_headers())

    def get_headers(self):
        return {'tk':self._account["tk"],'accountid':self._account["accountID"]}

    def get_details(self, id):
        self._details = requests.get(BASE_URL + '/v1/device/' + id + '/detail', headers=self.get_headers()).json()
        return self._details
    
    def get_energy(self, id):
        self._energy = requests.get(BASE_URL + '/v1/device/' + id + '/energy/month', headers=self.get_headers()).json()
        return self._energy
    
    def convert_hex(self, hex_string):
        self._converted_value = (int(hex_string.split(':')[0],16)+int(hex_string.split(':')[0],16))/8192
        return self._converted_value
        