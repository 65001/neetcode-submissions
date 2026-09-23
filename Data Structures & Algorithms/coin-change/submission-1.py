class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Let T(i, amount)  represent the minimum amount of change:
        # Can use the coin[i] more than once!

        # Base Case
        # T(i, 0) = 0
        # T(0, i) = float('inf')

        inf = float('inf')
        n = len(coins)

        # Case We chose to use coin[i]
        # T(i, amount ) = 1 + T(i, amount - coins[i]) where 0 <= i <= n and amount - coins[i] >= 0
        # Case We chose not to use coin[i]
        # T(i, amount) = T(i - 1, amount)
        # Recurrence
        # T(i, amount) = min( 1 + T(i, amount - coins[i]) , T(i - 1, amount))

        # Initalize the array!
        t = [[inf] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            t[i][0] = 0
        
        # compute the array
        for i in range(n + 1):
            coin = coins[i - 1]
            for j in range(amount + 1):
                if j >= coin:
                    t[i][j] = min( 1 + t[i][j - coin], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]

        
        result = t[n][amount]
        return result if result != inf else -1
        