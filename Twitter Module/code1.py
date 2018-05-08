import sys
import re
from textblob import TextBlob
from datetime import timedelta, date
import datetime

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():


	def clean_tweet(tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

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

	dir_path = "TCS_twitter_data.csv"
	csv = open(dir_path, "w") 

	columnTitleRow = "Time,Username,Tweet,Company,Date\n"
	csv.write(columnTitleRow)

	# for i in range(4,5):
	# 	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
	# 	print get_tweet_sentiment(tweet.text)
	# 	row = str(re.sub(",","",tweet.text.encode('utf-8'))) + "," + str(tweet.date).split(" ")[0] + "\n"
	# 	csv.write(row)
	query = '@TCS OR "Tata Consultancy Services" OR "Natarajan Chandrasekaran"'
	company = "TCS"
	start_date = date(2017, 04, 1)
	end_date = date(2017, 05, 3)
	for single_date in daterange(start_date, end_date):
		date1 = single_date.strftime("%Y-%m-%d") 

		tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(str(single_date)).setUntil(str(single_date+timedelta(1))).setMaxTweets(100)
		tweets = got.manager.TweetManager.getTweets(tweetCriteria)
		print len(tweets)
		
		for tweet in tweets:
			date_time = str(tweet.date).split(" ")
			date_ = date_time[0]
			time = date_time[1].split(":")[0] + ":" + date_time[1].split(":")[1]
			date_ = datetime.datetime.strptime(date_, '%Y-%m-%d').strftime('%m/%d/%Y')			
			#print time
			#print date_
			row = time + "," + tweet.username + "," + clean_tweet(tweet.text).encode('utf-8').replace(",","") + "," + company + "," + date_ + "\n"
			csv.write(row)

	#printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)

if __name__ == '__main__':
	main()
