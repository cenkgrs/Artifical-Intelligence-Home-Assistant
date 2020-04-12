from flask import Flask, render_template
from selenium import webdriver
import pyautogui as pyautogui
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


def start():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("dom.webnotifications.enabled", False)
    profile.set_preference("general.useragent.override", "Mozilla/5.0")
    profile.update_preferences()
    browser = webdriver.Firefox(firefox_profile=profile, executable_path='/usr/local/bin/geckodriver')

    app.run(debug=True)
    browser.get("http://127.0.0.1:5000/")
    pyautogui.press('f11')

