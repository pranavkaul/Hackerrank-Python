'''https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen'''

n = int(input())

nums = map(int, input().split())
print(sorted(list(set(nums)))[-2])





