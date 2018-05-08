'''
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores("Reliance Jio's net is so slow that even YouTube suggesting for 144p and still they ask us to join prime ")
print(str(vs))
#print(str(vs["compound"]))

'''
import pandas as pd
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import tokenize
import time
#start=time.time()


# read file
filenames=['TCS_twitter_data.csv']
df = pd.read_csv(filenames[0])

def sentiment_cal(tweet):	
	sia = SentimentIntensityAnalyzer()	
	score= sia.polarity_scores(tweet)
	score = float(score['compound'])	
	return score

result = pd.DataFrame()
for i,r in df.iterrows():
	print r.Time
	score=sentiment_cal(str(r.Tweet))
	temp=pd.DataFrame({'time':[r.Time],'username':[r.Username],'tweet':[r.Tweet],'company':[r.Company],'sentiment':[score],'date':[r.Date]})
	result = pd.concat([result,temp])
	#print(temp)
#print(result.head(2))

result.to_csv('labeled.csv',encoding='utf-8',sep=',')
#print(time.time()-start)





