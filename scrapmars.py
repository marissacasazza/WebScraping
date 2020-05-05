import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser

def scrape_all():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', executable_path, headless = False)
    
    title, paragraph = mars_news(browser)
    
    return{
    "news_title": title,
    "news_p": paragraph,
    "img": mars_img(browser),
    "weather": mars_weather(),
    "mars_info": mars_data(),
    "hemispheres": hemisphere(browser)

    }

def mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    li = soup.find('li', class_='slide')
    title = li.find('h3').text
    paragraph = li.find('div', class_='article_teaser_body').text

    return title, paragraph

def mars_img(browser):
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov'
    browser.visit(url2)
    browser.find_by_id('full_image').click()
    browser.links.find_by_partial_text('more info').click()

    html2 = browser.html
    soup2 = bs(html2, 'html.parser')

    img = soup2.find('img', class_='main_image')['src']
    img_url = base_url + img
    return img_url
    
def mars_weather():
    html3 = requests.get('https://twitter.com/marswxreport?lang=en').text
    soup3 = bs(html3, 'html.parser')
    tweet_find = soup3.find('p', class_='tweet-text').text

    return tweet_find

def mars_data():
    url4 = 'https://space-facts.com/mars/'
    mars_data = pd.read_html(url4)[0]
    mars_data2 = mars_data.rename(columns = {0: 'Metrics', 1: 'Values'})

    mars_bootstrap = mars_data2.to_html(classes='table table-striped')

    return mars_bootstrap

def hemisphere(browser):
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    html4 = browser.html
    soup4 = bs(html4, 'html.parser')

    results = soup4.find_all('h3')

    hemisphere = []

    for i in range(len(results)):
        
        browser.find_by_tag('h3')[i].click()
        loop_soup = bs(browser.html, 'html.parser')
        downloads = loop_soup.find('div', class_='downloads').find('a')['href']
        
        
        title = loop_soup.find('h2', class_='title').text
        #print(title + downloads)
        dictionary = {'title':title, 'img_url':downloads}
        hemisphere.append(dictionary)
        
        browser.back()
    browser.quit()   
    return hemisphere
