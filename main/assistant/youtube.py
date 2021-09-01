from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3
import pvporcupine
import pyaudio
import pvporcupine
import os
import time
import sys
import datetime
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3
import struct
rem = webdriver.ChromeOptions()
rem.add_experimental_option("excludeSwitches", ["enable-automation"])
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
lss = sr.Recognizer()
def loadup(s):
    k = ''
    while not k:
        try:
            k = browser.find_element_by_xpath(s)
        except:
            continue
rem = webdriver.ChromeOptions()
rem.add_experimental_option("excludeSwitches", ["enable-automation"])
browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe", options=rem)
browser.maximize_window()
with sr.Microphone() as source:
    engine.say("listening")
    print("listening...")
    voice = lss.listen(source)
    command = lss.recognize_google(voice)
    nb = 1


command = command.lower()
browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
browser.get("https://www.youtube.com/")

wait_for_page_load(browser)

command = command.replace("play", "")
command = command.replace("in youtube", "")
browser.find_element_by_xpath(
    "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys(command + Keys.RETURN)
loadup("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
browser.find_element_by_xpath(
    "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()
