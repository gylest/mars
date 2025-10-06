import re
import requests
from bs4 import BeautifulSoup

#
# Download web page for imdb chart and scrape the movie information
#


def readimdbtop250():
    url = 'https://www.imdb.com/chart/top'
    print(f'Start processing for {url}')

    # Get HTML and parse
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Create items that map to HTML elements
    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
               for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value')
             for b in soup.select('td.ratingColumn strong')]

    # Create a empty list for storing movie information
    mlist = []

    # Iterate over movies to extract each movie's details
    for i, value in enumerate(movies):
        # Separating  movie into: 'place','title', 'year'
        movie_string = value.get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(i))+1:-7]
        year = re.search(r'\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(i))-(len(movie))]
        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[i],
                "rating": ratings[i],
                "vote": votes[i],
                "link": links[i]}
        mlist.append(data)

    # printing movie details with its rating.
    for movie in mlist:
        print(f'{movie["place"]} - {movie["movie_title"]} ({movie["year"]}) - Starring: {movie["star_cast"]}, Rating = {float(movie["rating"]):.1f}')

    print(f'Processing complete for {url}')


#
# If this run as startup file, the if statement is true and the main() is called.
#
if __name__ == '__main__':
    readimdbtop250()
