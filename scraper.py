from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chromedriver = "C:\chromedriver\chromedriver.exe"                       #path to the chromedriver executable(only needed if using chrome)
driver = webdriver.Chrome(chromedriver)                                 #for Firefox would just be webdriver.Firefox()
driver.get("https://virtualsports.opap.gr/virtual-results")             #opens a window in the browser with this page

scores = []     
j=1
while 1:
    xpath = '//*[@id="coupon-table"]/div[2]/div[' +str(j)+ ']/div[6]'   #"create" the XPath of each game's score     
    j = j + 1
    try:
        newScore = driver.find_element_by_xpath(xpath)
        scores.append(newScore)
        #print("Found element at XPath " + xpath)                       #un-comment for debugging if problem appears
    except NoSuchElementException:                                      
        #print("No element at XPath " + xpath)                          #un-comment for debugging if problem appears
        break


num_scores = len(scores)
print("Scraping finished after returning " +str(num_scores) + " scores.")

"""
for i in range(num_scores):                                             #un-comment for debugging if problem appears                               
    print(scores[i].text)
"""