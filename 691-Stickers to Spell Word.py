class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        targetCount = collections.Counter(target)
        n = len(target)
        ##join each sticker to target
        stickerCount = [collections.Counter(sticker) & targetCount for sticker in stickers]
        
        ##remove those stickers within other larger sticker
        for i in range(len(stickerCount) - 1, -1, -1):
            if any(stickerCount[i] == stickerCount[i] & stickerCount[j] for j in range(len(stickerCount)) if i != j):
                stickerCount.pop(i)
        ##convert sticker back to string
        stickerList = ["".join(sticker.elements()) for sticker in stickerCount]
        
        length = 1 << n
        dp = [float('inf')]*length
        dp[0] = 0
        for pos in range(length):
            if dp[pos] == float('inf'): continue
            for sticker in stickerList:
                next_pos = pos
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (next_pos >> i) & 1: continue ##if ith pos is already filled
                        if c == letter:
                            next_pos |= 1 << i ##fill ith position, change to corresponding index
                            break
                dp[next_pos] = min(dp[next_pos], dp[pos] + 1)
                
        return dp[-1] if dp[-1] != float('inf') else -1