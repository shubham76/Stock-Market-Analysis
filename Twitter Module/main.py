import sys
import re
from textblob import TextBlob
from datetime import timedelta, date

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():


	def clean_tweet(tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
	def get_tweet_sentiment(tweet):
        # create TextBlob object of passed tweet text
		analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def daterange(start_date, end_date):
	    for n in range(int ((end_date - start_date).days)):
	        yield start_date + timedelta(n)

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)
		print("Date: %s\n" % t.date)

	# Example 2 - Get tweets by query search
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Donald Trump').setSince("2015-01-01").setUntil("2017-01-01").setMaxTweets(10)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	dir_path = "example.csv"
	csv = open(dir_path, "w") 

	columnTitleRow = "Query, Date, Positive, Negative, Neutral\n"
	csv.write(columnTitleRow)

	# for i in range(4,5):
	# 	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
	# 	print get_tweet_sentiment(tweet.text)
	# 	row = str(re.sub(",","",tweet.text.encode('utf-8'))) + "," + str(tweet.date).split(" ")[0] + "\n"
	# 	csv.write(row)
	query = "USA"

	start_date = date(2015, 01, 01)
	end_date = date(2015, 1, 3)
	for single_date in daterange(start_date, end_date):
		date1 = single_date.strftime("%Y-%m-%d") 
		print single_date.strftime("%Y-%m-%d")
		print single_date + timedelta(1)
		tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(str(single_date)).setUntil(str(single_date+timedelta(1))).setMaxTweets(100)
		tweets = got.manager.TweetManager.getTweets(tweetCriteria)
		print len(tweets)
		ptweets = 0
		negtweets = 0
		neutweets = 0
		for tweet in tweets:
	 		senti = get_tweet_sentiment(tweet.text)
	 		
	 		if(senti == 'positive'):
	 			ptweets += 1
	 		elif senti == 'negative':
	 			negtweets += 1
	 		else:
	 			neutweets += 1

		positive_percentage = float(ptweets)/float(len(tweets))
		negative_percentage = float(negtweets)/float(len(tweets))		 			
	 	neutral_percentage = float(neutweets)/float(len(tweets))	
		
		print positive_percentage
		print negative_percentage
		print neutral_percentage
		
		row = query + "," + str(single_date) + "," + str(positive_percentage) + "," + str(negative_percentage) + "," + str(neutral_percentage) + "\n"
		csv.write(row)

	#printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)

if __name__ == '__main__':
	main()
