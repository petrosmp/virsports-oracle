from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def save_scores(filename):
    chromedriver = "C:\chromedriver\chromedriver.exe";                      #path to the chromedriver executable(only needed if using chrome)
    driver = webdriver.Chrome(chromedriver);                                #for Firefox this would just be webdriver.Firefox()
    driver.get("https://virtualsports.opap.gr/virtual-results");            #opens a window in the browser with this page
    scores, o1, o2 = [], [], [];
    j=1;
    while 1:
        xpath = '//*[@id="coupon-table"]/div[2]/div[' +str(j)+ ']/div[6]';  #"create" the XPath of each game's score     
        j = j + 1;
        try:
            newScore = driver.find_element_by_xpath(xpath)
            scores.append(newScore.text);
            o1.append(newScore.text[0]);                                    #array with the numbers of the first team's goals
            o2.append(newScore.text[2]);                                    #array with the numbers of the second team's goals
            #print("Found element at XPath " + xpath)                       #un-comment for debugging if problem appears
        except NoSuchElementException:                                      
            #print("No element at XPath " + xpath)                          #un-comment for debugging if problem appears
            break
    driver.close();                                                         #close browser ater scraping is done
    num_scores = len(scores);
    print("\nScraping finished after returning " +str(num_scores) + " scores.");


    myfile = open(filename,"w");

    for i in range(num_scores):                                             #un-comment for debugging if problem appears                                                
        myfile.write(scores[i]+"\n");
    
    myfile.close();

def read_scores(filename):

    myfile = open(filename,"r");

    mystring = myfile.read();
    

    l,k =0,2;
    array1, array2 = [], [];
    while 1:
        if len(mystring) <= k:
            break;
        try:
            array1.append(int(mystring[l]));
            array2.append(int(mystring[k]));
        except IndexError:
            print("First score probably missing fom site, check to be sure");
            continue;
        l = l + 4;
        k = k + 4;

    myfile.close();
    return [array1,array2];

def scrape_days_scores(driver,):
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