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
    print("Scraping finished after returning " +str(num_scores) + " scores.");


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
