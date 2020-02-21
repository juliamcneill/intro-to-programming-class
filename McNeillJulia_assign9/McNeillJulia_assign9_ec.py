"""
McNeillJulia_assign9_ec

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 3 December, 2019
"""
#I don't know how to do this the way described in the prompt, but this is
#the way I learned how to do it in another class

import feedparser

rss_url = 'http://rss.nytimes.com/services/xml/rss/nyt/Science.xml'

feed = feedparser.parse(rss_url)

print("Feed Title: "

for i in range(len(eed)): 
    print(feed['entries'][i]['title']) 
    
