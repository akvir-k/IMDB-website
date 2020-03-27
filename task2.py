import string,pprint
from task1 import scrape_top_list

def group_by_year(scrape_top_list):
	year={}
	for i in scrape_top_list:
		
		value=i['year']
		list1=[]
		for j in scrape_top_list:
			if value == j['year']:
				list1.append(j)
		year[value]=list1

	return year

group_by_year(data)
