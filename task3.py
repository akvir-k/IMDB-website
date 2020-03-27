
import pprint,string
from task1 import scrape_top_list

def group_by_decades(scrape_top_list):
	group={}
	for i in scrape_top_list:
		value=i['year']

		value=value//10
		new_value=int(str(value)+'0')
		if new_value not in group:
			group[new_value]=[]
			group[new_value].append(i)
		else:
			group[new_value].append(i)
	return group



pprint.pprint(group_by_decades(scrape_top_list()))