import twint
import time

c = twint.Config()
c.Username = "realslimshady"
c.Store_object = True
c.Limit = 30000

t1 = time.time()
twint.run.Followers(c)

followers = twint.output.tweets_object[1:]

for follower in followers:
    print(follower)