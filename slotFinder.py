from webbot import Browser
import time
import pyautogui
import boto3

    
def available(html):
    res = html.find('Next available')
    return res != -1

if __name__ == '__main__':
    email = ''
    passwd = ''

    web = Browser()
    web.go_to('www.amazon.com')
    web.click('Sign in')
    web.type(email, into='Email')
    web.click(id='continue', tag='input')
    web.type(passwd, into='Password')
    web.press(web.Key.ENTER)
    
    target = 'https://www.amazon.com/gp/cart/view.html?ref_=nav_cart'
    
    web.go_to(target)
    
    id = 'sc-alm-buy-box-ptc-button-VUZHIFdob2xlIEZvb2Rz'
    web.click(id=id, tag='input')
    
    #id = 'a-autoid-0'
    #web.click(id=id,tag='input')
    
    pyautogui.click(1007,257)
    #print(pyautogui.position())

    id ='subsContinueButton'
    web.click(id=id,tag='input')
    time.sleep(15.0)
    html = web.get_page_source()

    findSpot = False
    while not findSpot:
        #if 'No delivery' in html:
        if not available(html):
            print('Not Available yet')
            pyautogui.click(154,77)
            time.sleep(15.0)
            html = web.get_page_source()
        else:
            client = boto3.client('sns')
            msg = "A slot is available, go get it"
            pn = "+1"
            client.publish(PhoneNumber=pn,Message=msg)
            print(msg)
            findSpot = True
