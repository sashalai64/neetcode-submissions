class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # {userId: [(time1, tweetId1), (time2, tweetId2)]}
        self.following = defaultdict(set) # {userId: [userId1, userId2,...]}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)

        for user in self.following[userId]:
            for time, t in self.tweets[user][-10:]:
                heapq.heappush(heap, (time, t))
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        while heap:
            time, t = heapq.heappop(heap)
            res.append(t)

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
