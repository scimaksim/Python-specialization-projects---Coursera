import urllib
import json

sum = 0

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    info = json.loads(data)

    print 'Number of items in dictionary:', len(info)
    print 'User count:', len(info['comments'])

    #Comments is a list of dictionary key-value pairs
    for item in info['comments']:
        sum += int(item['count'])

    print 'The sum of all counts is:', sum






