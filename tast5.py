
from task4 import scrape_movies_details
from task1 import scrape_top_list
import pprint,os,json,time,pprint
def get_movies_list_details():
	get_list=[]
	if os.path.exists('movies_list.json'):
		with open('movies_list.json','r') as file:
			new_file=json.load(file)
		return new_file
	else:		
		for i in range(5):
			data=scrape_movies_details(scrape_top_list()[i])
			get_list.append(data['cast'])

		with open('movies_list.json','w+') as file:
			dump_data=json.dump(get_list,file)
		return get_list

# for i in get_movies_list_details():	
# pprint.pprint(get_movies_list_details())


# pprint.pprint(movies_list)


	
