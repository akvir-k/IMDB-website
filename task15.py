
from tast5 import get_movies_list_details
import json,os,pprint

def analyse_actor(data):

	actor_analyse={}
	for i in data:
		for j in i:
			actor_id=j['imdb_id']
			if j['imdb_id'] not in actor_analyse:
				actor_analyse[actor_id]={}
				actor_analyse[actor_id]['Name']=j['Name']
				actor_analyse[actor_id]['No_of_movies']=0
			for k in i:
				if k['imdb_id']==actor_id:
					actor_analyse[actor_id]['No_of_movies']+=1
			
	return actor_analyse
pprint.pprint(analyse_actor(get_movies_list_details()))	
