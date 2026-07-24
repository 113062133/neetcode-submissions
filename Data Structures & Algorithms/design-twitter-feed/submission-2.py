from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        users = self.followMap[userId].copy()
        users.add(userId)
        
        heap = []
        for user in users:
            if user in self.tweetMap and self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                count, tweetId = self.tweetMap[user][index]
                heapq.heappush(heap, (-count, tweetId, user, index))

        while heap and len(res) < 10:
            neg_count, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)

            prev_index = index - 1
            if prev_index >= 0:
                prev_count, prev_tweetId = self.tweetMap[user][prev_index]
                heapq.heappush(heap, (-prev_count, prev_tweetId, user, prev_index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
