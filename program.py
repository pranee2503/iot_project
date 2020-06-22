import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "w84p65"
deviceType = "rasp"
deviceId = "6666"
authMethod = "token"
authToken = "66666666"
def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
deviceCli.connect()
while True:
        temp=random.randint(90, 110)
        pulse =random.randint(30, 120)
        #Send Temperature & Pulse rate to IBM Watson
        data = { 'Temperature' : temp, 'Pulse': pulse }
        #notification alerts-----------------------------------------------------------
        if(temp>100 and (pulse>90 or pulse<50)):
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"M8gTI2kYVsEiFKZRwnx47BpHyzCGub0q16ahlvAQPXtS9Wm3UfWFy2jhoEXGBksI40v9rZiUQmNafe5P","sender_id":"FSTSMS","message":"Temperature and Pulse are abnormal","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)       
        elif temp>100:
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"M8gTI2kYVsEiFKZRwnx47BpHyzCGub0q16ahlvAQPXtS9Wm3UfWFy2jhoEXGBksI40v9rZiUQmNafe5P","sender_id":"FSTSMS","message":"Temperature is HIGH","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)         
        elif pulse>90:
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"M8gTI2kYVsEiFKZRwnx47BpHyzCGub0q16ahlvAQPXtS9Wm3UfWFy2jhoEXGBksI40v9rZiUQmNafe5P","sender_id":"FSTSMS","message":"Pulse is HIGH","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)       
        elif pulse<50:
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"M8gTI2kYVsEiFKZRwnx47BpHyzCGub0q16ahlvAQPXtS9Wm3UfWFy2jhoEXGBksI40v9rZiUQmNafe5P","sender_id":"FSTSMS","message":"Pulse is LOW","language":"english","route":"p","numbers":"7993778964"}
                headers = {
                        'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)       
        #------------------------------------------------------------------------------
        def myOnPublishCallback():
            print ("Temperature = %s F" % temp, "and Pulse Rate = %s bpm" % pulse)
        success = deviceCli.publishEvent("Health", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        deviceCli.commandCallback = myCommandCallback
deviceCli.disconnect()








