# Lets Automate It!
python script to automate daily task in penetration testing

## nmap_auto_fast.py ##
- nmap script that can read all IPs in excel file and automated the scanning
The algorithm is based on scanning all port only at first, then scan the specific ports that had been detected with more nmap's options.

## nessus_vulnerability_assessment_automator.py ##
- python3 script to automate the setting for whitebox internal vulnerability assessment during penetration testing process. This script is meant for Nessus advance scan. The code had been obfuscate, contact me if you want the unobfuscated code. ^,^

<h2> Requirement: </h2>
<h3> 1. Excel Files </h3>

<img src="https://github.com/saitamang/saitamang.github.io/blob/master/assets/images/excel_nessus.PNG" alt="" data-canonical-src="https://github.com/saitamang/saitamang.github.io/blob/master/assets/images/excel_nessus.PNG" width="1000" height="300" />

p/s: 
- the test.xlsx are attached as example
- kindly change the column bar name as above if you have your own file, dont worry if you have many columns

<h3> 2. Python3 modules </h3>

`pip3 install -r requirements.txt`

<h3> 3. Google Chrome Driver </h3>
(A) For windows:

- Check your Google Chrome about to get the version

- Download the driver version from url https://chromedriver.chromium.org/downloads

- Put your chrome driver in the same folder as nessus_config_review.py file

(B) For Linux:
- locate your chromedriver that is basically in --> /usr/bin/chromedriver

<h3>Make Sure:</h3>
- Check your terminal always as it may ask some credential and some others
- Don't make the browser small size

<h2>Dont forget to STAR (★) my repo</h2>

enjoy :)

There will be version 2.0 coming soon :)

