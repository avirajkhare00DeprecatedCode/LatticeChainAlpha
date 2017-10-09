from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def generate_keys():

    key_dict = []

    driver = webdriver.Chrome('/Users/avirajkhare00/money/projectx/service1/core/chromedriver')
    driver.get("file:///Users/avirajkhare00/money/wallets/neopaperwalletorg/generate.html")
    #time.sleep(2)
    public_key = driver.find_element_by_id("neo-public-key")
    private_key = driver.find_element_by_id("wif_")
    print "---GENERATING NEO PUBLIC AND PRIVATE KEYS---"
    print "PUBLIC KEY- " + public_key.text
    print "PRIVATE_KEY- " + private_key.text
    print "---END NEO PUBLIC AND PRIVATE KEY---"
    key_dict.append({
        "neo_public_key" : public_key.text,
        "neo_private_key" : private_key.text
    })

    driver.get("file:///Users/avirajkhare00/money/wallets/universal_wallet/index.html")

    driver.find_element_by_xpath('//*[@id="seedSkipper"]/a').click()

    #time.sleep(2)

    print "BITCOIN PUBLIC ADDRESS- " + driver.find_element_by_xpath('//*[@id="btcaddress"]').text
    print "BITCOIN PRIVATE ADDRESS- " + driver.find_element_by_xpath('//*[@id="btcprivwif"]').text

    key_dict.append(
        {
            "bitcoin_public_key" : driver.find_element_by_xpath('//*[@id="btcaddress"]').text,
            "bitcoin_private_key" : driver.find_element_by_xpath('//*[@id="btcprivwif"]').text
        }
    )


    driver.close()

    return key_dict