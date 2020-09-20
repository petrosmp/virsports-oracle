def scrape_days_scores(driver):
    """
    Beautifully scrapes a day's scores and saves them in a .txt file named accordingly (called when on the day's page)
    """

    from alive_progress import alive_bar
    from time import sleep
    from selenium.common.exceptions import NoSuchElementException

    sleep(2)
    links = driver.find_elements_by_link_text("+22")
    scores_num = len(links)
    i = 0;
    day_title = driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rXASPFw5Drqj"]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]').text
    outfile = open(day_title+".txt","w");
    print("Scraping scores for %s"%(day_title))
    with alive_bar(scores_num) as bar:
        while 1:
            try:
                i += 1
                first_score = driver.find_element_by_css_selector('#coupon-table > div:nth-child(3) > div:nth-child('+str(i)+') > div.col-lg-1.col-sm-4.col-xs-4.d-none.d-lg-flex.vs-no-bg.vs-home-score').text
                outfile.write(first_score + "\n");
                bar()                              #rsalmei's (https://github.com/rsalmei) alive_progress bar is way superior than any I am willing to write so I'm using that one
            except NoSuchElementException:
                break
    print("\rFinished after scraping %i scores"%(i-1))
    outfile.close();