
marksheet =[]
score_ = []
for i in range(int(input())):
    name = input()
    score = float(input())
    marksheet += [[name,score]]
    score_ += [score]
x = sorted(list(set(score_)))[1]

for name_,s in sorted(marksheet):
    if s == x:
        print(name_)
