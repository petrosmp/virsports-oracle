"""
Imports and driver settings are done inside the functions to allow for usage in other scripts etc (only need to import the needed function, not *)
"""


def get_scores_per_month(given_month):
    """
    Circles the calendar for given month (or for current month if input is 0).
    """
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
    from time import sleep
    from datetime import date
    from detect import scrape_days_scores

    today_month = int(str(date.today())[5:7])
    if given_month > today_month:                                       #check if given month is valid
        if given_month > 12:
            if given_month == 69:
                print("Nice!")
                exit()
            else:
                print("Months go up to 12, dumbass")
                exit()           
        print("This month (the " + str(given_month) + "th of current year) has not yet come to pass")
        exit()

    chromedriver = "C:\chromedriver\chromedriver.exe";                      #path to the chromedriver executable(only needed if using chrome)
    driver = webdriver.Chrome(chromedriver);                                #for Firefox this would just be webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://virtualsports.opap.gr/virtual-results");            #opens a window in the browser with this page

    if given_month:
        today_month = int(str(date.today())[5:7])
        if given_month > today_month:                                       #check if given month is valid
            if given_month > 12:
                if given_month == 69:
                    print("Nice!")
                    exit()
                else:
                    print("Months go up to 12, dumbass")
                    exit()           
            print("This month (the " + str(given_month) + "th of current year) has not yet come to pass")
            exit()
        else:
            calendar = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/img')
            calendar.click()

            #browse to that month
            go_back = today_month - given_month
            if go_back == 0:                                                #if given month is today's month, switch to default case
                given_month =0;
            for i in range(go_back):
                prev_month_button = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[1]/span')
                prev_month_button.click()
            given_month_name = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/span[1]').text
            print("The month you requested was " + given_month_name)
            
            #find all active (clickable) days in the datepicker (calendar)
            month = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody').find_elements_by_tag_name("a") 
            
            #find this month's last day coordinates
            last_day = 31
            if given_month == 2:
                last_day = 28
            if given_month == 4 or given_month == 6 or given_month  ==  9 or given_month == 11:
                last_day = 30;
            print("%s's last day is the %i"%(given_month_name, last_day))
            row, collumn = 1,1
            for day in month:
                print("Parsing day: %s of current calendar"%(day.text))
                if day.text == str(last_day) and row != 1:#change to whatever you want to search (MUST BE STRING!!!)
                    print("Found last day of the month (" + day.text + ") at row %i, collumn %i"%(row,collumn))
                    break
                collumn += 1;
                if collumn == 8:
                    row+=1
                    collumn = 1;
            #circle the calendar 
            print("Starting to circle the calendar")
            for r in range(row,0,-1):
                if r == row:                                                        #when on the row where today is, start from today
                    for c in range(collumn,0,-1):
                        print("New Iteration    row: %i collumn %i [101]"%(r,c))
                        try:
                            if c != collumn:
                                calendar.click()
                                print("clicked calendar [101.555]")
                            else:
                                print("didnt need to click calendar [101.000]")
                            sleep(1)
                            day_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr['+str(r)+']/td['+str(c)+']/a'
                            day = driver.find_element_by_xpath(day_xpath)
                            day_num = day.text
                            day.click()
                            print("clicked day %s [101] (everything that happens from now on will be on this day's page)"%(day_num))
                            day_title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
                            print("this data was taken from the %s of %s: %s  [101]"%(day_num, given_month_name, day_title))
                            scrape_days_scores(driver)
                            if int(day_title[:2]) == 1:
                                break
                        except NoSuchElementException:
                            print("Stopped at " + day.text + "with NoSuchElementException [101]")
                            break
                        except ElementClickInterceptedException:
                            print("Element not clickable at row %s, collumn %s for some reason, usually the page hasn't fully loaded yet [101]"%(r,c))
                            continue
                        sleep(2)
                else:                                                               #when on every other row, start from the end (7th collumn)
                    for c in range(7,0,-1):
                        try:
                            print("New Iteration    row: %i collumn %i [102]"%(r,c))
                            calendar.click()
                            print("clicked calendar [102]")
                            day_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr['+str(r)+']/td['+str(c)+']/a'
                            day = driver.find_element_by_xpath(day_xpath)
                            day_num = day.text
                            day.click()
                            print("clicked day %s [102] (everything that happens from now on will be on this day's page)"%(day_num))
                            day_title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
                            print("this data was taken from the %s of %s: %s  [102]"%(day_num, given_month_name, day_title))
                            scrape_days_scores(driver)
                            if int(day_title[:2]) == 1:
                                break
                        except NoSuchElementException:
                            print("Stopped at " + day.text + "with NoSuchElementException [102]")
                            break
                        except ElementClickInterceptedException:
                            print("Element not clickable at row %s, collumn %s for some reason, usually the page hasn't fully loaded yet [102]"%(r,c))
                            continue
                        sleep(2)
            driver.close()
            exit()
    else:                                                                   #if no month is given 
        print("Current month has been selected.")
        calendar = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/img')
        calendar.click()
        month = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody').find_elements_by_tag_name("a") #finds all active (clickable) days in the datepicker (calendar)
        #find today's coordinates
        row, collumn = 1,1
        for day in month:
            print("Parsing day %s of current month [201]"%(day.text))
            if day.text == str(date.today())[-2:]:                              #change to whatever you want to search (MUST BE STRING!!!)
                print("Found todays date (" + day.text + ") at row %i, collumn %i [201]"%(row,collumn))
                break
            collumn += 1;
            if collumn == 8:
                row+=1
                collumn = 1;
        #circle the calendar 
        print("starting to circle the calendar [201]")
        for r in range(row,0,-1):
            if r == row:                                                        #when on the row where today is, start from today
                for c in range(collumn,0,-1):
                    try:
                        print("New Iteration    row: %i collumn %i [201]"%(r,c))
                        calendar.click()
                        print("calendar clicked [201]")
                        day_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr['+str(r)+']/td['+str(c)+']/a'
                        day = driver.find_element_by_xpath(day_xpath)
                        day_num = day.text
                        day.click()
                        print("clicked day %s [201] (everything that happens from now on will be on this day's page)"%(day_num))
                        day_title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
                        print("this data was taken from the %s of current month: %s  [201]"%(day_num, day_title))
                        scrape_days_scores(driver)
                        if int(day_title[:2]) == 1:
                            break
                    except NoSuchElementException:
                        print("Stopped at " + day.text + "with NoSuchElementException [201]")
                        break
                    except ElementClickInterceptedException:
                        print("Element not clickable at row %s, collumn %s for some reason, usually the page hasn't fully loaded yet [201]"%(r,c))
                        continue
                    sleep(7)
                    """
                    try:
                        print("Printing scores for: " + driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text)
                        scores = driver.find_elements_by_partial_link_text("-")
                        if len(scores) == 0:
                            print("No scores detected [1]")
                            break
                        for score in scores:
                            print(score[i].text)
                    except NoSuchElementException:
                        print("No scores on this page")
                        continue
                    """
            else:                                                               #when on every other row, start from the end (7th collumn)
                for c in range(7,0,-1):
                    try:
                        print("New Iteration    row: %i collumn %i [202]"%(r,c))
                        calendar.click()
                        print("calendar clicked [202]")
                        day_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr['+str(r)+']/td['+str(c)+']/a'
                        day = driver.find_element_by_xpath(day_xpath)
                        day_num = day.text
                        day.click()
                        print("clicked day %s [202] (everything that happens from now on will be on this day's page)"%(day_num))
                        day_title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
                        print("this data was taken from the %s of current month: %s  [202]"%(day_num, day_title))
                        scrape_days_scores(driver)
                        if int(day_title[:2]) == 1:
                            break
                    except NoSuchElementException:
                        print("Stopped at " + day.text + "with NoSuchElementException [202]")
                        break
                    except ElementClickInterceptedException:
                        print("Element not clickable at row %s, collumn %s for some reason, usually the page hasn't fully loaded yet [202]"%(r,c))
                        continue
                    sleep(7)
                    """
                    try:
                        print("Printing scores for: " + driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text)
                        scores = driver.find_element_by_css_selector('#senna_surface1').find_elements_by_partial_link_text("-")
                        if len(scores) == 0:
                            print("No scores detected [1]")
                            break
                        for score in scores:
                            print(score[i].text)
                    except NoSuchElementException:
                        print("No scores on this page")
                        continue
                    """
        driver.close()
        exit()