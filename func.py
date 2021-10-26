import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import os.path, time

site_check 	= []
site_names 	= []
site_links 	= []
site_arg1 	= []
site_arg2 	= []
prod_price1 = []
prod_price 	= []
prod_name1 	= []
prod_name 	= []
product 	= {}

'''This function will run as it is. It will read the Settings.csv file and take properties for sites for other funtions to work. '''
def get_settings():
	file_name = "Settings.csv"
	file = pd.read_csv(file_name)
	settings_param = file.iloc[:,:].values

	for i in settings_param:
		site_check.append(i[0])
		site_names.append(i[1])
		site_links.append(i[2])
		site_arg1.append(i[3])
		site_arg2.append(i[4])
		prod_price1.append(i[5])
		prod_price.append(i[6])
		prod_name1.append(i[7])
		prod_name.append(i[8])

'''This function will run also as it is. It will take user input and generate link to searc for product, also call on function which will request.'''
def gen_link():

	user_input = input("Enter product name: ") #   "samsung galaxy s20"   #
	url_prefix = '+'.join(user_input.split())

	with open('OUT.txt', 'a') as file:
		file.write(f'\n{time.ctime(os.path.getctime("OUT.txt"))}\n')

	for i in range(0,len(site_names)):
		if(site_check[i] == 1):
			#print(site_check[i])
			site_url = site_names[i] + site_links[i] + url_prefix

			#print(site_names[i])
			get_data(site_url,site_arg1[i],site_arg2[i],prod_price1[i],prod_price[i],prod_name1[i],prod_name[i],i)

'''Will take from global variables argument and send request. Also create a product dict in which will be found name, price and site'''
def get_data(site:str, arg1:str, arg2:str, price_arg:str, price_:str, product_arg:str, product_:str, index:int):
	global product
	get_site = req.get(site).text
	site_as_text = bs(get_site, 'html.parser')
	product_html = site_as_text.find(arg1,{"class":arg2})

	try:
		price = product_html.find(price_arg, {"class":price_})
		if(price.sup):
			price.sup.decompose()
		price = price.get_text().strip()
	except:
		price = None

	try:
		name = product_html.find(product_arg,{"class":product_}).get_text().strip()
	except:
		name = None

	product = {"name":name, "price":price, "site":site_names[index]}
	# print(product)
	generate_file()

def generate_file():
	with open('OUT.txt', 'a') as file:
		file.write("\nname: " + product["name"])
		file.write("\nprice: " + product["price"])
		file.write("\nfound on: " + product["site"]+"\n")