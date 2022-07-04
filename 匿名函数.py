# 匿名函数
# 一个参数
# multiply = lambda x : 2*x
# print(multiply(9))

# 两个参数
# cut = lambda x,y : x-y
# print(cut(10,2))


def climbStairs(n):
	if n < 2:
		return n
	# 初始化数据
	dp = [0] * (n+1)
	dp[1],dp[2] = 1,2
	for i in range(3,n+1):
		dp[i] = dp[i-1] + dp[i-2]  # 状态转移方程
	return dp[n]

print(climbStairs(1000))
