import sys
import requests

url = sys.argv[0]
r = requests.get(url)
print(f'encoding: {r.encoding}', file=sys.stderr)
print(r.text)
