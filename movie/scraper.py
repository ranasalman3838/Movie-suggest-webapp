import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


HEADERS ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

genres = [   
    
    "Comedy",
   
    "Horror",
   
    "Romance",
   
    "Thriller"
]

url_dict = {}

for genre in genres:
    url = "https://www.imdb.com/search/title/?genres={}&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=N97GEQS6R7J9EV7V770D&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16"
    formated_url = url.format(genre)
    url_dict[genre] = formated_url
    
print(url_dict)
def get_movies(url, interval, file_name):
    
    resp = requests.get(url, headers=HEADERS)
    content = BeautifulSoup(resp.content, 'lxml')

    movie_list = []

    for movie in content.select('.lister-item-content'):
        time.sleep(interval)
        try:
            data = {
                "title":movie.select('.lister-item-header')[0].get_text().strip(),
                "year":movie.select('.lister-item-year')[0].get_text().strip(),
                "certificate":movie.select('.certificate')[0].get_text().strip(),
                "time":movie.select('.runtime')[0].get_text().strip(),
                "genre":movie.select('.genre')[0].get_text().strip(),
                "rating":movie.select('.ratings-imdb-rating')[0].get_text().strip(),
                "metascore":movie.select('.ratings-metascore')[0].get_text().strip(),
                "simple_desc":movie.select('.text-muted')[2].get_text().strip(),
                "votes":movie.select('.sort-num_votes-visible')[0].get_text().strip()
            
                
            }
        except IndexError:
            continue
    
        movie_list.append(data)
         
        
    dataframe = pd.DataFrame(movie_list)
    dataframe.to_csv(file_name)

url = "https://www.imdb.com/search/title/?genres=Adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=N97GEQS6R7J9EV7V770D&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16"

# Calling the function
for genre, url in url_dict.items():
    get_movies(url, 1, genre+'.csv')
    print("Saved:", genre+'.csv')