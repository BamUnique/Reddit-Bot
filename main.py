import praw
reddit = praw.Reddit(client_id="xLz4-bF6Daoo6yPFIeLiSA", client_secret="qTNeS2Up8RSTdFcujf3c8a2S7e8Jng",
                     password="rH2ji9jLVF2TGBZ", user_agent="BamYouKnow Bot 0.1",
                     username="BamsRedditBot")

subr = reddit.subreddit('leagueoflegends') # this chooses a subreddit you want to get comments from
for comment in subr.stream.comments(skip_existing=True): # this iterates through the comments from that subreddit as new ones are coming in
  try:
    if "!lol" in comment.body: # "!bot" is the keyword in this case. replace "bot" with your keyword
      comment.reply("I have been summoned. This is a nice place.") # this is what your bot replies to the comment that has the keyword
  except praw.exceptions.APIException: # Reddit may have rate limits, this prevents your bot from dying due to rate limits
    print("probably a rate limit...")