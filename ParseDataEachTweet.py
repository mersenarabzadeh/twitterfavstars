import tweepy
import pandas as pd

# twitter credentials
client = tweepy.Client(*****, wait_on_rate_limit=True)

# Get a tweet information
def crawl(tweetid, csvnumber):
      all_tweets = []
      # Take and parse information
      for page in tweepy.Paginator(client.get_liking_users, tweetid, user_fields=['created_at'], max_results=100, limit=11):
           for User in page.data:
             parsed_user = {}
             parsed_user['id'] = User.id
             parsed_user['username'] = User.username
             parsed_user['date'] = User.created_at
             all_tweets.append(parsed_user)

      #Save information to a CSV
      df = pd.DataFrame(all_tweets)
      print(df.head())
      filename = 'first' + str(csvnumber) + '.csv'
      df.to_csv(filename)


# Read the list of tweets
list = pd.read_csv('badlist.csv')

# Send a tweet with filenumber to function
i = 0
for id in list['id']:
  crawl(id, i)
  i = i + 1
