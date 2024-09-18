import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


dtype = {'name': str, 'phone': str}
contacts_df = pd.read_csv('./data/Students-81_kohinoor.csv', dtype=dtype)
contacts = contacts_df['phone'].tolist()
print('contacts imported\nOpening Whatsapp\n')

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input("Press Enter after scanning the QR code")

# message = "This message is for testing purpose. %0APlease ignore this \nwww.duckduckgo.com"
message = ""

cnt = 1
for contact in contacts:
    try:
        url = f"https://web.whatsapp.com/send?phone={'+91' if contact[:3] != '+91' else ''}{contact}&text={message}"
        driver.get(url)
        # Take some time to load the chat
        sleep(15)

        action = ActionChains(driver)
        action.send_keys(Keys.ENTER)
        action.perform()
        print(f"{cnt}. Message Sent to: {contact}")
        cnt = cnt+1
        sleep(5)
    except:
        print("Error in sending the message to", contact)

print('All done...')

sleep(1000)
driver.quit()



# import pandas as pd
# import pywhatkit as pwk
# from time import sleep

# dtype = {'name': str, 'contact': str}
# contacts_df = pd.read_csv('./numbers.csv', dtype=dtype)

# message = 'Please ignore this message, this is for testing purpose.'

# for number in contacts_df['contact'].tolist():
#     try:
#         pwk.sendwhatmsg_instantly(number, message)
#         print("Message Sent to: ", number)

#         sleep(5)
#     except:
#         print("Error in sending the message to", number)



# cotacts_df = pd.read_csv('./numbers.csv')

# try:
#      # sending message in Whatsapp in India so using Indian dial code (+91)
#      pwk.sendwhatmsg_instantly("+918944808060", "please check the link")
 
#      print("Message Sent!") #Prints success message in console
 
#      # error message
# except: 
#      print("Error in sending the message")