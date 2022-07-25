import json

array = '{"fruits": ["apple", "banana", "orange","coconut"]}'
data  = json.loads(array)
print (data['fruits'])
# the print displays:
# [u'apple', u'banana', u'orange']