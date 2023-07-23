# beyonnex
Required Software Packages:
1. Selenium, Python 3.11, bs4 (BeautifulSoup), xlsxwriter and Docker.

   
**Steps to execute without Docker:**
1. Place the given files some where on the PC and it using any editor like PyCharm.
2. Run the main.py
3. The script gets executed and test report Beyonnex_Weather_shopper.xlsx is generated.

   
**Alternatively execute it from the command line (without Docker):**
1. Go to the location where the files are copied from the terminal and execute python3 main.py

   
**Steps to execute with Docker**
1. From Pycharm or from the terminal execute the below to build the docker:
 **docker build -t dockertest .**
2. To run the docker execute the below:
 **docker run dockertest**

   
**Note:**
The current latest version of the chrome browser that is getting installed version 115. There is no correctly working chrome driver I could find for the version 115. Hence I used 114 version driver, which gives the following error:
Error getting version of chromedriver 115. Retrying with chromedriver 114 (attempt 1/5)
Incompatible release of chromedriver (version 114.0.5735.16) detected in PATH: /chromedriver/chromedriver
Hence the docker could not run.
