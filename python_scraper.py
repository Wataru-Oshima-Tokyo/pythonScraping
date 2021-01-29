import csv
from typing import List  # imported for the hint format

import requests
import lxml.html

def main():
    """
    the main function calling fetch(), scrape(),save()
    """

    url = 'https://gihyo.jp/dp'
    html = fetch(url)
    books = scrape(html, url)
    save('books.csv', books)

def fetch(url: str) -> str:
    """
    getting web page given by the URL in the url
    getting the encoding of the web page by the content-type header
    return: HTML , str format
    """
    r = requests.get(url)
    return r.text

def scrape(html: str, base_url: str) -> List[dict]:
    """
    extracting a book information with the standard expression from the HTML which is given by the parameter HTML
    the parameter base_url specifies the URK which is to be the standard when converted to the absolute URL
    returns: the lost of book (dict)
    """
    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url) #convered all hrefs in the a element

    #by cssselect() method, getting all a elemetns applied to the selctet and prcoessing each a element
    #the meaning of selector: the a element with "itemprop=url" passed down from the li element which is also passed forn from "id-listBook"

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        # getting the URL from the href of a element
        url = a.get('href')

        # getting the title of the book from the itemprop="title" in the p element
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content() #since it contains a wbr element, use text_content() not text_content

        books.append({'url': url, 'title': title})

    return books


def save(file_path: str, books: List[dict]):
    """
    save the list of books given by the parameter books as csv informat
    the path of the file is given by the parameter file_path
    no return
    """

    with open(file_path, 'w', newline='') as f:
        #specifing the file object in the first parameter and the list of the field names in the second parameter
        writer = csv.DictWriter(f, ['url', 'title'])
        writer.writeheader() #outputting the heade in the first row
        #outputting a multiple rows once. the parameter is the list of dict
        writer.writerows(books)

#calling the main() when the pythong command is executed. This is the basic idiom that prevents executing the main() as a module from another file which imports this file
if __name__ == '__main__':
    main()




# print('rank, city, population')
#
# #join methonの引数に渡す要素はStr
# print(','.join(['1', '上海', '24150000']))
# print(','.join(['2', 'カラチ', '2350000']))
# print(','.join(['3', '北京', '2151600']))
# print(','.join(['4', '天津', '147221000']))
# print(','.join(['5', 'イスタブル', '14160467']))
