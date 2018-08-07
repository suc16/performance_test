#!/usr/bin/python3
# -*- coding=utf-8 -*-
#
# __author__ = SuChen
#

import json
import time
from selenium import webdriver
from pyvirtualdisplay import Display

# Get date as timestamp
print("Begin at %s \n" % time.ctime())

# Attention: start Xvfb
display = Display(visible=0, size=(800, 600))
display.start()
# Get local session of firefox
browser = webdriver.Firefox() 

url_in_queue = "http://www.taobao.com"
print("  url : %s" % url_in_queue)

# Load page （wait 3 seconds to finish the GET request）
browser.get(url_in_queue) 
time.sleep( 3 )

p_timing = browser.execute_script("return window.performance.timing")
#p_getEntries = browser.execute_script("return window.performance.getEntries()") 

#onload
pageloadtime = p_timing["loadEventStart"] - p_timing["navigationStart"]  
#dns
dns = p_timing["domainLookupEnd"] - p_timing["domainLookupStart"]  
#tcp
tcp = p_timing["connectEnd"] - p_timing["connectStart"]  
#ttfb
ttfb = p_timing["responseStart"] - p_timing["navigationStart"]

# Print result
print("\nEnd at %s \n" % time.ctime())
print("selenium result:")
print("onload    %10.2f ms"%(pageloadtime))
print("dns       %10.2f ms"%(dns))
print("tcp       %10.2f ms"%(tcp))
print("ttfb      %10.2f ms"%(ttfb))  

browser.quit()
display.stop()
