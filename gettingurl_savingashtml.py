import sys
import requests

url = sys.argv[1]
r = requests.get(url)
print(f'encoding: {r.encoding})', file=sys.stderr)
print(r.text)

"""
put the below code onto the terminal to make this program work
(scrapying)$ python "this file name" "the url you want to get" > "name".html
you do not have to include the double quotes
"""
