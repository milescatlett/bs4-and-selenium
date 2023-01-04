from datetime import datetime

f = open("wmb.txt", "r")
ftb = ''
for line in f:
    ftb = line
splitup = ftb.split("@")
output = []
for i in range(len(splitup) - 1):
    lst = splitup[i].split("#")
    brewery = lst[0]
    food_truck = lst[1]
    start = datetime.strptime(lst[2], '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(lst[3], '%Y-%m-%d %H:%M:%S')
    eid = lst[4]
    uid = lst[5]
    t = (brewery, food_truck, start, end, eid, uid)
    output.append(t)
    print(type(t))
print(output)


