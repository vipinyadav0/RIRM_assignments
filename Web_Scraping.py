import requests
from bs4 import BeautifulSoup

URL = "https://ful.io"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
soup.prettify() #prettifying the soup data


''' 
upon inspecting html of given website, we see social links are in a div 
with class name "-mx-1"  uniquely
'''
link_data = soup.find("div", class_="-mx-1") 

print("Social links :- ")
for links in link_data.find_all('a', href=True): # finding all the <a> tags
    print(links['href'])


lst = [] # creating an list that contains <div> with class "lg:w-1/4" 
contacts = soup.find_all("div", class_="lg:w-1/4") #since contacts does not have separate div class
for contact in contacts:
    lst.append(contact)

last_element = lst[-1] # accessing and storing the last element in list which has email and contact details
print("  ")
print("Email/s :-")
email = last_element.find('a', href=True)
email_data = email['href']
print(email_data[7:])



print("  ")
print("Contact :-")
y = last_element.find('p')
print(y.text)



