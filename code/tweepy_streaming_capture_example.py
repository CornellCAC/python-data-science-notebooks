# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 08:59:27 2018

@author: XSEDE	
"""

import re
import datetime
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="your_consumer_key"
consumer_secret="your_consumer_secret"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="your_access_token"
access_token_secret="your_access_token_secret"

# Create variables to use for output file and tweet filter
hashtag = "maga"
date_time_temp = str(datetime.datetime.now())

# Replace all characters except letters and numbers with "_" for filename
current_date_time = re.sub('[^a-zA-Z0-9]','_', date_time_temp)
file_out = open(hashtag + "_" + current_date_time + ".json", 'a')

# Define the Stream Listener
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data) # Print output to console
        file_out.write(data) # Write output to file
        return True

    def on_error(self, status):
        print(status)

# Run the main program and collect tweets with hashtag "nerd"
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['nerd'])
file_out.close()