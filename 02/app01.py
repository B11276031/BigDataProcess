#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
import json,urllib.request

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization=CWA-CED0FE4D-EB90-4855-80EE-362A9F64A637&locationId=F-D0047-009'

data = urllib.request.urlopen(url).read()
output = json.loads(data)
location=output['records']['locations'][0]['location']


for i in location:
    print(f'{i}')


for i in location:
  name = i['locationName']
  lat=i['lat']
  print(name,lat)
