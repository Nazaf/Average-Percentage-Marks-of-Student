n = input("")
grade = []
for entry in range(int(n)):
    grade.append([i for i in raw_input().split()])
query = input()
queryOut = [x[1:] for x in grade if x[0] == query]
total = 0
scores = 0
for x in queryOut:
    for y in x:
        total += float(y)
        scores += 1
print("%.2f" % (float(total/scores)))
