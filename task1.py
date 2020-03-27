from bs4 import BeautifulSoup
import requests,json,os,string,pprint


def scrape_top_list():
	if os.path.exists("movie.json"):
		with open("movie.json",'r') as file:
			new_file=json.load(file)
		return new_file
	else:
		print('else')	 
		url='https://www.imdb.com/india/top-rated-indian-movies/'
		request_data=requests.get(url)
		soup=BeautifulSoup(request_data.text,'html.parser')
		main_div=soup.find('div',class_='lister')
		tbody=soup.find('tbody',class_='lister-list')
		trs=tbody.find_all('tr')
		# return trs
		Movie_name=[]
		Movie_rank=[]
		year=[]
		rating=[]
		url_movie=[]

		for tr in trs:
			# postion=tr
			postion=tr.find('td',class_="titleColumn").get_text().strip()
			rank=''
			movie=''
			for i in postion:
				if '.' not in i:
					rank+=i
				else:
					break
			Movie_rank.append(int(rank))

			movie=tr.find('td',class_='titleColumn').a.get_text()
			Movie_name.append(movie)

			release_date=tr.find('td',class_='titleColumn').span.get_text()
			release_movie=release_date[1:(len(release_date)-1)]
			year.append(int(release_movie))

			movie_link=tr.find('td',class_='titleColumn').a['href']
			movie='https://www.imdb.com'+movie_link
			url_movie.append(movie)

			movie_rating=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
			rating.append(float(movie_rating))
		main_file=[]
		for i in range(len(Movie_rank)):
			movie_dict={}
			movie_dict['Name']=str(Movie_name[i])
			movie_dict['Position']=Movie_rank[i]
			movie_dict['year']=year[i]
			movie_dict['rating']=rating[i]
			movie_dict['url']=url_movie[i]
			main_file.append(movie_dict	)

		with open('movie.json','w+') as file:
			new_file=json.dump(main_file,file)
		return new_file

		


