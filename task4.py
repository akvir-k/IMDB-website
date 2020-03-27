
import requests, pprint,json, string, os
from task1 import scrape_top_list
from bs4 import BeautifulSoup
from task12 import Scrape_movie_cast 
from pprint import pprint

def scrape_movies_details(url_movie):
	print(url_movie)

	if os.path.exists(url_movie['Name']+'.json') and False:
		with open(url_movie['Name']+'.json') as file:
			new_file=json.load(file)
		return new_file
	else:	
		url=url_movie['url']
		request=requests.get(url)
		soup=BeautifulSoup(request.text,'html.parser')

		data=[]
		plot_summary=soup.find('div',class_="plot_summary")
		summary=plot_summary.find('div',class_='summary_text').get_text().strip()
		Director=plot_summary.find('div',class_='credit_summary_item')

		des=Director.find_all('a')
		dir_list=[]
		for i in des:
			dir_list.append(i.get_text())

		find_country=soup.find('div',id='titleDetails')
		divs=find_country.find_all('div')

		for div in divs:
			if 'Country:' in div.get_text():
				data_country=div.a.get_text()
			if 'Language:' in div.get_text():
				lang_find=div.find_all('a')
				Language=[]
				for i in lang_find:
					Language.append(i.get_text())

		class_poster=soup.find('div',class_='poster')
		poster_url=class_poster.find('a').img['src']

		get_time=soup.find('div',class_='title_wrapper')
		time=get_time.find('time').get_text().strip()
		new_time=0
		word=''
		for i in range(len(time)):
			if time[i] in string.digits:
				word+=time[i]
			if time[i]=='h':
				new_time+=int(word)*60
				word=''
			elif time[i]=='m':
				new_time+=int(word)
				new_time=str(new_time)+' min'

		find_genre=soup.find('div',id='titleStoryLine')
		sub_genre=find_genre.find_all('div',class_='see-more inline canwrap')
		Genres=[]
		for i in sub_genre:
			if 'Genres' in i.h4.get_text():
				gen_data=i.find_all('a')
				for j in gen_data:
					Genres.append(j.get_text().strip())

		Movie_data=soup.find('div',class_='title_wrapper').h1.get_text().strip()
		Movie=''
		# print(Movie_data)
		for i in Movie_data:
			if '(' not in i:
				Movie+=i
			else:
				break
		# print(Movie)
		final_data={'Movie':'','Director':'','Country':'','Language':'','Poster':'','Runtime':'' ,'Genres':''}
		final_data['Movie']=Movie.strip()
		
		final_data['Director']=dir_list
		final_data['Country']=data_country
		final_data['Language']=Language
		final_data['Poster']=poster_url
		final_data['Runtime']=new_time
		final_data['Genres']=Genres

		# Add task 13 in task 4
		final_data['cast']=Scrape_movie_cast(url)
		# print(final_data)
		with open(url_movie['Name']+'.json', 'w+') as file:
			file_new=json.dump(final_data,file)

			return final_data

pprint(scrape_movies_details(scrape_top_list()[0]))
# scrape_movies_details(value)
