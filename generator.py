import sys
import requests
import json
import random

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def printContents(msg, isQuote):
	if isQuote:
		print('\t\t"' + msg + '",')
	else:
		print('\t\t' + msg + ',')

baseUserURL = "https://randomuser.me/api/"
baseQuotesURL = "http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1"
enrol_min = 7
enrol_max = 8
course_id_min = 1
course_id_max = 138

print('[')
for x in range(20):
	print('\t[')

	# name, email
	response = requests.get(baseUserURL)
	person = json.loads(response.content)['results'][0]
	firstName = person['name']['first']
	lastName = person['name']['last']
	fullName = firstName.capitalize() + ' ' + lastName.capitalize()
	email = firstName + lastName + '@gmail.com'
	printContents(fullName, True)
	printContents(email, True)

	# bio
	response = requests.get(baseQuotesURL)
	quote = json.loads(response.content)[0]['content']
	quote = strip_tags(quote).replace('\n', '') # remove html tags
	quote = quote[:-2]
	printContents(strip_tags(quote).replace('\n', ''), True)

	# array of course id
	enrolNum = random.randint(enrol_min, enrol_max)
	courses = '['
	for e in range(enrolNum):
		courses = courses + str(random.randint(course_id_min, course_id_max)) + ','
	courses += ']'
	printContents(courses, False)

	print('\t],')
print(']')


