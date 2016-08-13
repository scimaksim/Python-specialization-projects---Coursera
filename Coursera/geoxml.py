import urllib
import xml.etree.ElementTree as ET

# Sum = sum of all number, count = number of values extracted
sum = 0
count = 0

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    tree = ET.fromstring(data)
    results = tree.findall('comments/comment')
    for each_result in results:
        num = each_result.find('count').text
        sum += int(num)
        count += 1
    break

print 'Count:', count
print 'Sum:', sum


