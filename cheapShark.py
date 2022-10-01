import requests

def getDeals():
    PARANS = {'storeID':1, 'sortBy':'Metacritic', 'desc': 0, 'upperPrice':10, 'onSale':1, 'output':'100'} #More complicated query
    res = requests.get('https://www.cheapshark.com/api/1.0/deals?', params=PARANS).json()
    #print(str(res))
    # with open("Output.txt", "w") as text_file:
    #     text_file.write(str(res))
    return res[0]

def main():
    PARANS = {'storeID':1} #Query Parameters
    res = requests.get('https://www.cheapshark.com/api/1.0/deals?', params=PARANS).json() #get and convert to jSON

    #print(res[0].keys())# Keys we have access to.

    for i in range(len(res)):# For loop to print out the data we want.
        print(res[i]['title']+"---Normal Price: "+res[i]['normalPrice']+">>>Sale Price: "+res[i]['salePrice'])
    
    print("===================================================================================")

    PARANS = {'storeID':1, 'sortBy':'Metacritic', 'desc': 0, 'upperPrice':10, 'onSale':1, 'output':'100'} #More complicated query
    res = requests.get('https://www.cheapshark.com/api/1.0/deals?', params=PARANS)#.json()

    print(res.url)

    res = res.json()

    for i in range(len(res)):
        print(res[i]['title']+"---Normal Price: "+res[i]['normalPrice']+">>>Sale Price: "+res[i]['salePrice']+" LINK: https://store.steampowered.com/app/"+str(res[i]['steamAppID']))


if __name__ == "__main__":
    main()
    #getDeals()
