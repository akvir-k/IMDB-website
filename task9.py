
from task8 import find_position
import os ,json,requests,time,pprint
from task1 import scrape_top_list
from task4 import scrape_movies_details


for i in range(250):
	pprint.pprint(find_position(scrape_top_list()[i]))
	time.sleep(5)





