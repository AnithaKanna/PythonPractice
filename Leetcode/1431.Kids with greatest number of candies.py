class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ouput = []
        for i in range(len(candies)):
            if (candies[i]+extraCandies) >= max(candies):
                ouput.append(True)
            
            else:
                ouput.append(False)
            
        return ouput;
