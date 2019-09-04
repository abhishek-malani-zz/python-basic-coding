from bs4 import BeautifulSoup
import requests
import json

url = "https://klook.klktech.com/signin"
page_data = requests.get(url)
page_source = BeautifulSoup(page_data.text, 'html.parser')
data = page_source.find('script')
x = data.text.split(";")[3].strip().replace("var ","")
sliceobject=slice(15,None)
y = x[sliceobject]
z = json.loads(y)
arr=[]
each_city = {}
for i in range (len(z)):
	a = z[i]['countries']
	for j in range (len(a)):
		b = z[i]['countries'][j]['cities']
		for k in range (len(b)):
			# arr["range_name"] = z[i]['range_name']
			# arr["country_name"] = z[i]['countries'][j]['country_name']
			# arr["city_id"] = z[i]['countries'][j]['cities'][k]['city_id']
			# arr["city_name"] = z[i]['countries'][j]['cities'][k]['city_name']
			each_city = {"range_name":z[i]['range_name'], "country_name": z[i]['countries'][j]['country_name'], "city_id":z[i]['countries'][j]['cities'][k]['city_id'], "city_name":z[i]['countries'][j]['cities'][k]['city_name']}
			arr.append(each_city)
print(arr)
