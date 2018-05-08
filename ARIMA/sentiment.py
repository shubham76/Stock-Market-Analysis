import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import time
start=time.time()


# read file
filenames=['normalized.csv']
df = pd.read_csv(filenames[0])

def sentiment_cal(title,intro,body):
	
	sia = SentimentIntensityAnalyzer()
	tscore = sia.polarity_scores(title)
	iscore= sia.polarity_scores(intro)
	bscore= sia.polarity_scores(body)
	tscore = float(tscore['compound'])
	iscore = 0.5*float(iscore['compound'])
	bscore = 0.25*float(bscore['compound'])
	max_pos,max_neg=1.0,-1.0
	score=(tscore+iscore+bscore)
	if score>max_pos:
		score=max_pos
	elif score<max_neg:
		score=max_neg
	return round(score,2)


result = pd.DataFrame()
for i,r in df.iterrows():
	score=sentiment_cal(str(r.title),str(r.intro),str(r.body))
	temp=pd.DataFrame({'date':[r.date],'time':[r.time],'title':[r.title],'intro':[r.intro],'body':[r.body],'score':[score]})
	result = pd.concat([result,temp])
#print(result.head(2))

result.to_csv('labeled_round.csv',encoding='utf-8',sep=',')
print(time.time()-start)
