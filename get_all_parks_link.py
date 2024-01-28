from parker_general import *

def GetAllParksLink():
    # URL of the page to scrape
    url = base_url + 'aspx/park/park.aspx?lang=zh-Hant-TW'

    # Fetch the page
    response = requests.get(url)

    # Parse the HTML content
    tree = html.fromstring(response.content)

    # Extracting <a> elements with class 'park'
    district_elements = tree.xpath('//a[@class="park"]')

    all_parks_link = []

    # Iterate over each element to extract text and href
    for element in district_elements:
        href = element.get('href')            # Get href attribute of the element
        url = base_url + href
        response = requests.get(url)
        tree = html.fromstring(response.content)
        park_elements = tree.xpath('//a[@class="park"]')
        for _element in park_elements:
            _href = _element.get('href')
            all_parks_link.append(_href)

    # Open a file in write mode
    with open('all_parks_link.txt', 'w') as file:
        for link in all_parks_link:
            file.write(link + '\n')  # Write each link to the file, followed by a newline



if __name__ == "__main__":
    GetAllParksLink()