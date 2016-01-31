from selenium import webdriver
import unittest

browser = webdriver.Firefox()

browser.get("http://localhost:8000")

assert 'To-Do' in browser.title, "browser title was: "+browser.title

browser.quit()
