# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
final_count = int(raw_input('Enter count: '))
final_position = int(raw_input('Enter position: '))

iteration_num = 0

print url

while iteration_num < final_count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')

    print tags[final_position-1].get('href', None)
    url = tags[final_position-1].get('href', None)

    iteration_num += 1
