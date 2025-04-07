from typing import List
from collections import Counter
class Solution:
    def preProcess(self, stickers:List[str], target:str) -> List[str]:
        #preprocess the stickers with 2 intuitions
        #1. remove letter that is not in target to reduce search iterations
        #2. remove sticker which is a subset of another sticker
        reducedStickers = []
        for sticker in stickers:
            reducedStickers.append(self.filter_word(sticker, target))
        preProcessedStickers = reducedStickers
        for i in range(len(reducedStickers)):
            for j in range(len(reducedStickers)):
                if i != j and self.isSubsetWord(reducedStickers[i], reducedStickers[j]):
                    preProcessedStickers.remove(reducedStickers[i])
        return preProcessedStickers

    def filter_word(self, word:str, target:str) -> str:
        # Keep only the letters in 'word' that are also in 'target'
        return ''.join([letter for letter in word if letter in target])

    def isSubsetWord(self, subsetWord, supersetWord) -> bool:
        subsetCount = Counter(subsetWord)
        supersetCount = Counter(supersetWord)
        for (letter, count) in subsetCount.items():
            if subsetCount[letter] > supersetCount.get(letter, 0):
                return False
        return True

    def minStickers(self, stickers: List[str], target: str) -> int:
    def helper(self, stickers: List[str], target: str, idx: int, memo: dict) -> int:
        if target == '':
            return 0

        if idx == len(stickers):
            return len(target) + 1

        if memo.get

solution = Solution()
stickers = ["with","example","science"]
target = "thehat"
print(solution.preProcess(stickers, target))