class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dfs = [-1] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dfs[coin] = 1
                
        for i in range(len(dfs)):
            for coin in coins:
                if (i - coin > 0):
                    if dfs[i] == -1 and dfs[i - coin] != -1:
                        dfs[i] = dfs[i - coin] + 1
                    elif dfs[i] != -1 and dfs[i - coin] != -1:
                        dfs[i] = min(dfs[i - coin] + 1, dfs[i])
        return dfs[amount]