class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set([id])
        dq = deque([id])
        dist = 0
        videoDict = defaultdict(int)
        while dq:
            k = len(dq)
            for i in range(k):
                current = dq.popleft()
                for nb in friends[current]:
                    if nb not in visited:
                        visited.add(nb)
                        dq.append(nb)
            dist += 1
            if dist == level: break
        
        for friend in dq:
            for vedio in watchedVideos[friend]:
                videoDict[vedio] += 1
        
        res = [(val, key) for key, val in videoDict.items()]
        res.sort()
        return [key for _, key in res]
            