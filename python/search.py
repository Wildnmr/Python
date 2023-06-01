# search utility

import re

text = "the phone number for the area is even to the phone number of the county"

#to check for a text in  a sentense

'phone' in text

# to use search tool

# set pattern you looking for

pattern = 'phone'

match = re.search(pattern, text)




matches = re.findall('phone', text)

for match in re.finditer('phone', text):
    print(match)
    
    
match
matches












