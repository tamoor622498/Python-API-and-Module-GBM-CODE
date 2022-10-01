import tweepy
import json
import authReal
import BasicCATAASWorking

api = authReal.authFunc() #Twitter account

timeline = api.mentions_timeline() #Gets all of the mentions in your timeline

for tweet in timeline:#Runs through all the of the tweets
    if((tweet.favorited == False) & ("cat" in (tweet.text).lower())): #only gets unliked tweets  and have the word cat
        text = tweet.text.lower()#Turns everything to lowercase
        text = text.replace('@umbcieee', '',1)#Removes name
        text = text.replace('cat', '',1)#Removes cat
        text = text.replace(':', '',1)#Removes :
        BasicCATAASWorking.getCatWithText('@'+tweet.user.screen_name+' :'+text)#Downloads image with text
        media_list = []#array of tweet stuff
        response = api.media_upload("images\image.png")#adds image
        media_list.append(response.media_id_string)#Text
        api.update_status('@'+tweet.user.screen_name+' Your Cat picture:', media_ids=media_list)#Tweets out image and text
        tweet.favorite()#Likes tweet
        print('@'+tweet.user.screen_name+' :'+text)#Prints the text

