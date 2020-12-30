'''https://www.hackerrank.com/challenges/finding-the-percentage/problem'''

n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    scores = list(map(float, line[1:]))
    student_marks[line[0]] = sum(scores)/float(len((scores)))
query = str(input())
print("%.2f" % student_marks[query])


