class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # {userId: (time, tweetId)}
        self.following = defaultdict(set) # {userId: [user1, user2]}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)

        for user in self.following[userId]:
            for time, id in self.tweets[user][-10:]:
                heapq.heappush(heap, (time, id))
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        res = []
        while heap:
            time, id = heapq.heappop(heap)
            res.append(id)
        
        return res[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
