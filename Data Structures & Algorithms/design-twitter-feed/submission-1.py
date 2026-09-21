class Twitter:

    def __init__(self):
        self.feeds: list[tuple[int, int]] = []
        self.follows: dict[int, set] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feeds.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followed = self.follows.get(userId, set())
        n = len(self.feeds)
        while n > 0 and len(res) < 10:
            if self.feeds[n-1][0] in followed or self.feeds[n-1][0] == userId:
                res.append(self.feeds[n-1][1])
            n -= 1
        return res
                

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.follows.get(followerId):
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.follows.get(followerId):
            self.follows.get(followerId).remove(followeeId)
        
