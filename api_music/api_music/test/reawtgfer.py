import json

import xmltodict

with open('/home/user/Moduli/api_music/data/api_music.xml', 'rb') as file:
    result = xmltodict.parse(file)
    print(json.dumps(result))
    print(result)

