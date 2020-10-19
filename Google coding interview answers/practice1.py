# Solution to 'https://www.youtube.com/watch?v=3Q_oYDQ2whs'

a = int(input("Enter the number of meetings for the first person: "))
d = []
for i in range(a):
    b = input("Enter the start of meeting: ")
    c = input("Enter the end of meeting: ")
    d.append([b,c])
f = input("Enter the daily bound start time: ")
g = input("Enter the daily bound end time: ")
d.append([f,g])

h = int(input("Enter the number of meetings for the second person: "))
e = []
for i in range(h):
    b = input("Enter the start of meeting: ")
    c = input("Enter the end of meeting: ")
    e.append([b,c])
f = input("Enter the daily bound start time: ")
g = input("Enter the daily bound end time: ")
e.append([f,g])

# Make the list of free times
f = []
for i in range(int(a)):
    if i == int(a)-1:
        if d[i+1][0] !=  d[0][0]:
            f.append([d[i+1][0],d[0][0]])
        if d[i+1][1] != d[i][1]:
            f.append([d[i][1],d[i+1][1]])
    else:
        if d[i][1] != d[i+1][0]:
            f.append([d[i][1], d[i+1][0]])

g = []
for i in range(int(h)):
    if i == int(h)-1:
        if e[i+1][0] != e[0][0]:
            g.append([e[i+1][0], e[0][0]])
        if e[i+1][1] != e[i][1]:
            g.append([e[i][1], e[i+1][1]])
    else:
        if e[i][1] != e[i+1][0]:
            g.append([e[i][1], e[i+1][0]])

# Find the suitable lists for comparison
final = []
for i in range(len(g)):
    for j in range(len(f)):
        if g[i][0] >= f[j][1] and g[i][1] <= f[j][0]:
            pass

# Find the overlapping segments of the compared lists
        else:
            if g[i][0] < f[j][1] and g[i][0] > f[j][0] and g[i][1] >= f[j][1]:
                final.append([g[i][0],f[j][1]])
            if g[i][0] < f[j][0] and g[i][1] > f[j][1]:
                final.append([f[j][0],f[j][1]])
            if g[i][1] > f[j][0] and g[i][0] <= f[j][0] and g[i][1] < f[j][1]:
                final.append([f[j][0],g[i][1]])
            if g[i][0] > f[j][0] and g[i][1] < f[j][1]:
                final.append([g[i][0],g[i][1]])

print(final)


