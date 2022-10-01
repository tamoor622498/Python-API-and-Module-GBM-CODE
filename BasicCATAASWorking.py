import requests

def getCatWithText(text=" "):#space for "empty"
    if (text == ""):
        text = " ";
    response = requests.get("https://cataas.com/cat/says"+"/"+text) #Get webpage with text
    file = open("images\image.png", "wb") #Open in write binary mode
    file.write(response.content)
    #print(response.content)
    file.close() #File write finished

if __name__ == "__main__":
    getCatWithText()