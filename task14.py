

from tast5 import get_movies_list_details
import json,os,pprint

def anaylase_co_factor(data):
	
	amd={}
	for i in data:
		for j in i:
			actor_id=j['imdb_id']
			if actor_id not in amd:
				amd[actor_id]={}
				amd[actor_id]['Name']=j['Name']
				amd[actor_id]['frequent']=[]
			flag=False
			for k in i:
				if k['imdb_id'] ==actor_id:
					flag=True
				elif flag:
					for check in amd[actor_id]['frequent']:
						if check['imdb_id']==k['imdb_id']:
							check['movies']+=1
							break
					else:
						if k['imdb_id'] not in amd[actor_id]['frequent']:
							k['movies']=1	
							amd[actor_id]['frequent'].append(k)
							break
	return amd				
pprint.pprint(anaylase_co_factor(get_movies_list_details()))