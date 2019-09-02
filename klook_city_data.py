from bs4 import BeautifulSoup
import requests
import json

url = "https://klook.klktech.com/signin"
page_data = requests.get(url)
page_source = BeautifulSoup(page_data.text, 'html.parser')
tour_data = page_source.find('script')
city_list_raw_data = tour_data.text.split(";")[3].strip().replace("var ","")
sliceobject=slice(15,None)
city_list = city_list_raw_data[sliceobject]
city_list_json = json.loads(city_list)
city_dict={}
city_array = []
for i in range (len(city_list_json)):
	countries = city_list_json[i]['countries']
	for j in range (len(countries)):
		cities = countries[j]['cities']
		for k in range (len(cities)):
			city_dict["range_name"] = city_list_json[i]['range_name']
			city_dict["country_name"] = countries[j]['country_name']
			city_dict["city_id"] = cities[k]['city_id']
			city_dict["city_name"] = cities[k]['city_name']
			city_array.append(city_dict)
print(city_array)