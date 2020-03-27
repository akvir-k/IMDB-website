
import os ,json,requests
from task1 import scrape_top_list
from task4 import scrape_movies_details
def find_position(data):
	url=data['url']
	# print(data)
	word=''
	for i in url[27::]:
		if'/' not in i:
			word+=in
		else:
			word+='.json'
			break
	# print('task9/'+word)
	# return word
	if os.path.exists('task9/'+word):
		with open('task9/'+word,'r') as file:
			new_file=json.load(file)
		return new_file
	else:
		request=json.dumps(scrape_movies_details(url))	
		with open('task9/'+word,'w+') as file:
			new_file=json.dump(request,file)
			
		with open('task9/'+word,'r') as file:
			new_file=json.load(file)
			return new_file

# print(find_position(scrape_top_list()[14]))
		




