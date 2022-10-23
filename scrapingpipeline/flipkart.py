from http.server import executable
import random
import pandas as pd
# fetch mongodb class so that we can store data
from db.index import MongoDBManagement
#  fetch configuration
from config.index import ObjectRepo
# selenium based imports inorder to perform data fetching pipeline
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class scrapper_flip:
    """
    """
    def __init__(self,executable_path, chrome_options):
        try:
            self.driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
        except Exception as e:
            raise Exception(f"(__init__): something went wrong while initialization of driver. Error: {str(e)}")

    def openURL(self,url):
        """
        """
        try:
            if self.driver:
                self.driver.get(url)
                return True
        except Exception as e:
            raise Exception(f"(openURL): something went wrong while opening link: {url}. Error: {str(e)}")

    