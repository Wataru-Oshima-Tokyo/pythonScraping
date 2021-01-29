from pyquery import PyQuery as pq

#get a PyQuery object by reading HTML file
d =pq(filename ='dp.html')
d.make_links_absolute('https://gihyo.jp/dp') #change all hte links to absoulute url

#obtain the list of a elements applied to d() selector and process to each a element)

for a in d('#listBook >li > a[itemprop="url"]'):
    #get the url of the book from href attribute in an a element
    #since it's lxml element obtained from a valuable, obtain PyQuery object as d(a)
    url = d(a).attr('href')

    # get the title of the book from p element which has itemprop="name" attribute
    p = d(a).find('p[itemprop="name"]').eq(0)
    title = p.text()

    #output the url and the title
    print(url, title)
