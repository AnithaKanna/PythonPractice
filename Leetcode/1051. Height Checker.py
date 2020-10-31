  def heightChecker(self, heights: List[int]) -> int:
        heights1 = heights.copy()
        heights1.sort()
        diff = [ a-b  for a, b in zip(heights, heights1)]
        count = diff.count(0)
        return (len(heights)-count)
