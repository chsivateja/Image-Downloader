import requests
from bs4 import BeautifulSoup
number = 0
total_images = []
def download(number,url):    
	image_urls = []
	print "Received URL",url
	string = (requests.get(url)).content
	location = string.find("<img src=")
	while location > 0:
		temp_location = location+len("<img src= ")
		second_location= string[temp_location:].find("\"")
		print string[temp_location:second_location+temp_location]
		if string[temp_location:second_location+temp_location] not in image_urls and string[temp_location:second_location+temp_location] not in total_images:
			total_images.append(string[temp_location:second_location+temp_location])
			image_urls.append(string[temp_location:second_location+temp_location])
		string = string[second_location+temp_location:]
		location = string.find("<img src=")
	for i in range(len(image_urls)):
		print number
		obj = open(str(number),"w")
		obj.write((requests.get(image_urls[i])).content)
		number = number + 1
	return number+1 


URL = raw_input("Enter Sitemap URL")
url_dict = dict()
#download(0,"http://www.nextbigwhat.com/delhi-government-to-grant-radio-taxi-licence-to-ola-uber-297/")
def URL_seperator(URL,url_dict):
	print "Looking ..", URL
	url_dict[URL] = list()
	response = requests.get(URL)
	html = response.content
	index = html.find("<loc>")
	while index > 0:
		html = html[index+5:]
		destination_url =  html[0:html.find("</loc>")]
		index = html.find("<loc>")
		if destination_url[-3:] == "xml":
			url_dict[destination_url] = list()
		else:
			url_dict[URL].append(destination_url)

URL_seperator(URL,url_dict)
for value in url_dict:
	if len(url_dict[value]) == 0:
		 URL_seperator(value, url_dict)
print url_dict.values()
for image_url in url_dict.values():
	for image in image_url:
		number = download(number,str(image))
		print number
