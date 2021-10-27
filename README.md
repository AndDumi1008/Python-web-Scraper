|| App name: Sharpp
|| Author: Andrei Dumitrescu
|| Curent Version: 1.0
|| Code Language: Python 3
|| Platform: Windows

DO THIS BEFORE RUNNING: 
	Open cmd and install requirements.txt with the following command line: 
	If You are in project location in cmd :	python -m pip install -r requirements.txt
	Else :				python -m pip install -r "<path>\requirements.txt"

Goal: Run Script and export/Append price of the product to the table so you can monitor price over time.
Resources: Using Request and BS4 modules to create the script
Language: English
Prog. Language: Python 3

About the code: It should be easy to configure and run. Could increase run time if there will be
				an multiple site scraper in only one run. Output should be easy to read if configured correctly.
				
				Require low knowledge of html/CSS, python 3 and pip installed on run envirement
				
				First run the 'requirement.txt' with command prompt, enter the following command: pip install -r <path/to/requirement.txt>
				Then you can run as it is or check config file.
				
				For other site scrap add look at how config file is wrote. For remove you can delete or change on CHECK column from 1 to 
				other value
				or vice-versa, where 1 means it will run and scrap the site or 0 to not scrap scrap the site.
				
				Program stop if there is an error. Please provide feedback!
				If you did something wrong the output will be most probably some text that was randomly scraped from site.
				
Beta: 	There will be the base of the code. Not so many functions for user. Just a simple program that will scrap and output price and
		description of a product from big eShop in Romania (ex.: eMag, cel, domo)