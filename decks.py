from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
import json
import time


def main():
    # initialize json file
    f = open("deck-stats.json", "w")
    f.write("[\n")
    # initialize browser and logs in
    profile = FirefoxProfile(r"C:\Users\matth\AppData\Roaming\Mozilla\Firefox\Profiles\wb2ce82q.default-release")
    browser = webdriver.Firefox(profile)
    browser.implicitly_wait(10)

    # url = "https://hsreplay.net/"
    # browser.get(url)
    # browser.find_element(By.CLASS_NAME, 'button-container').click()
    # time.sleep(5)
    # browser.find_element(By.CLASS_NAME, 'form-group').click()
    # time.sleep(5)
    # browser.find_element(By.ID, 'accountName').send_keys('gaming.misdeed@gmail.com')
    # time.sleep(5)
    # browser.find_element(By.ID, 'password').send_keys('naCqQMy2')
    # time.sleep(2)
    # browser.find_element(By.ID, 'submit').click()
    # time.sleep(5)

    page = 0
    while page < 2:
        page += 1
        browser.get("https://hsreplay.net/decks/#rankRange=TOP_1000_LEGEND&timeRange=CURRENT_EXPANSION&gameType=RANKED_CLASSIC&sortBy=winrate&page=" + str(page))
        # locates information
        decks = browser.find_element(By.CSS_SELECTOR, 'div.deck-list-wrapper')
        roles = decks.find_elements(By.CLASS_NAME, 'deck-name')
        winrates = decks.find_elements(By.CLASS_NAME, 'win-rate')
        games = decks.find_elements(By.CLASS_NAME, 'game-count')
        durations = decks.find_elements(By.CLASS_NAME, 'duration')
        decklists = decks.find_elements(By.CLASS_NAME, 'card-list')

        for i in range(len(roles)):
            cards = decklists[i].find_elements(By.CLASS_NAME, 'card-icon')
            # print(f"{roles[i].text}\t{winrates[i].text}\t{games[i].text}\t\t{durations[i].text}")
            decklist = []
            for j in range(len(cards)):
                decklist.append(cards[j].get_attribute('aria-label'))
            deck = {
                "class": roles[i].text,
                "winrate": winrates[i].text,
                "games": games[i].text,
                "duration": durations[i].text,
                "list": decklist
            }
            # removes trailing comma
            if i != len(roles) - 1:
                f.write(json.dumps(deck) + ",\n")
            else:
                f.write(json.dumps(deck) + "\n")

    f.write("]")
    f.write("[\n")




if __name__ == '__main__':
    main()
