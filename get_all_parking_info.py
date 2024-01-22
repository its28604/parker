from parker_general import *

# URL of the page to scrape
url = base_url + 'aspx/park/park.aspx?lang=zh-Hant-TW'

# Fetch the page
response = requests.get(url)

# Parse the HTML content
tree = html.fromstring(response.content)

# Extracting <a> elements with class 'park'
park_elements = tree.xpath('//a[@class="park"]')

# Iterate over each element to extract text and href
for element in park_elements:
    text = element.text_content().strip()  # Get text content of the element
    href = element.get('href')            # Get href attribute of the element
    print(f"Text: {text}, Link: {href}")
