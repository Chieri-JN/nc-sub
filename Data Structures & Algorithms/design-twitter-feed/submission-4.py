"""
init 
timeCounter -> int of time
userId -> heap of their feed (we get the top 10 based off time)
    - tuple of (time, tweetId, poster userID)
    - 
userID -> set Of their followers
userID -> set of who they follow
# userID -> set 

getNewsFeed; 
    keep popping from feed until we get ten 
        -> if use no longer follows the person dont add back to feed

unfollow:
    -> remove from set of who they follow
    -> remove from set of their followers 

"""
from heapq import *
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.feeds = {}
        self.followers = {}
        self.following = {}
        self.time = 0
        self.posts = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        followers = self.followers.get(userId, set())
        post = (-self.time, tweetId, userId)
        for f in followers:
            feed = self.feeds.get(f, [])
            heappush(feed, post)
            self.feeds[f] = feed

        ownFeed = self.feeds.get(userId, [])
        self.feeds[userId] = ownFeed
        self.posts[userId].add(post)
        heappush(ownFeed, post)
        

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(f"self.feeds; {self.feeds}")
        topTen = []
        feed = self.feeds.get(userId, [])
        follows = self.following.get(userId, set())
        putBack = []
        seen = set()

        while feed and len(topTen) < 10:
            time, tweetId, posterID = heappop(feed)
            if posterID in follows or posterID == userId:
                if tweetId not in seen:
                    topTen.append(tweetId)
                putBack.append((time, tweetId, posterID))
                seen.add(tweetId)
            
        for p in putBack:
            heappush(feed, p)

        return topTen


    def follow(self, followerId: int, followeeId: int) -> None:
        # user1 follows user2
        user1, user2 = followerId, followeeId
        user2Posts = self.posts.get(user2, set())
        user1Feed = self.feeds.get(user1, [])
        self.feeds[user1] = user1Feed

        user1Follows = self.following.get(user1, set())
        user2Followers = self.followers.get(user2, set())

        user2Followers.add(user1)
        self.followers[user2] = user2Followers
        
        user1Follows.add(user2)
        self.following[user1] = user1Follows

        for post in user2Posts:
            heappush(user1Feed, post)

        

        # print(f"self.following: {self.following}")
        # print(f"self.followers: {self.followers}")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user1, user2 = followerId, followeeId

        user1Follows = self.following.get(user1, set())
        user2Followers = self.followers.get(user2, set())


        if user1 in user2Followers:
            user2Followers.remove(user1)
        if user2 in user1Follows:
            user1Follows.remove(user2)


