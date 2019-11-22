# /usr/bin/python3

import os, time, selenium, pandas as pd, numpy as np, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pandas import ExcelWriter
from pandas import ExcelFile

b36d375bf6afe60d39a76745f781ab88 = None
o41fbb39d7dc93ad07d8126d0d17139c3 = Options()
u2879959685cbf0727819759e44c6e715 = e6603da1acdd6f636053fd30d4a653e3 = e230450c7869f12283a9a784a6023a68 = cb6462b1997e6e59ae9c0c40c41963c6 = c9bc48c8a0b0e1d60ae7b113617c864c7 = d656c603994e747a4a39010356a737bb = ""

def w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, text):
    p5a7486c909fd18f4cd49d169b75e2d53 = False
    for i in range(1,20):
        if (b36d375bf6afe60d39a76745f781ab88.page_source.find(text) != -1):
            p5a7486c909fd18f4cd49d169b75e2d53 = True
            break
        else:
            time.sleep(1)
    if not p5a7486c909fd18f4cd49d169b75e2d53:
        print("Error. Timeout.")
    return b36d375bf6afe60d39a76745f781ab88

def a75b59e37ddaead95524079cb557a273(d656c603994e747a4a39010356a737bb, e6603da1acdd6f636053fd30d4a653e3, e230450c7869f12283a9a784a6023a68, cb6462b1997e6e59ae9c0c40c41963c6, c9bc48c8a0b0e1d60ae7b113617c864c7):
	p7c36de502f4aa5d7a5fb2292243a2aa9 = os.getcwd()
	p1dd8f006837f1230e42dc6e79e27215c = p7c36de502f4aa5d7a5fb2292243a2aa9+'/'+d656c603994e747a4a39010356a737bb
	a2571565ecf98e6d43f0536c7240880e = pd.read_excel (r''+p1dd8f006837f1230e42dc6e79e27215c+'')
	df = pd.DataFrame(a2571565ecf98e6d43f0536c7240880e)

	df['Hostname'] = np.where(df['Hostname'].isnull(), df['IP'], df['Hostname'])

	e6603da1acdd6f636053fd30d4a653e3 = df['Hostname']
	e230450c7869f12283a9a784a6023a68 = df['Description']
	cb6462b1997e6e59ae9c0c40c41963c6 = df['IP']
	c9bc48c8a0b0e1d60ae7b113617c864c7 = df['Credential']

	for i in range(len(df)):
		print(e6603da1acdd6f636053fd30d4a653e3[i])
		print(e230450c7869f12283a9a784a6023a68[i])
		print(cb6462b1997e6e59ae9c0c40c41963c6[i])
		print(c9bc48c8a0b0e1d60ae7b113617c864c7[i])
		print()

	n1e1b20a4a7cfc16bc374338a263aec2d(b36d375bf6afe60d39a76745f781ab88, e6603da1acdd6f636053fd30d4a653e3, e230450c7869f12283a9a784a6023a68, cb6462b1997e6e59ae9c0c40c41963c6, c9bc48c8a0b0e1d60ae7b113617c864c7)
	return 0

def n1e1b20a4a7cfc16bc374338a263aec2d(b36d375bf6afe60d39a76745f781ab88, e6603da1acdd6f636053fd30d4a653e3, e230450c7869f12283a9a784a6023a68, cb6462b1997e6e59ae9c0c40c41963c6, c9bc48c8a0b0e1d60ae7b113617c864c7):
	u57f4679269eb6506b6109bc966cd7157 = input("Enter your nessus username:\n$ ")
	f366af137ab9cba47cf204ef452c82ef = input("Enter your nessus password:\n$ ")
	b36d375bf6afe60d39a76745f781ab88.get(u2879959685cbf0727819759e44c6e715)
	b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Sign In')
	b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/div/form/div[1]/input").send_keys(u57f4679269eb6506b6109bc966cd7157)
	b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/div/form/div[2]/input").send_keys(f366af137ab9cba47cf204ef452c82ef)
	b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/div/form/button").click()
	b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'My Scans')

	for i in range(len(e6603da1acdd6f636053fd30d4a653e3)):
		print("\n##############  New Scanning  ##############\n")
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[1]/a[1]").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Advanced Scan')
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/div[1]/div[2]/div[2]/a[2]").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Targets')
		print("host session : "+e6603da1acdd6f636053fd30d4a653e3[i])
		print("desc session : "+e230450c7869f12283a9a784a6023a68[i])
		print("ip session : "+cb6462b1997e6e59ae9c0c40c41963c6[i])
		print("passwd session : "+c9bc48c8a0b0e1d60ae7b113617c864c7[i])
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[1]/div/input").send_keys(e6603da1acdd6f636053fd30d4a653e3[i])
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[2]/div/textarea").send_keys(e230450c7869f12283a9a784a6023a68[i])
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[5]/div/textarea").send_keys(cb6462b1997e6e59ae9c0c40c41963c6[i])
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[2]/span").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Destination ports')
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[4]/div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/div/div[3]/div[1]/div/input").clear()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[4]/div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/div/div[3]/div[1]/div/input").send_keys("all")
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[2]/ul/li[2]").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'unscanned')
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[5]/div[1]/div[1]/div[2]/div/input").clear()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[5]/div[1]/div[1]/div[2]/div/input").send_keys("all")
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[2]/ul/li[3]").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Probe')
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[6]/div[1]/div[1]/div[2]/div[6]/div[1]/div/span/span[1]/span").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[6]/div[1]/div[1]/div[2]/div[6]/div[1]/div/span/span[1]/span").send_keys(Keys.DOWN, Keys.RETURN)
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[4]/span").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Override')
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(13) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/aside/ul/li[5]/span").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'safe checks')
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-view:nth-child(14) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-settings-section:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-settings-section:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.editor-settings-section:nth-child(8) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1)").click()
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[2]/a[2]").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'SNMPv3')
		c103ee3639b6b08cfaa7b9afb18e4457d = e230450c7869f12283a9a784a6023a68[i]
		d654a25a65caa5674e1c2a23ff24b939 = ""
		dc = "dc"
		l1 = 'l1'
		t71d9de156a31eb8c06bb3bbf54d831d4 = ""
		s87ed9fbf4288a3bebf159694b4b1ea5e = ""
		f7a903a4359a35e02420a093fc769913 = ""
		if 'Windows' in e230450c7869f12283a9a784a6023a68[i]:
			print("Windows")
			time.sleep(1)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div/div[2]/ul[3]/li[3]/div/span[2]").click()
			b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Authentication method')
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[6]/div[1]/div/input").send_keys("sysadmin")
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[6]/div[2]/div/input").send_keys(c9bc48c8a0b0e1d60ae7b113617c864c7[i])
			time.sleep(1)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.component-inputs:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").click()
			b36d375bf6afe60d39a76745f781ab88.find_element_by_css_selector("div.component-inputs:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)").click()
			t71d9de156a31eb8c06bb3bbf54d831d4 = "windows"
			y = re.findall(r'20\d+', c103ee3639b6b08cfaa7b9afb18e4457d)
			y476c00d2d8eacc5114658627e0bfe3bb = ''.join(y)
			e772d6a76b4710dcdf676392d3074a17 = re.findall(r'\d+', c103ee3639b6b08cfaa7b9afb18e4457d)
			e772d6a76b4710dcdf676392d3074a17 = ''.join(e772d6a76b4710dcdf676392d3074a17)
			if 'server' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
				if '2003' in y476c00d2d8eacc5114658627e0bfe3bb:
					d654a25a65caa5674e1c2a23ff24b939 = ""
				else:
					d654a25a65caa5674e1c2a23ff24b939 = " server"
			else:
				print("Not windows server")
			
			if any(t71d9de156a31eb8c06bb3bbf54d831d4 in c103ee3639b6b08cfaa7b9afb18e4457d.lower() for t71d9de156a31eb8c06bb3bbf54d831d4 in ('dc', 'domain controller')):
				print("Got DC Keyword")
				if '2008' in y476c00d2d8eacc5114658627e0bfe3bb:
					dc = " domain controller "
					l1 = "level 1"
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[68]"
				if '2003' in y476c00d2d8eacc5114658627e0bfe3bb:
					l1 = ""
					dc = " dc "
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[121]"
				if '2012' in y476c00d2d8eacc5114658627e0bfe3bb:
					if 'r2' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
						f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[134]"
						dc = " r2 dc "
					else:
						f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[130]"
						dc = " dc "
				if '2016' in y476c00d2d8eacc5114658627e0bfe3bb:
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[76]/div"
					dc = " dc "
			else:
				print("It is not DC")
				if '2003' in y476c00d2d8eacc5114658627e0bfe3bb:
					l1 = ""
					dc = " ms "
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[122]"
				if '7' in e772d6a76b4710dcdf676392d3074a17:
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[126]"
					y476c00d2d8eacc5114658627e0bfe3bb = e772d6a76b4710dcdf676392d3074a17
					dc = " workstation "
					l1 = "level 1"
				if '8' in e772d6a76b4710dcdf676392d3074a17:
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[129]"
					y476c00d2d8eacc5114658627e0bfe3bb = e772d6a76b4710dcdf676392d3074a17
					dc = ""
					l1 = ""
				if '2016' in y476c00d2d8eacc5114658627e0bfe3bb:
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[77]"
					dc = " ms "
				else:
					if '2012' in y476c00d2d8eacc5114658627e0bfe3bb:
						if 'r2' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
							f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[136]"
							dc = " ms "
						else:
							f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[36]/li[132]"
							dc = " ms "
			s87ed9fbf4288a3bebf159694b4b1ea5e = t71d9de156a31eb8c06bb3bbf54d831d4+d654a25a65caa5674e1c2a23ff24b939+" "+y476c00d2d8eacc5114658627e0bfe3bb+dc+l1
			print("syntax is : "+s87ed9fbf4288a3bebf159694b4b1ea5e)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[2]/a[3]").click()
			b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Add compliance')
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[1]/div[2]/div[1]/input").send_keys(s87ed9fbf4288a3bebf159694b4b1ea5e)
			time.sleep(2)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath(f7a903a4359a35e02420a093fc769913).click()
			time.sleep(1)

		else:
			print("Linux")
			time.sleep(1)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div/div[2]/ul[3]/li[2]/div").click()
			b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Authentication method')
			time.sleep(1)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath('//*[@id="active-credentials"]/li[2]/div[2]/div/div[1]/span/span[1]/span').click()
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath('//*[@id="active-credentials"]/li[2]/div[2]/div/div[1]/span/span[1]/span').send_keys(Keys.UP, Keys.RETURN)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[1]/div/input").send_keys("root")
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[2]/div/input").send_keys(c9bc48c8a0b0e1d60ae7b113617c864c7[i])
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath('//*[@id="active-credentials"]/li[2]/div[2]/div/div[5]/div[3]/div[1]/span/span[1]/span').click()
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath('//*[@id="active-credentials"]/li[2]/div[2]/div/div[5]/div[3]/div[1]/span/span[1]/span').send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.RETURN)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[3]/div[10]/div[1]/div/input").send_keys("root")
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[3]/div[10]/div[2]/div/input").send_keys(c9bc48c8a0b0e1d60ae7b113617c864c7[i])
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[5]/div[4]/div/input").send_keys(c9bc48c8a0b0e1d60ae7b113617c864c7[i])
			if 'red hat' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
				t71d9de156a31eb8c06bb3bbf54d831d4 = "red hat"
				v = re.findall(r'([6|7])', c103ee3639b6b08cfaa7b9afb18e4457d)
				v7b429202f49c6f41db35b044af2b11f4 = ''.join(v)
				f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[140]"
				if '7' in v7b429202f49c6f41db35b044af2b11f4:
					v7b429202f49c6f41db35b044af2b11f4 = "el"+v7b429202f49c6f41db35b044af2b11f4
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[144]"
				s87ed9fbf4288a3bebf159694b4b1ea5e = t71d9de156a31eb8c06bb3bbf54d831d4+" "+v7b429202f49c6f41db35b044af2b11f4+" server "+l1
				print("syntax is : "+s87ed9fbf4288a3bebf159694b4b1ea5e)
			if 'centos' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
				t71d9de156a31eb8c06bb3bbf54d831d4 = "centos"
				v = re.findall(r'([6|7])', c103ee3639b6b08cfaa7b9afb18e4457d)
				v7b429202f49c6f41db35b044af2b11f4 = ''.join(v)
				f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[38]"
				if '7' in v7b429202f49c6f41db35b044af2b11f4:
					v7b429202f49c6f41db35b044af2b11f4 = "el "+v7b429202f49c6f41db35b044af2b11f4
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[42]"
				s87ed9fbf4288a3bebf159694b4b1ea5e = t71d9de156a31eb8c06bb3bbf54d831d4+" "+v7b429202f49c6f41db35b044af2b11f4+" server "+l1
				print("syntax is : "+s87ed9fbf4288a3bebf159694b4b1ea5e)
			if 'ubuntu' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
				t71d9de156a31eb8c06bb3bbf54d831d4 = "ubuntu"
				v = re.findall(r'\d.+', c103ee3639b6b08cfaa7b9afb18e4457d)
				v7b429202f49c6f41db35b044af2b11f4 = ''.join(v)
				if '12.04' in v7b429202f49c6f41db35b044af2b11f4:
					v7b429202f49c6f41db35b044af2b11f4 = v7b429202f49c6f41db35b044af2b11f4+" lts benchmark "+l1
					f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[168]"
				else:
					if '14.04' in v7b429202f49c6f41db35b044af2b11f4:
						f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[170]"
					if '16.04' in v7b429202f49c6f41db35b044af2b11f4:
						f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[174]"
					if '18.04' in v7b429202f49c6f41db35b044af2b11f4:
						f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[178]"
					v7b429202f49c6f41db35b044af2b11f4 = "linux "+v7b429202f49c6f41db35b044af2b11f4+" lts server "+l1
				s87ed9fbf4288a3bebf159694b4b1ea5e = t71d9de156a31eb8c06bb3bbf54d831d4+" "+v7b429202f49c6f41db35b044af2b11f4
				print("syntax is : "+s87ed9fbf4288a3bebf159694b4b1ea5e)
			if 'hp-ux' in c103ee3639b6b08cfaa7b9afb18e4457d.lower():
				t71d9de156a31eb8c06bb3bbf54d831d4 = "hp-ux"
				s87ed9fbf4288a3bebf159694b4b1ea5e = t71d9de156a31eb8c06bb3bbf54d831d4
				f7a903a4359a35e02420a093fc769913 = "/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/ul[32]/li[82]/div"
				print("syntax is : "+s87ed9fbf4288a3bebf159694b4b1ea5e)
			
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[2]/a[3]").click()
			b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Add compliance')
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div/section/div[1]/div[1]/div/div[1]/div[2]/div[1]/input").send_keys(s87ed9fbf4288a3bebf159694b4b1ea5e)
			time.sleep(2)
			b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath(f7a903a4359a35e02420a093fc769913).click()
			time.sleep(1)
		b36d375bf6afe60d39a76745f781ab88.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[2]/span").click()
		b36d375bf6afe60d39a76745f781ab88 = w9d6b042ae634aa8159a9793988c6a7f7(b36d375bf6afe60d39a76745f781ab88, 'Schedule')
		time.sleep(4)
	return 0

if __name__ == "__main__":
	print("   _____       _ __                                   ")
	print("  / ___/____ _(_) /_____ _____ ___  ____ _____  ____ _")
	print("  \__ \/ __ `/ / __/ __ `/ __ `__ \/ __ `/ __ \/ __ `/")
	print(" ___/ / /_/ / / /_/ /_/ / / / / / / /_/ / / / / /_/ / ")
	print("/____/\__,_/_/\__/\__,_/_/ /_/ /_/\__,_/_/ /_/\__, /  ")
	print("                                             /____/   \n\n")

	print("Welcome to autoscan_nessus script by Saitamang\n")
	u = input("Kindly enter your Nessus IP ie:192.168.1.1\n$ ")
	u2879959685cbf0727819759e44c6e715 = "https://"+u+":8834"
	print("\nURL entered is : "+u2879959685cbf0727819759e44c6e715+"\n")
	d656c603994e747a4a39010356a737bb = input("Enter fullname of the excel filename :\n$ ")
	if ".xlsx" in d656c603994e747a4a39010356a737bb:
		print("File name is :"+ d656c603994e747a4a39010356a737bb)
	else:
		d656c603994e747a4a39010356a737bb = d656c603994e747a4a39010356a737bb+".xlsx"
		print("File name is :"+ d656c603994e747a4a39010356a737bb)
	e334d4bfdbe5614e4edd3f3111e80454 = int(input("\nWhat is your os:-\n1. Linux\n2. Windows\n\nKey in your number your number and press ENTER\n$ "))
	c030503c947bceca6be59816319a41cd2 = input("\nGive the full path of Google Chrome Driver and press ENTER\neg:\nLinux: /usr/bin/chromedriver\nWindows: D:\Desktop\chromedriver.exe\n\n$ ")
	if  e334d4bfdbe5614e4edd3f3111e80454 == 1:
		b36d375bf6afe60d39a76745f781ab88 = webdriver.Chrome(executable_path=c030503c947bceca6be59816319a41cd2, options=o41fbb39d7dc93ad07d8126d0d17139c3)
		b36d375bf6afe60d39a76745f781ab88.maximize_window()
		a75b59e37ddaead95524079cb557a273(d656c603994e747a4a39010356a737bb, e6603da1acdd6f636053fd30d4a653e3, e230450c7869f12283a9a784a6023a68, cb6462b1997e6e59ae9c0c40c41963c6, c9bc48c8a0b0e1d60ae7b113617c864c7)
		print("\n##############  Done Scanning Setup  ##############\n")
	elif e334d4bfdbe5614e4edd3f3111e80454 == 2:
		b36d375bf6afe60d39a76745f781ab88 = webdriver.Chrome(executable_path=c030503c947bceca6be59816319a41cd2, options=o41fbb39d7dc93ad07d8126d0d17139c3)
		b36d375bf6afe60d39a76745f781ab88.maximize_window()
		a75b59e37ddaead95524079cb557a273(d656c603994e747a4a39010356a737bb, e6603da1acdd6f636053fd30d4a653e3, e230450c7869f12283a9a784a6023a68, cb6462b1997e6e59ae9c0c40c41963c6, c9bc48c8a0b0e1d60ae7b113617c864c7)
		print("\n##############  Done Scanning Setup  ##############\n")
		print("##############  Check out my github : https://github.com/saitamang  ##############\n")
	else:
		print("Operating System don't exist")
