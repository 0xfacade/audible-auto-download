#!/bin/env python3

import pickle
import getpass

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import requests

email = input("E-Mail: ")
pw = getpass.getpass("Password: ")

print("Browsing to audible..")

opts = Options()
opts.headless = True

browser = Firefox(options=opts)
browser.get("https://www.audible.de/")

print("Trying to login..")
links = browser.find_elements_by_partial_link_text("Anmelden")
links[0].click()
input_ = browser.find_element_by_id("ap_email")
input_.send_keys(email)
input_ = browser.find_element_by_id("ap_password")
input_.send_keys(pw)

submit = browser.find_element_by_id("signInSubmit")
submit.click()

browser.get("https://www.audible.de/lib?pageSize=50")

try:
    table = browser.find_elements_by_css_selector("table.bc-table")[0]
except:
    print("Failed to login. Check email and password.")
    exit(1)

print("Retrieving list of audiobooks.")

rows = table.find_elements_by_tag_name("tr")

# row 0 is the title row
audiobooks = []
for row in rows[1:]:
    links = row.find_elements_by_tag_name("a")
    if len(links) < 4:
        continue

    title = links[1].text

    shift = 0
    if "Serie anzeigen" in row.text:
        shift += 1
    if "Downloadteile anzeigen" in row.text:
        shift += 1

    author = links[2 + shift].text
    url = links[4 + shift].get_attribute("href")
    
    audiobooks.append((author, title, url))
    print(f'Found "{title}" by "{author}".')

cookies = browser.get_cookies()

print("Writing cookies..")
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies:
    jar.set(cookie["name"], cookie["value"], 
            domain=cookie["domain"],
            path=cookie["path"])

with open("cookies.pickle", "wb") as f:
    pickle.dump(jar, f)

with open("audiobooks.pickle", "wb") as f:
    pickle.dump(audiobooks, f)

print(f"Done. Found {len(audiobooks)} audiobooks.")

