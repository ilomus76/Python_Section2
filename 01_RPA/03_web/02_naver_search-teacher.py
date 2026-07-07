from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options= Options()
options.add_experimental_option('detach', True)

chrome= webdriver.Chrome(options)
chrome.get('https://www.naver.com')


#sp


