from selenium import webdriver
from random import randrange
import time

url = "https://kingoftheclicks.com/?ref=thekingoftheclicks"
browser = webdriver.Chrome('/Users/isaiah/Desktop/Code/Python/king-of-the-clicks/chromedriver')
browser.get(url)

time.sleep(2)
browser.find_element_by_xpath('//*[@id="__layout"]/div/main/div[3]/div[2]/div/div/div/footer/button[1]').click()
time.sleep(2)

i = 1

while(True):
    browser.find_element_by_xpath('//*[@id="__layout"]/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span').click()
    print(i)
    i = i+1
    browser.find_element_by_xpath('//*[@id="__layout"]/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span').click()
    print(i)
    i = i+1
    browser.find_element_by_xpath('//*[@id="__layout"]/div/main/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span').click()
    print(i)
    i = i+1
