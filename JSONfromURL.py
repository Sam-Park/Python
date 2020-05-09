import urllib.request, json

with urllib.request.urlopen("https://www.chapelhillopendata.org/api/v2/catalog/datasets/census-diversity") as url:
    data = json.loads(url.read().decode())
    links = data['links']
    for href in links:
        print()
    # print(hrefs)