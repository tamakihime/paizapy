first = input()
first = first.split()
yoko = int(first[0])
tate = int(first[1])
kaisuu = int(first[2])
second = input()
second = second.split()
x = int(second[0])
y = int(second[1])
for i in range(kaisuu):
    yomikomi = input()
    yomikomi = yomikomi.split()
    opretor = yomikomi[0]
    if opretor == "D":
        y = y-int(yomikomi[1])
        if y < 0:
            y = y+tate
    if opretor == "U":
        y = y+int(yomikomi[1])
        if y > (tate-1):
            y = y-tate
    if opretor == "R":
        x = x+int(yomikomi[1])
        if x > (yoko-1):
            x = x-yoko
    if opretor == "L":
        x = x-int(yomikomi[1])
        if x < 0:
            x = yoko+x
print(x,y)
print('\n')




