from selenium import webdriver
from selenium.webdriver import FirefoxProfile, Keys
from selenium.webdriver.common.by import By
import json
import time
import os


def main():
    # initialize browser
    profile = FirefoxProfile(r"C:\Users\matth\AppData\Roaming\Mozilla\Firefox\Profiles\wb2ce82q.default-release")
    browser = webdriver.Firefox(profile)
    browser.implicitly_wait(10)

    # loops through each of the 9 class pages
    roles = ['DRUID', 'HUNTER', 'MAGE', 'PALADIN', 'PRIEST', 'ROGUE', 'SHAMAN', 'WARLOCK', 'WARRIOR']
    for role in roles:
        filename = role.lower() + '.json'
        with open(os.path.join(r'C:\Users\matth\Desktop\PL\GeoJSON\card-stats', filename), 'w') as f:
            f.write("[\n")
            browser.get("https://hsreplay.net/cards/#rankRange=LEGEND&playerClass=" + role + "&timeRange=CURRENT_EXPANSION&gameType=RANKED_CLASSIC")
            # scrolls up+down to load table on first iteration
            if role == 'DRUID':
                time.sleep(2)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                browser.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_UP)
                time.sleep(2)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # loads all names, costs, and table cells
            costs = browser.find_elements(By.CLASS_NAME, 'card-cost')
            names = browser.find_elements(By.CLASS_NAME, 'card-name')
            cells = browser.find_elements(By.CLASS_NAME, 'table-cell')
            j = 0
            for i in range(0, len(cells), 7):
                card = {
                    "name": names[j].text,
                    "cost": costs[j].text,
                    "popularity": cells[i].text,
                    "avg-copies": cells[i+1].text,
                    "deck-winrate": cells[i+2].text,
                    "times-played": cells[i+3].text,
                    "mulligan-winrate": cells[i+4].text,
                    "kept-percent": cells[i+5].text,
                    "drawn-winrate": cells[i+6].text
                }
                # remove trailing comma
                if j != len(names)-1:
                    f.write(json.dumps(card) + ",\n")
                else:
                    f.write(json.dumps(card) + "\n")
                j += 1
            f.write("]")


if __name__ == '__main__':
    main()
