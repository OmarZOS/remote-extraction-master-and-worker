

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from bot_studio import *
import re as re
from selenium.webdriver.common.by import By 
import win32clipboard
import os
from context import Context
from bs4 import BeautifulSoup as bs
from connect import connect
from context import Context






def get_container(username,password,page):
    print(password)
    print(username)
   
    connection=connect()

    browser=connect().connection(username,"aliali350**")
    browser.get(page + 'posts/')
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")


    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #uncomment to limit the number of scrolls
        #scroll_number += 1
        
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    company_page = browser.page_source  
    linkedin_soup = bs(company_page.encode("utf-8"), "html")
    linkedin_soup.prettify()

    containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})
    #container = containers[0].find("div","display-flex feed-shared-actor display-flex feed-shared-actor--with-control-menu ember-view")
    return containers


#post of page
def get_post_page(username,password,page):
    print("getposts page df")
    containers=get_container(username,password,page)
    post_dates = []
    post_texts = []
    post_likes = []
    post_comments = []
    video_views = []
    media_links = []
    media_type = []


    for container in containers:
        

        try:
            posted_date = container.find("span",{"class":"visually-hidden"})
            text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper"})
            text = text_box.find("span",{"dir":"ltr"})
            new_likes = container.findAll("li", {"class":"social-details-social-counts__reactions social-details-social-counts__item social-details-social-counts__reactions--with-social-proof"})
            new_comments = container.findAll("button", {"class": "social-details-social-counts__comments social-details-social-counts__item social-details-social-counts__item--with-social-proof"})
            
            post_dates.append(posted_date.text.strip())
             
            post_texts.append(text.text.strip())



            try:
                video_box = container.findAll("div",{"class": "feed-shared-update-v2__content feed-shared-linkedin-video ember-view"})
                video_link = video_box[0].find("video", {"class":"vjs-tech"})
                media_links.append(video_link['src'])
                media_type.append("Video")
            except:
                try:
                    image_box = container.findAll("div",{"class": "feed-shared-image__container"})
                    image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view"})
                    media_links.append(image_link['src'])
                    media_type.append("Image")
                except:
                    try:
                        #mutiple shared images
                        image_box = container.findAll("div",{"class": "feed-shared-image__container"})
                        image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"})
                        media_links.append(image_link['src'])
                        media_type.append("Multiple Images")
                    except:
                        try:
                            article_box = container.findAll("div",{"class": "feed-shared-article__description-container"})
                            article_link = article_box[0].find('a', href=True)
                            media_links.append(article_link['href'])
                            media_type.append("Article")
                        except:
                            try:
                                video_box = container.findAll("div",{"class": "feed-shared-external-video__meta"})          
                                video_link = video_box[0].find('a', href=True)
                                media_links.append(video_link['href'])
                                media_type.append("Youtube Video")   
                            except:
                                try:
                                    poll_box = container.findAll("div",{"class": "feed-shared-update-v2__content overflow-hidden feed-shared-poll ember-view"})
                                    media_links.append("None")
                                    media_type.append("Other: Poll, Shared Post, etc")
                                except:
                                    media_links.append("None")
                                    media_type.append("Unknown")



            #Getting Video Views. (The folling three lines prevents class name overlap)
            view_container2 = set(container.findAll("li", {'class':["social-details-social-counts__item"]}))
            view_container1 = set(container.findAll("li", {'class':["social-details-social-counts__reactions","social-details-social-counts__comments social-details-social-counts__item"]}))
            result = view_container2 - view_container1

            view_container = []
            for i in result:
                view_container += i

            try:
                video_views.append(view_container[1].text.strip().replace(' Views',''))

            except:
                video_views.append('N/A')


            try:
                post_likes.append(new_likes[0].text.strip())
            except:
                post_likes.append(0)
                pass

            try:
                post_comments.append(new_comments[0].text.strip())                           
            except:                                                           
                post_comments.append(0)
                pass
        
        except:
            pass
 
     
    data = {
        "Date_Posted": post_dates,
        "Media_Type": media_type,
        "Post_Text": post_texts,
        "Post_Likes": post_likes,
        
        "Post_Comments": video_views,
        "Media_Links": media_links
    }

   
     
    return data


    


def get_post_url(username,password,limit_posts,page):
    
    #get botton
    print("get all url post")
    browser=connect().connection(username,password)
    
    browser.get(page+"posts")
    time.sleep(3)
    list_url=[]
    last_height = browser.execute_script("return document.body.scrollHeight")

     #Scrolling
    SCROLL_PAUSE_TIME=3
    print("scrolling")
    try:
         
        while True:

                # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                #uncomment to limit the number of scrolls
                #scroll_number += 1

                # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        time.sleep(3)
        bottons=browser.find_elements_by_class_name("feed-shared-control-menu__trigger")
        
        lst=[]
        i=0
        for bt in bottons:
            if i > limit_posts:
                return list_url
            
            print("parser bottons")
            browser.execute_script("arguments[0].click();",  bt)
            time.sleep(2)

            targ=browser.find_element_by_class_name("artdeco-dropdown__content-inner")
    
            bbt=targ.find_elements_by_class_name("tap-target")
    
            browser.execute_script("arguments[0].click();", bbt[1])
            time.sleep(3)
            url= get_url()
            list_url.append(url)
            i=i+1

            time.sleep(3)
        return list_url
    except Exception as ex:
        print(ex)
        return list_url


        

    # get comment 
def get_comment_data(comment):
        
        try:
            data={}
            print("get_comment_data")
            com_split=comment['Comment'].split('\n')
            data['type']='comment'
            data['checked']=3

            data['comment_text']=com_split[6]
            data['nbre_likes']=com_split[8]
            data['nbre_replies']=com_split[10]
            
            return data
        except Exception as ex:
            
            print("error in get_user_comment_data")
            print(ex)
            return data



def get_user_comment_data(linkedin,comment,schema):
    print("get_user_comment_data")
    try:
        user_info=linkedin.get_profile(profile_link='https://www.linkedin.com'+comment ['User Link'])
        time.sleep(3)

        data={}
        #keys=comment.keys()
        for key in schema['user']:
            data[key]=user_info['body'][key]
        data['User Link']=comment ['User Link']
        data['UserName']=comment['UserName']
        data['type']='user'
        data['checked']=0
        print("ok_get_user_comment_data")
        return data
    except:
        print("error in get_user_comment_data")
        return data

def get_url():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    
    return data