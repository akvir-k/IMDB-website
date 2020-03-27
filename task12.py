from bs4 import BeautifulSoup
from task1 import scrape_top_list
import json, requests,os
def Scrape_movie_cast(url):

	# data=(scrape_top_list()[])
	request=requests.get(url)
	soup=BeautifulSoup(request.text,'html.parser')
	
	title_cast=soup.find('div',id='titleCast')
	url_cast=title_cast.find('div',class_='see-more').a['href'].strip()
	new_url=url+url_cast

	word=url[27:36]
	if os.path.exists('task12/'+word):
		with open('task12/'+word,'r') as file:
			new_file=json.load(file)
			return new_file
	else:

		request1=requests.get(new_url)
		new_soup=BeautifulSoup(request1.text,'html.parser')
		table=new_soup.find('table',class_='cast_list')
		td=table.find_all('td',class_="")
		cast_list=[]
		# print(td)
		for tds in td:
			cast_dict={}
			name=tds.a.get_text().strip()
			imdb_id=tds.a['href']
			actor_id=imdb_id[6:15]
			cast_dict['imdb_id']=actor_id
			cast_dict['Name']=name
			cast_list.append(cast_dict)
		with open('task12/'+word,'w+') as file:
			new_file=json.dump(cast_list,file)
			return cast_list
print(Scrape_movie_cast())