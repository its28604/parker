from parker_general import *
from get_coordinate import *

def getParkInfo(link):
    # URL of the page to scrape
    url = base_url + link

    # Fetch the page
    response = requests.get(url)

    # Parse the HTML content
    tree = html.fromstring(response.content)
    
    lab = {}
    try:
        # Extracting <a> elements with class 'park'
        lab["labParkName"] = tree.xpath('//th[@id="labParkName"]/text()')[0]
        lab["labTel"] = tree.xpath('//td[@id="labTel"]/text()')[0].replace('聯絡電話：', '')
        labAdd = lab["labAdd"] = tree.xpath('//td[@id="labAdd"]/text()')[0].replace('地址：', '')
        labCoor = GoogleMapHelper.getCoordinate(labAdd)
        lab["labAdd"] = labAdd
        lab["labCoor"] = labCoor
        lab["labHours"] = tree.xpath('//td[@id="labHours"]/text()')[0].replace('營業時間：', '')
        lab["labTotal"] = tree.xpath('//td[@id="labTotal"]/text()')[0]
        lab["labSpace"] = tree.xpath('//td[@id="labSpace"]/text()')[0]
        lab["labCharge"] = tree.xpath('//td[@id="labCharge"]/text()')[0].replace('收費方式：', '')
    except:
        print(f"Error occure within parsing: {linkZ}")
    return lab




if __name__ == "__main__":
    import json
    import time

    file_path = "all_parks_link.txt"
    out_file_path = "all_parks_info.json"
    labs = {}
    with open(out_file_path, 'r') as file:
        labs = json.load(file)
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                id = line.split("&sn=")[1]
                id = id.replace("\n", "")
                if id not in labs:
                    url = f"aspx/park/{line.strip()}"
                    lab = getParkInfo(url)
                    lab["labURL"] = url
                    print(lab)
                    labs[id] = lab
                    count += 1
                    print(count)
                    if count == 3:
                        break
                    time.sleep(5)
            except Exception as e:
                print(e)
                break
    
    with open(out_file_path, 'w') as out_file:
        out_file.write(json.dumps(labs, ensure_ascii=False))

    
