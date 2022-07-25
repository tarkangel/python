import json

array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
print (data['fruits'])
# the print displays:
# [u'apple', u'banana', u'orange']