<h1> WebScraping Homework </h1>
<br>
<body>
	<h2>Scraping in Jupyter Notebook</h2>
<p>
For my project, I used splinter and requests to help scrape the information I needed. 
Using Jupyter notebook, I scraped for the following information: 
<br>
<em>(please refer to the "mission_to_mars.ipynb" file)<em>
<ul>
<li><h3>Latest Title and Article Teaser </h3>
<code>html = browser.html
soup = bs(html, 'html.parser')
li = soup.find('li', class_='slide')
title = li.find('div', class_='content_title').text
paragraph = li.find('div', class_='article_teaser_body').text</code><br>
Output: Title: NASA's Perseverance Rover Will Look at Mars Through These 'Eyes' - Article Teaser:
A pair of zoomable cameras will help scientists and rover drivers with high-resolution color images.
<br>
<li><h3>Main Image</h3>
	<code> img = soup2.find('img', class_='main_image')['src']     
	<br>img_url = base_url + img </ br>
img_url </code> 
Output: 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA14934_hires.jpg'
<br>
<li><h3>Mars Weather</h3>
	<code> html3 = requests.get('https://twitter.com/marswxreport?lang=en').text <br>
	soup3 = bs(html3, 'html.parser') <br>
	tweet_find = soup3.find('p', class_='tweet-text').text <br>
	tweet_find</code> <br>
<br>
Output: 'InSight sol 504 (2020-04-27) low -93.6ºC (-136.5ºF) high -6.7ºC (20.0ºF)\nwinds from the SW at 4.6 m/s (10.3 mph) gusting to 15.0 m/s (33.6 mph)\npressure at 6.80 hPapic.twitter.com/U8P9d9J696'
<br>
<li><h3>Mars Information</h3>
<code>url4 = 'https://space-facts.com/mars/'
mars_data = pd.read_html(url4)[0]
mars_data2 = mars_data.rename(columns = {0: 'Metrics', 1: 'Values'})
mars_data2</code><br>
Output: Metrics	Values
0	Equatorial Diameter:	6,792 km
1	Polar Diameter:	6,752 km
2	Mass:	6.39 × 10^23 kg (0.11 Earths)
3	Moons:	2 (Phobos & Deimos)
4	Orbit Distance:	227,943,824 km (1.38 AU)
5	Orbit Period:	687 days (1.9 years)
6	Surface Temperature:	-87 to -5 °C
7	First Record:	2nd millennium BC
8	Recorded By:	Egyptian astronomers
<br>
<li><h3>Hemisphere Image URLs</h3>
<code>browser.visit(url5)
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
pd.DataFrame(hemisphere)</code><br>
<br>
Output: 	title	img_url
0	Cerberus Hemisphere Enhanced	http://astropedia.astrogeology.usgs.gov/downlo...
1	Schiaparelli Hemisphere Enhanced	http://astropedia.astrogeology.usgs.gov/downlo...
2	Syrtis Major Hemisphere Enhanced	http://astropedia.astrogeology.usgs.gov/downlo...
3	Valles Marineris Hemisphere Enhanced	http://astropedia.astrogeology.usgs.gov/downlo...
	</li> </ul></p>
