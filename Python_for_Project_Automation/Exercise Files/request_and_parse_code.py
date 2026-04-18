# import relevant libraries
import requests
from bs4 import BeautifulSoup

# define the url
# FILL IN before running the code
url = "https://kibworthbooks.com/?srsltid=AfmBOor9vdN2zXbwmTmPvuJqSyZ0eU_-E3fi3ItU0sJp1nm4VYuK4rWK"

# send a request to get html code from that url
# uncomment the following line and replace with your code
response = requests.get(url, headers={"Accept": "text/html"})

# parse the response
# uncomment the following line and replace with your code
parsed_response = BeautifulSoup(response.text, "html.parser")

# format the parsed HTML response in a way that’s easier to read and print it out
# uncomment the following line before running the code
print(parsed_response.prettify())