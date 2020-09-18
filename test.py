"""
Imports and driver settings are done inside the functions to allow for usage in other scripts etc (only need to import the needed function, not *)
"""


def get_this_months_scores():
    """
    Circles the calendar for given month (or for current month if no input is detected).
    """
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
    from time import sleep
    from datetime import date

    chromedriver = "C:\chromedriver\chromedriver.exe";                      #path to the chromedriver executable(only needed if using chrome)
    driver = webdriver.Chrome(chromedriver);                                #for Firefox this would just be webdriver.Firefox()
    driver.get("https://virtualsports.opap.gr/virtual-results");            #opens a window in the browser with this page

    days = []

    calendar = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/img')
    calendar.click()
    month = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody').find_elements_by_tag_name("a") #finds all active (clickable) days in the datepicker (clanedar)

    #find today's coordinates
    row, collumn = 1,1
    for day in month:
        if day.text == str(date.today())[-2:]:                              #change to whatever you want to search (MUST BE STRING!!!)
            print("Found todays date (" + day.text + ") at row %i, collumn %i"%(row,collumn))
            break
        collumn += 1;
        if collumn == 8:
            row+=1
            collumn = 1;
    #circle the calendar 
    for r in range(row,0,-1):
        if r == row:                                                        #when on the row where today is, start from today
            for c in range(collumn,0,-1):
                try:
                    calendar.click()
                    day_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr['+str(r)+']/td['+str(c)+']/a'
                    day = driver.find_element_by_xpath(day_xpath)
                    day.click()
                    title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
                    print(title + " row:" +  str(r) + " collumn: " + str(c))
                    if int(title[:2]) <= 1:                                 #terminate process when 1st of the month is reached (needed here because it is possible (though unlikely) that today is the first of the month)
                        break
                except NoSuchElementException:
                    print("Stopped at " + day.text + "with NoSuchElementException")
                    break
                except ElementClickInterceptedException:
                    print("Element not clickable at row %s, collumn %s for some reason, usually the page hasn't fully loaded yet"%(r,c))
                    continue
                sleep(2)
        else:                                                               #when on every other row, start from the end (7th collumn)
            for c in range(7,0,-1):
                try:
                    calendar.click()
                    day_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr['+str(r)+']/td['+str(c)+']/a'
                    day = driver.find_element_by_xpath(day_xpath)
                    day.click()
                    title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
                    print(title + " row:" +  str(r) + " collumn: " + str(c))
                    if int(title[:2]) <= 1:                                 #terminate process when 1st of the month is reached 
                        break
                except NoSuchElementException:
                    print("Stopped at " + day.text + "with NoSuchElementException")
                    break
                except ElementClickInterceptedException:
                    print("Element not clickable at row %s, collumn %s for some reason, usually the page hasn't fully loaded yet"%(r,c))
                    continue
                sleep(2)
    driver.close()