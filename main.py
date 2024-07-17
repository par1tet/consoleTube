import innertube
# import json

client = innertube.InnerTube("WEB")

query = input('Enter query for search: ')
data = client.search(query=query)

# with open('test.json', 'w') as file:
#     json.dump(data,file,indent=4,ensure_ascii=True)
    
for i in data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]:

    if (list(i.keys())[0]) == 'shelfRenderer' or (list(i.keys())[0]) == 'reelShelfRenderer' or (list(i.keys())[0]) == 'lockupViewModel':
        continue
    print(list(i.keys())[0])
    # print(f"{i[list(i.keys())[0]]['shortBylineText']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']}")
    print(f"https://www.youtube.com{i[list(i.keys())[0]]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']}")
    print('---------------------')
