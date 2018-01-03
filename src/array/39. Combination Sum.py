import time
class Solution(object):
  def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res

  def dfs(self, nums, target, index, path, res):
    if target < 0:
      return  # backtracking
    if target == 0:
      res.append(path)
      return
    for i in range(index, len(nums)):
      if nums[i] > target:
        break
      self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


solution = Solution()
time_start = time.time()
print(solution.combinationSum(candidates=[2, 5, 6, 8], target=8))
time_end = time.time()
print(time_end - time_start)
