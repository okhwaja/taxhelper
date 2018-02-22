import csv, json
from time import sleep
from dateutil import parser

from selenium.webdriver import Firefox

class TaxHelper():
  def __init__(self, cred_path, csv_path, start_index=0):
    self.credentials = json.load(open(cred_path))
    self.start_index = start_index
    self.csv_path = csv_path

  def load_browser(self):
    browser = Firefox()
    browser.get('https://myturbotax.intuit.com/')
    browser.implicitly_wait(7)
    self.br = browser

  def load_trades(self):
    with open(self.csv_path) as csvfile:
      reader = csv.DictReader(csvfile)
      return [x for x in reader][self.start_index:]

  def start(self):
    trades = self.load_trades()
    self.load_browser()
    try:
      self.login()
      self.navigate_to_stocks()
      self.navigate_to_add_sales_entry()
      for i, t in enumerate(trades):
        print i + self.start_index
        self.add_trade(t)
        sleep(1)
        self.click_common_button('yes')
        sleep(1)
    except Exception as e:
      raise e

  def add_trade(self, t):
    e = self.br.find_element_by_xpath('//*[@id="radio_0e:0"]')
    e.click()

    self.click_common_button('continue')

    e = self.br.find_element_by_xpath('//*[@id="edt_00"]')
    e.send_keys('LTC - cryptocurrency')

    e = self.br.find_element_by_xpath('//*[@id="edt_01"]')
    v = str(round(float(t['net_proceeds']), 2))
    e.send_keys(v)

    e = self.br.find_element_by_xpath('//*[@id="edt_02"]')
    v = parser.parse(t['sell_datetime']).strftime('%m%d%Y')
    e.send_keys(v)

    self.click_common_button('continue')

    # "Purchase" option is already selected
    self.click_common_button('continue')

    e = self.br.find_element_by_xpath('//*[@id="edt_00"]')
    v = str(round(float(t['cost_basis']), 2))
    e.send_keys(v)

    e = self.br.find_element_by_xpath('//*[@id="edt_01"]')
    v = parser.parse(t['purchase_datetime']).strftime('%m%d%Y')
    e.send_keys(v)

    self.click_common_button('continue')

    # summary page. move to next one
    self.click_common_button('continue')

  def click_common_button(self, key):
    xpaths = {
        'yes': '//*[@id="Yes_00"]',
        'no': '//*[@id="No_00"]',
        'continue': '//*[@id="Continue_00"]'}

    p = xpaths[key]
    e = self.br.find_element_by_xpath(p)
    e.click()
    sleep(1)

  def login(self):
    el = self.br.find_element_by_id('ius-userid')
    el.send_keys(self.credentials['username'])
    el = self.br.find_element_by_id('ius-password')
    el.send_keys(self.credentials['password'])
    el.submit()
    # sleep(7)

  def navigate_to_stocks(self):
    # "Take me to my return" link
    l = self.br.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/div[2]/div[1]/div[1]/div[3]/a')
    l.click()
    sleep(4)

    # Federal on sidebar
    l = self.br.find_element_by_xpath('/html/body/div[2]/div/div[3]/section/div/div[1]/div/div[2]/div[2]/div/section/div/div[4]/a')
    l.click()
    sleep(1)

    # stock options button
    l = self.br.find_element_by_id('MyStuff-OverviewGroup-Item-STOCKSALES-4-EditAction')
    l.click()
    sleep(2)

  def navigate_to_add_sales_entry(self):
    e = self.br.find_element_by_xpath('//*[@id="mc_00_ADD"]')
    e.click()
    sleep(1)

    self.click_common_button('no')
    sleep(1)

def main():
  t = TaxHelper('cred.ignore.json', 'ltc_sells.csv', start_index=154)
  t.start()

if __name__ == '__main__':
  main()
