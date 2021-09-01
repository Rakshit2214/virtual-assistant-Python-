from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pvporcupine
import os
import time

import datetime
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3
import pvporcupine
import pyaudio
import struct
rem = webdriver.ChromeOptions()
rem.add_experimental_option("excludeSwitches", ["enable-automation"])

rem = webdriver.ChromeOptions()
rem.add_experimental_option("excludeSwitches", ["enable-automation"])

browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe", options=rem)

browser.get("https://open.spotify.com/search")

browser.maximize_window()
wait_for_page_load(browser)
# browser.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
browser.find_element_by_xpath("//button[@data-testid='login-button']").click()
loadup('/html/body/div[1]/div[2]/div/form/div[1]/div/input')
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/div/input').send_keys(
    'rakshitwalia2002@gmail.com')
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/div/input').send_keys(
    'jaideep1234')
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/div[2]/button').click()
wait_for_page_load(browser)
assert "Spotify" in browser.title

command = command.replace("play", "")
loadup("//input[@data-testid='search-input']")
browser.find_element_by_xpath("//input[@data-testid='search-input']").send_keys(
    command + Keys.RETURN)
loadup("//button[@data-testid='play-button']")
ac = ActionChains(browser)
k = browser.find_element_by_xpath("//button[@data-testid='play-button']")
ac.move_to_element(k).perform()
sleep(0.5)
ac.click().perform()