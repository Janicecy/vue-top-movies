from urllib import request
from lxml import etree
from bs4 import BeautifulSoup
# response = request.urlopen('https://www.imdb.com/chart/top/')
# html_tree = etree.HTML(response.read().decode('utf-8'))
import re
from models import IMDB_Movie
soup = BeautifulSoup(open('index.html'), 'lxml')


URL = 'https://www.imdb.com/chart/top/'
DOMAIN = 'https://www.imdb.com/'


def get_html(url):
    response = request.urlopen(url)
    # read and return html content
    return response.read().decode('utf-8')


# parse https://www.imdb.com/chart/top/
# soup = BeautifulSoup(get_html(URL), 'lxml')
lister_list = soup.select("tbody[class='lister-list'] > tr")


counter = 1
for item in lister_list:
    # if counter == 3:
    #     break
    posterColumn = item.findChild('td', {'class': 'posterColumn'})

    detail_path = posterColumn.a['href']
    poster_path = posterColumn.a.img['src']

    titleColumn = item.findChild('td', {'class': 'titleColumn'}),
    # for unknown reason, the titleColumn is a tuple
    title = titleColumn[0].a.get_text()

    imdbRating = item.find_next('td', {'class': 'imdbRating'}),
    rating = imdbRating[0].strong.get_text()

    # parse https://www.imdb.com/title/detail_path/
    detail_response = get_html(DOMAIN + detail_path)
    detail_soup = BeautifulSoup(detail_response, 'lxml')

    # get container of all info needed
    content = detail_soup.find(
        'div', class_=re.compile('^Hero__ContentContainer'))

    genre = content.find(attrs={'data-testid': 'genres'}).get_text()
    plot = content.find(attrs={'data-testid': 'plot-l'}).get_text()

    # get container of names
    principal_credit = content.find(
        'ul', class_=re.compile('^ipc-metadata-list'))

    directors = [li.get_text() for li in principal_credit.contents[0].ul]

    # get original names that might contain braces
    _writers = [li.get_text() for li in principal_credit.contents[1].ul]
    # trim everything between braces
    writers = list(map(lambda name: name.split("(")[0], _writers))
    stars = [li.get_text() for li in principal_credit.contents[2].ul]

    user_review_count = content.find('span', {'class': 'score'}).get_text()

    print(counter)
    counter = counter+1
    movie = IMDB_Movie(
        title=title,
        rating=rating,
        genre=genre,
        plot=plot,
        directors=directors,
        writers=writers,
        stars=stars,
        poster_path=poster_path,
        detail_path=detail_path,
        user_review_count=user_review_count
    )

    movie.save()