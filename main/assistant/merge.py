from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

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
import pvporcupine
import pyaudio
import struct
handle = pvporcupine.create(keywords=['bumblebee'])

def get_next_audio_frame():
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(rate=handle.sample_rate, channels=1, format=pyaudio.paInt16, input=True,
                           frames_per_buffer=handle.frame_length, input_device_index=None)
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    return pcm
def loadup(s):
    k = ''
    while not k:
        try:
            k = browser.find_element_by_xpath(s)
        except:
            continue
def wait_for_page_load(self, timeout=10):
    self.log.debug("Waiting for page to load at {}.".format(self.driver.current_url))
    old_page = self.find_element_by_tag_name('html')
    yield
    WebDriverWait(self, timeout).until(staleness_of(old_page))

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

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

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good night")


class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    def run(self):
        self.XiaoAI()



    def XiaoAI(self):
        wish()
        engine.say("my name is bumble bee, call me anytime")

        engine.say(("switching to standby mode now"))
        engine.runAndWait()
        try:
            nb = 0
            while (nb != 4):
                command = ''
                if (nb == 1):

                    while True:
                        pcm = get_next_audio_frame()
                        keyword_index = handle.process(pcm)
                        if keyword_index == 0:
                            break
                    engine.say("can i help you with anything else, reply with YES or NO")
                    engine.runAndWait()


                    with sr.Microphone() as source:
                        print("listening...")
                        voice = lss.listen(source)
                        command = lss.recognize_google(voice)
                        command.lower()
                    if "yes" in command:
                        engine.say("listening now")
                        engine.runAndWait()
                        print("listening...")
                        with sr.Microphone() as source:
                            voice = lss.listen(source)
                            command = lss.recognize_google(voice)
                            command = command.lower()
                    if 'no' in command:
                        nb=4
                        sys.exit()

                if (nb == 0):



                    while True:
                        pcm = get_next_audio_frame()
                        keyword_index = handle.process(pcm)
                        if keyword_index == 0:
                            break

                    engine.say("speak idiot")
                    engine.runAndWait()
                    with sr.Microphone() as source:
                        engine.say("listening")
                        print("listening...")
                        voice = lss.listen(source)
                        command = lss.recognize_google(voice)
                        nb = 1


                command = command.lower()
                if 'instagram' in command:
                    command = command.replace("open", "")
                    browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
                    browser.get("https://www.instagram.com/accounts/login/")
                    loadup("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
                    assert "Instagram" in browser.title
                    elem = browser.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(
                        'rakshitwalia2003')

                    b = browser.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(
                        "jaideep123")
                    browser.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div").click()
                    loadup("/html/body/div[4]/div/div/div/div[3]/button[2]")
                    browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
                elif ('play' in command.lower() and 'youtube' not in command.lower()):

                    rem = webdriver.ChromeOptions()
                    rem.add_experimental_option("excludeSwitches", ["enable-automation"])

                    browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe", options=rem)

                    browser.get("https://open.spotify.com/search")

                    browser.maximize_window()
                    wait_for_page_load(browser)
                    browser.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
                    #browser.find_element_by_xpath("//button[@data-testid='login-button']").click()
                    k = ''
                    while not k:
                        try:
                            k = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/div/input')
                        except:
                            continue
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/div/input').send_keys('rakshitwalia2002@gmail.com')
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/div/input').send_keys('jaideep1234')
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/div[2]/button').click()
                    wait_for_page_load(browser)
                    assert "Spotify" in browser.title

                    command = command.replace("play", "")
                    k = ''
                    while not k:
                        try:
                            k = browser.find_element_by_xpath("//input[@data-testid='search-input']")
                        except:
                            continue
                    browser.find_element_by_xpath("//input[@data-testid='search-input']").send_keys(command + Keys.RETURN)
                    k = ''
                    while not k:
                        try:
                            k = browser.find_element_by_xpath("//button[@data-testid='play-button']")
                        except:
                            continue
                    ac = ActionChains(browser)
                    k = browser.find_element_by_xpath("//button[@data-testid='play-button']")
                    ac.move_to_element(k).perform()
                    sleep(0.5)
                    ac.click().perform()



                elif ('close' in command):
                    nb = 4
                    engine.say("closing now")
                    engine.runAndWait()
                    sys.exit()
                elif ('youtube' in command.lower()):
                    command = command.lower()
                    browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
                    browser.get("https://www.youtube.com/")

                    wait_for_page_load(browser)

                    command = command.replace("play", "")
                    command = command.replace("in youtube", "")
                    browser.find_element_by_xpath(
                        "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys(
                        command + Keys.RETURN)
                    loadup("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
                    browser.find_element_by_xpath(
                        "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()

                else:
                    command = command.replace("search", "")
                    o = command

                    browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
                    browser.get("https://www.google.co.in/")
                    browser.maximize_window()
                    wait_for_page_load(browser)
                    assert "Google" in browser.title
                    browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(o + Keys.RETURN)


        except:
            engine.say("you killed me")
            engine.runAndWait()
            sys.exit()


FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920, 1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.jpg"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())