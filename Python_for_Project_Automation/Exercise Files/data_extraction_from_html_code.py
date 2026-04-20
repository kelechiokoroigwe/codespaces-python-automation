# import all necessary libraries
import requests 
from bs4 import BeautifulSoup 

# define url of webpage to scrape from
url = "https://kibworthbooks.com/collections/childrens-age-9?page=3"

# send a request to get html code from the url and save the response 
response = requests.get(url, headers={"Accept": "text/html"}) 

# use BeautifulSoup to parse the text from the response 
parsed_response = BeautifulSoup(response.text, "html.parser") 

# find all book titles 
# uncomment the following line of code and FILL IN
titles = parsed_response.find_all("div", class_="product-card__name")

# iterate over the titles and print the text for each
# write your code below
for title in titles:
    print(title.text)

