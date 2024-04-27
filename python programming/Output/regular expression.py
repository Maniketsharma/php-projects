import re
mystr='''Tata Motors International Business
A Block, Shivasagar Estate,
Dr. Annie Besant Road,
Worli, Mumbai - 400018
Contact: +91(22) 67577200


Domestic Business
Tata Motors Ltd
4th Floor, Ahura Centre
82 Mahakali Caves Road
MIDC, Andheri East
Mumbai - 400093
Contact: 022 - 62407101'''
patt =  re.compile(r'\d{3}-\d{4}')

matches = patt.finditer(mystr)
for match in matches:
      print(match)