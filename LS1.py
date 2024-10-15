
f = open("D:\PПроекты\sequence.txt", "r")
list1 = [float(x) for x in f]
f.close()

white = "\u001b[47m"
red = "\u001b[41m"
end = "\u001b[0m"

for i in range(0 , 11):
    if i < 5:
        print(f'{white}{"  "*(5-i)}{red}{"  "*(i)}{white}{red}{"  "*(i)}{white}{"  "*(5-i)}{end}')

    elif i == 5:
        continue
    else:
        print(f'{white}{"  "*(i-5)}{red}{"  "*(10-i)}{white}{red}{"  "*(10-i)}{white}{"  "*(i-5)}{end}')
s = "---$"
for i in range(4):
    print(f'{"  "*(3-i)}{white}  {end}{"  "*i}{"  "*i}{white}  {end}{"  "*(3-i)}{"  "*(3-i)}{white}  {end}{"  "*i}{"  "*i}{white}  {end}{"  "*(3-i)}')
for i in range(3, -1, -1):
    print(f'{"  "*(3-i)}{white}  {end}{"  "*i}{"  "*i}{white}  {end}{"  "*(3-i)}{"  "*(3-i)}{white}  {end}{"  "*i}{"  "*i}{white}  {end}{"  "*(3-i)}')

plot = [[0 for i in range(10)] for i in range(10)]

result = [3*i for i in range(10)]
step = abs((result[0]-result[9])/9)


for i in range(10):
    for j in range(10):
        if j == 0:
            plot[i][j] = step*(8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot[i][0] - result[9-j]) < step:
            for m in range(9):
                if 8-m == j:
                    plot[i][m+1] = 1

for i in range(9):
    line = ""
    for j in range(10):
        if j == 0:
            line += "\t" + str(plot[i][j]) + "\t"
        if plot[i][j] == 0:
            line += "--"
        if plot[i][j] == 1:
            line += "##"
    print(line) 
print("\t0\t1 2 3 4 5 6 7 8 9")                   

list1 = [float(x) for x in list1 if x < 0]

res1 = []
res2 = []
for x in list1:
    if -5 < x < 0:
        res1.append(x)
    if x < -5:
        res2.append(x)

proc = int(round(len(res1)/len(list1), 2)*100)
print(f'{"#"*(proc//10)}{"-"*(10-(proc//10))} {proc}% числа большие -5 от всех (отрицательные)')
proc2 = int(round(len(res2)/len(list1), 2)*100)
print(f'{"#"*(proc2//10)}{"-"*(10-(proc2//10))} {proc2}% числа меньшие -5 от всех (отрицательные)')
