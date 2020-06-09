from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

driver.maximize_window()

name = input("Enter the name of person or gorup:")

msg = input("Enter the message: ")

count = int(input("Enter the count: "))

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))

user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]")

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()

print("Success")