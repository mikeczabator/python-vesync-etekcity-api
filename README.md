# python-vesync-etekcity-api
API to VeSync Etekcity smart plugs

from vesync.api import VesyncApi
api = VeSync("username", "password")

devices = api.get_devices()

api.turn_on(device_id)

api.get_details(device_id)
api.get_energy(device_id) # building out different time windows soon

api.turn_off(device_id)

# print all device info:
devices = api.get_devices()
for i in devices:
    for k1 in i.keys():
        print(i[k1]) if k1 == 'deviceName' else print("\t"+k1+': '+i[k1])
        if k1 == 'deviceStatus' and i[k1] == 'on':
            details = api.get_details(i['cid'])
            for k2 in details.keys():
                if k2 == 'power' or k2 == 'voltage':
                    print("\t\t"+ k2+': '+ str(api.convert_hex(details[k2])))
                else:
                    print("\t\t"+ k2+': '+ str(details[k2]))
