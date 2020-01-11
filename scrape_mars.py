import pandas as pd
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
    
#def scrape_info():
    #browser = init_browser()
mars_scrape = {}
    
def news():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    response = requests.get(url)
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('div', class_='list_text')

    news_title = results.find("div", class_="content_title").text
    news_p = results.find("div", class_ ="article_teaser_body").text
    mars_scrape["news_title"] = news_title
    mars_scrape["news_p"] = news_p
    return mars_scrape

    browser.quit()
    
def nasa_image():
    browser = init_browser()
    mars = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    find_img = soup.find('img', class_="thumb")
    img = find_img.get('src')
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23511-640x350.jpg'
    mars_scrape["featured_image_url"] = featured_image_url
    return mars_scrape

    browser.quit()

def weather():
    browser = init_browser()
    twitter = "https://twitter.com/MarsWxReport/status/1196244436252078080"
    browser.visit(twitter)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    mars_scrape["mars_weather"] = mars_weather
    return mars_scrape

    browser.quit()

def mars_facts():
    browser = init_browser()
    mars_facts = "https://space-facts.com/mars/"
    mars_tables = pd.read_html(mars_facts)
    facts_df = pd.DataFrame(mars_tables[0])
    mars_scrape["facts_df"] = facts_df
    return mars_scrape

    broswer.quit()

def hemispheres():
    browser = init_browser()
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url":      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
    {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
]
    
    mars_scrape["hemisphere_image_urls"] = hemisphere_image_urls
    
    return mars_scrape

    browser.quit()