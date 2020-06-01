from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Disables printing to console.

option = str(input('[1] Join random lobby\n[2] Play with a friend\n\n> Select an option: '))
timeout = float(input('Timeout (in seconds, e.g 0.01): '))
started = False

if option == '1':
    driver = webdriver.Chrome(options=options)
    driver.get('https://play.typeracer.com/')
    sleep(2)
    
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]').click()
    except:
        pass

    driver.find_elements_by_css_selector('#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a')[0].click()
    print('\n[+] Found lobby.')
    sleep(2)

    all_text = driver.find_elements_by_css_selector('#gwt-uid-15 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div')[0].text

    while not started:
        try:
            for letter in all_text:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').send_keys(letter)
                sleep(timeout)
            started = True
        except:
            pass
    
    print('\n> Finished.')

elif option == '2':
    url = str(input('URL: '))
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(2)
    
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]').click()
    except:
        pass

    try:
        driver.find_elements_by_css_selector('#gwt-uid-17 > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2) > a')[0].click()
    except:
        print('\n> Invalid URL.')
    else:
        print('\n[+] Joined lobby.')
        sleep(2)

        all_text = driver.find_elements_by_css_selector('#gwt-uid-17 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div')[0].text

        while not started:
            try:
                for letter in all_text:
                    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').send_keys(letter)
                    sleep(timeout)
                started = True
            except:
                pass
        
        print('\n> Finished.')

else:
    print('Invalid option.')
