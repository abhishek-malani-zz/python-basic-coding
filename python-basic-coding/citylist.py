from bs4 import BeautifulSoup
import requests
import csv
import json

init_url = "https://www.trazy.com"

api_url = "https://www.trazy.com/index.php/api/getActivityList2/"

headers = {
    'Cache-Control': "no-cache",
    'Host': "www.trazy.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "172",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

column_headers = ["country","city name","tour_title","tour_duration","tour_price","tour_reg_price","price_currency","discount","availability","rating","pageview_text"]

file_name = 'trazy_data_dump.csv'

def main():
	with open(file_name, 'a') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(column_headers)
	csvFile.close()
	page_data = requests.get(init_url)
	page_source = BeautifulSoup(page_data.text, 'html.parser')
	cities = page_source.select("#city_option_list .city_option_item > a");
	for city in cities:
		get_world_code(city.text, city.attrs['href'])


def get_city_data(city_name, world_code):
	response = requests.post(api_url, data=dict(item_per_page='12',world_code=world_code))
	json_data=json.loads(response.text)
	item_count = json_data["count"]
	response = requests.post(api_url, data=dict(item_per_page=item_count,world_code=world_code))
	json_data=json.loads(response.text)
	for i in range(len(json_data["items"])):
	    row=[json_data["items"][i]["country"],
	    city_name,
	    json_data["items"][i]["tour_title"],
	    json_data["items"][i]["tour_duration"],
	    json_data["items"][i]["tour_price"],
	    json_data["items"][i]["tour_reg_price"],
	    json_data["items"][i]["price_currency"],
	    json_data["items"][i]["discount"],
	    json_data["items"][i]["availability"],
	    json_data["items"][i]["rating"],
	    json_data["items"][i]["pageview_text"]]

	    print(row)

	    with open(file_name, 'a') as csvFile:
	        writer = csv.writer(csvFile)
	        writer.writerow(row)
	    csvFile.close()


def get_world_code(city_name, city_link):
	page_data = requests.get(init_url+city_link)
	page_source = BeautifulSoup(page_data.text, 'html.parser')
	tags = page_source.select("#world_code")
	for tag in tags:
		world_code = tag.attrs['value']
		print(city_name + ": " + tag.attrs['value'])
		get_city_data(city_name, world_code)


main()
