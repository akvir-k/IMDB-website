
from tast5 import get_movies_list_details
from task1 import scrape_top_list

def Analyse_movies_directors(movie_list):
	
	Director_list={}

	for i in movie_list:
		for j in i['Director']:
			if j not in Director_list:
				Director_list[j]=1
			else:
				Director_list[j]+=1
	return Director_list


print(Analyse_movies_directors(get_movies_list_details(scrape_top_list()[0:5])))	
