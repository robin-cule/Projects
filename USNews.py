from bs4 import BeautifulSoup
import requests
import re

## Loading the webpage and parsing it into beautifulsoup object
url2 = "https://www.usnews.com"
user_agent2 = {'User-Agent':"Mozilla/5.0"}
page2 = requests.get(url2, headers = user_agent2)
soup2 = BeautifulSoup(page2.text,'lxml')


## Extracting the second top story from the front page
top_stories = soup2.select('div.Box-w0dun1-0.ContentBox__Container-sc-1egb8dt-0.iZCosX.lmOexQ.ArmRestTopStories__CollapseBorderContentBox-s0vo7p-2.fTDCpH.ArmRestTopStories__CollapseBorderContentBox-s0vo7p-2.fTDCpH h3.Heading-sc-1w5xk2o-0.ContentBox__StoryHeading-sc-1egb8dt-3.MRvpF.fqJuKa.story-headline a')
second_top = top_stories[1]
second_top_url = second_top['href']

## Printing the second top story url
print(second_top_url)


## Going to the second top story url 
second_page = requests.get(second_top_url, headers = user_agent)
second_top_soup = BeautifulSoup(second_page.text,'lxml')

Headers = second_top_soup.select('h1.Heading-sc-1w5xk2o-0.iQhOvV')
## Heading ( Story Name) 
Headers[0].text


## Extracting the texts from the main body 
Main_body = second_top_soup.select('div.Raw-slyvem-0.bCYKCn p')
sent = []

## Extracting first three sentences
for sente in Main_body:
    sent.append(sente.text)
summary = sent[:3]


## Defining an empty string to store the sentences
answer = ''

for x in summary:
    answer = answer + x

sentences = re.split('\. |:|;', answer)
first_three = ' '.join(sentences[:3])


print(first_three)









