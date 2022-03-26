
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


class connect:

        def __init__(self):
            print("connection")

        def connection(self,username1,password1):
            #create contexte
            driver = webdriver.Chrome("chromedriver")
     
            driver.get("https://linkedin.com/uas/login")
            
            print(username1)
           
            print(password1)

            # waiting for the page to load
            time.sleep(5)
            
            username = driver.find_element_by_id("username")
            
            username.send_keys(username1)

            
            pword = driver.find_element_by_id("password")
            
            pword.send_keys(password1)		

            
            driver.find_element_by_xpath("//button[@type='submit']").click()
            return driver


