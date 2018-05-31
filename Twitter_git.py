import tweepy
from textblob import TextBlob
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import csv


def clean_tweets(twts):
    stop_words = set(stopwords.words("english"))
    ps = PorterStemmer()
    
##  remove stop words      
    for i in range(len(twts)):
        twts[i][0] = [w for w in twts[i][0] if not w in stop_words]
    print(twts)



## stemmed sentences
    for i in range(len(twts)):
        stemmed = []
        for word in twts[i][0]:
            stemmed.append(ps.stem(word))
        twts[i][0] = stemmed
    

    for i in range(len(twts)):
        twts[i][0]=" ".join(twts[i][0])
        "" .join(twts[i][0].split(','))
    return twts
        
        
    



consumer_key = '**put your own consumer key**'
consumer_secret = '**put your own consumer secret**'

access_token = '**put your own access token'
access_token_secret = '**put your own access token secret **'



topic = input('Enter topic :')

tt = TweetTokenizer()
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(topic)

help(api.search)

tweets_and_their_sentiments = []

for tweet in public_tweets:
    if tweet.lang == 'en':
        blob = TextBlob(tweet.text)
    ##        print(blob.tags)
        tokenized_tweet = tt.tokenize(tweet.text)
        

        tweets_and_their_sentiments += [[tokenized_tweet,
                                        blob.sentiment.polarity]]
##        
##try :
##    print(tweets_and_their_sentiments)
##except:
##    print("Encountered an Error while printing")
##    
##    
cleaned_tweets = clean_tweets(tweets_and_their_sentiments)
print(cleaned_tweets)

with open('data.csv',"w",encoding='utf-8') as file:
    filwr = csv.writer(file,delimiter =','
                       ,quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filwr.writerow(["Cleaned Sentence","Public Perception"])
    filwr.writerows(cleaned_tweets)
print("PROGRAM ENDED")
    
