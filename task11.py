from task4 import scrape_movies_details
from task1 import scrape_top_list
from task8 import find_position
import requests, json, pprint

def analyse_movies_genres():
	
	Genres_dict={}
	for i in range(250):
		data=find_position(scrape_top_list()[i])
		data_dict=json.loads(data)

		for j in data_dict['Genres']:
			if j not in Genres_dict:
				Genres_dict[j]=1
			else:
				Genres_dict[j]+=1
	return Genres_dict




print(analyse_movies_genres())