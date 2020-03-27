
from task8 import find_position
import os ,json,requests,time,pprint
from task1 import scrape_top_list
from task4 import scrape_movies_details

def analyse_language_and_directors():

	dirctors_details={}
	
	for i in range(250):
		file=find_position(scrape_top_list()[i])
		file_dict=json.loads(file)
		
		for j in file_dict['Director']:
			Language={}
			for k in range(250):
				data=json.loads(find_position(scrape_top_list()[k]))
				if j in data['Director']:

					for lang in data['Language']:
						if lang not in Language:
							Language[lang]=1
						else:
							Language[lang]+=1
			dirctors_details[j]=Language
			print(dirctors_details)
	# return dirctors_details


pprint.pprint(analyse_language_and_directors())