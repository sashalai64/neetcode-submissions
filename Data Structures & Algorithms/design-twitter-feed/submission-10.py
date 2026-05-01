class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)


    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append([-self.time, tweetId])
        

    def getNewsFeed(self, userId):
        maxHeap = []
        recent_tweets = []

        if self.tweets[userId]:
            for tweet in self.tweets[userId][-10:]:
                heapq.heappush(maxHeap, tweet)
        
        for followerId in self.following[userId]:
            if followerId in self.tweets:
                for tweet in self.tweets[followerId][-10:]:
                    heapq.heappush(maxHeap, tweet)
        
        while maxHeap and len(recent_tweets) < 10:
            recent_tweets.append(heapq.heappop(maxHeap)[1])
        
        return recent_tweets


    def follow(self, followerId, followeeId):
        if followeeId not in self.following[followerId] and followeeId != followerId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        