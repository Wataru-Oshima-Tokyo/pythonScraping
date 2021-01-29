from urllib.parse import urljoin
from bs4 import BeautifulSoup

# reading html file and get the bs object
with open('dp.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

# by the select(), gettng the a list whcih is applied to the select and processing to each a element
for a in soup.select('#listBook > li > a[itemprop="url"]'):
    # get the url of the book from the href element
    url = urljoin('https://gihyo.jp/dp', a.get('href'))

    # the title of the book is obtained from the p elemtn whic has itemprp="name" attribute
    p = a.select('p[itemprop="name"]')[0]
    title = p.text #use text not string because it has the wbr element

    #output the url and tiel fo the book
    print(url, title)
