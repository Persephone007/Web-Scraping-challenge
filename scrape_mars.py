{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import time\n",
    "\n",
    "    def init_browser():\n",
    "    executable_path = {\"executable_path\": 'chromedriver.exe'}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "    \n",
    "    def scrape_info():\n",
    "    browser = init_browser()\n",
    "\n",
    "    mars_scrape = {}\n",
    "    \n",
    "    \n",
    "    \"\"\"\"\"\" news\n",
    "    url = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    results = soup.find('div', class_='list_text')\n",
    "\n",
    "    news_title = results.find(\"div\", class_=\"content_title\").text\n",
    "    news_p = results.find(\"div\", class_ =\"article_teaser_body\").text\n",
    "    mars_scrape[\"news_title\"] = news_title\n",
    "    mars_scrape[\"news_p\"] = news_p\n",
    "    \n",
    "    \"\"\"\"\"\" nasa image\n",
    "    mars = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(mars)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "    find_img = soup.find('img', class_=\"thumb\")\n",
    "    img = find_img.get('src')\n",
    "    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23511-640x350.jpg'\n",
    "    mars_scrape[\"featured_image_url\"] = featured_image_url\n",
    "\n",
    "    \"\"\"\"\"\" weather\n",
    "    twitter = \"https://twitter.com/MarsWxReport/status/1196244436252078080\"\n",
    "    browser.visit(twitter)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "    mars_weather = soup.find('div', class_='js-tweet-text-container').text\n",
    "    mars_scrape[\"mars_weather\"] = mars_weather\n",
    "    \n",
    "    \"\"\"\"\"\" mars facts\n",
    "    mars_facts = \"https://space-facts.com/mars/\"\n",
    "    mars_tables = pd.read_html(mars_facts)\n",
    "    facts_df = pd.DataFrame(mars_tables[0])\n",
    "    mars_scrape[\"facts_df\"] = facts_df\n",
    "\n",
    "    \"\"\"\"\"\" henispheres\n",
    "    \n",
    "    hemisphere_image_urls = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": \"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif\"},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif\"},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif\"},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": \"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif\"},\n",
    "]\n",
    "    \n",
    "    mars_scrape[\"hemisphere_image_urls\"] = hemisphere_image_urls\n",
    "    \n",
    "    return mars_scrape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
