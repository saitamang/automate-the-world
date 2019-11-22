# Automate-the-world
python script to automate daily task in penetration testing

# nmap_auto_fast.py #
- nmap script that can read all IPs in excel file and automated the scanning
The algorithm is based on scanning all port only at first, then scan the specific ports that had been detected with more nmap's options.

# nessus_config_review.py #
- python3 script to automate the setting for whitebox internal vulnerability assessment during penetration testing process. This script is meant for Nessus advance scan.

<h2> Requirement: </h2>
<h3> 1. Excel Files </h3>
+------------+----------------------------------------------------+----------------+----------------+  <br />
|    Host    |  Description                                       |      IP        |   Credential   |  <br />
+------------+----------------------------------------------------+----------------+----------------+  <br />
| gryffindor |  Windows Server 2016 Standard Edition              |   10.10.3.75   |    q!@#$       |  <br />
+------------+----------------------------------------------------+----------------+----------------+  <br />
| slytherin  |  HP-UX  B.11.31 U ia64                             |   10.10.3.37   |    haah345     |  <br />
+------------+----------------------------------------------------+----------------+----------------+  <br />
| hufflepuff |  Centos 6.9                                        |   10.10.3.91   |    123qwe      |  <br />
+------------+----------------------------------------------------+----------------+----------------+  <br />
| revenclaw  |  Windows Server 2008 R2 Datacenter Edition dC      |   10.10.3.131  |    zxc456      |  <br />
+------------+----------------------------------------------------+----------------+----------------+  <br />

p/s: 
- the test.xlsx are attached as example
- kindly change the column bar name as above

<h3> 2. Python3 modules </h3>
` $ pip3 install -r requirements.txt`

<h3> 3. Google Chrome Driver </h3>
(A) For windows:
- Check your Google Chrome about to get the version
- Download the driver version from url --> https://chromedriver.chromium.org/downloads
- Put your chrome driver in the same folder as nessus_config_review.py file

(B) For Linux:
- locate your chromedriver
p/s : basically in --> /usr/bin/chromedriver

<h2>Dont forget to STAR (★) my repo</h2>

enjoy :)

