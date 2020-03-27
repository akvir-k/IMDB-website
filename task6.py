
from tast5 import get_movies_list_details
from task1 import scrape_top_list

def Analyse_movies_language(movie_list):
	Language_list={}

	for i in movie_list:
		for j in i['Language']:
			if j not in Language_list:
				Language_list[j]=1
			else:
				Language_list[j]+=1
	return Language_list


print(Analyse_movies_language(get_movies_list_details(scrape_top_list()[0:10])))	
