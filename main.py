import csv, json, time

from selenium.webdriver import Firefox

def main():
  creds = json.load(open('cred.ignore.json'))

  try:
    browser = Firefox()
    browser.get('https://myturbotax.intuit.com/')
    login(browser, creds)
    navigate_to_stocks(browser)
    # browser.quit()
  except Exception as e:
    # browser.quit()
    raise e

def login(b, credentials):
  el = b.find_element_by_id('ius-userid')
  el.send_keys(credentials['username'])
  el = b.find_element_by_id('ius-password')
  el.send_keys(credentials['password'])
  el.submit()
  time.sleep(4)

def navigate_to_stocks(br):
  # "Take me to my return" link
  l = br.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/div[2]/div[1]/div[1]/div[3]/a')
  l.click()
  time.sleep(4)

  # Federal on sidebar
  l = br.find_element_by_xpath('/html/body/div[2]/div/div[3]/section/div/div[1]/div/div[2]/div[2]/div/section/div/div[4]/a')
  l.click()
  time.sleep(1)

  # stock options button
  l = br.find_element_by_id('MyStuff-OverviewGroup-Item-STOCKSALES-4-EditAction')
  l.click()
  time.sleep(2)

if __name__ == '__main__':
  main()
