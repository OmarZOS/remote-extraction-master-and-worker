from lib2to3.pgen2 import driver
from click import command
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  
import time
from bs4 import BeautifulSoup
import pandas as pd
from context  import Context
import networkx as nx
from selenium.webdriver.common.by import By


import json




def get_user_name_password():
    config_data=None
    with open ('config.json') as json_file:
        config_data=json.load(json_file)
    return config_data["facebook"]


  
def get_driver():
    option = Options()
    option.add_argument("--disable-infobars")
    #option.add_argument("--disable-notifactions")
   
    option.add_argument("start-maximized")
    #option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })
 #   driver = webdriver.Chrome(service=s)
    driver1 = webdriver.Chrome(executable_path="chromedriver.exe", options=option)

    driver1.maximize_window()
    return driver1




def get_friends_user(email,password,account,nb_friends):
    print("scrapping friends")
    
    driver1=get_driver ()
    driver1.get("https://www.facebook.com")
    try:
        username_el=driver1.find_element(By.ID, "email")
        password=driver1.find_element(By.ID, "pass")
        sub=driver1.find_element(By.NAME,'login')
        

        username_el.send_keys("alilamri350@gmail.com")


        password.send_keys("aliali19980*")  
 
        sub.click()
       
        length=0

        #account="journalmaracanaalgerie"
        
        
        time.sleep(3)
        driver1.get("https://www.facebook.com/"+account+"/friends")
        time.sleep(3)
         
        list_friends=[]
        
        time.sleep(3)
        while True:

           
            
            soup=BeautifulSoup(driver1.page_source,"html.parser")
            users=driver1.find_elements(By.XPATH, '//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8"]')
            time.sleep(3)
            for user in users:
                 
                 
                try:
                    if len(list_friends)<= nb_friends:
                            
                        
                        if get_id(user.get_attribute("href")) not in list_friends:

                            list_friends.append(get_id(user.get_attribute("href")))
                    else:
                        print("end add user list")
                        print(list_friends)
                        return list_friends
                        driver1.close()
                        break
                      
                       
                except Exception as ex:
                    
                    print(ex)
                
            if len(list_friends)< nb_friends:
                print("end add user list")
                return list_friends
                driver1.close()


            #scroll  
            y=500
             
            for i in range(0,25):
                driver1.execute_script("window.scrollTo(0, "+str(y)+")")
                y=y+500
        
            
       
        print("end add user list")
        return list_friends
        driver1.close()




    except Exception as ex :
        print(ex)
        print("error")
        return list_friends
        driver1.close()

 
def get_id(href):

    id=href.split('/')[-1]
    return id.split('=')[-1]
 
 