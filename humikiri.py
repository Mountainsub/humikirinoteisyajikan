# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def hms(t):
    h = (t // 60) // 60 
    m = (t // 60) % 60
    s = t % 60
    return h, m, s
def jikoku(h, m, s):
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0" +str(m)
    else:
        m = str(m)
    if s < 10:
        s = "0" + str(s)
    else:
        s =  str(s)
    return h +":" + m + ":" + s
def zerosyori(t):
    dammy = list(t)
    dammy = list(map(int, dammy))
    return dammy[0] * 10 + dammy[1]
line = input()
a, b, c, d, e = map(int, line.split())
index = int(input())
close = []
direct = []
opened =[]
switch = 0
switch1 = []
start = []
starttime =[]
end = []
endtime = []
for i in range(index):
    line = input().split()
    direct.append(int(line[0]))
    start.append(line[1])
    end.append(line[2])
def switch(di, t_1, t_2):
    if di == 0:
        h, m = t_1.split(":")
        h = zerosyori(h)
        m = zerosyori(m)
        map(int, (h, m))
        total_m = (60 * h + m) * 60
        total_m -= a
        h, m, s = hms(total_m)
        close.append(total_m)
        s_time = jikoku(h, m, s)
        starttime.append(s_time)
        H, M = t_2.split(":")
        H = zerosyori(H)
        M = zerosyori(M)
        total_m = (60 * H + M) * 60
        total_m += b
        h, m, s = hms(total_m)
        e_time = jikoku(h, m, s)
        opened.append(total_m)
        endtime.append(e_time)
        return s_time + " - " + e_time 
    else:
        h, m = t_1.split(":")
        h = zerosyori(h)
        m = zerosyori(m)
        map(int, (h, m))
        total_m = (60 * h + m) * 60
        total_m -= c
        h, m, s = hms(total_m)
        s_time = jikoku(h, m, s)
        starttime.append(s_time)
        close.append(total_m)
        h, m = t_1.split(":")
        h = zerosyori(h)
        m = zerosyori(m)
        total_m = (60 * h + m) * 60
        total_m += d
        opened.append(total_m)
        h, m, s = hms(total_m)
        e_time = jikoku(h, m, s)
        h, m = t_2.split(":")
        h = zerosyori(h)
        m = zerosyori(m)
        total_m = (60 * h + m) * 60
        endtime.append(e_time)
        return s_time + " - " + e_time
def interval(t_1, t_2):
    if t_2 - t_1 <= e:
        return True
lists = []
for i in range(index):
    lists.append(switch(direct[i], start[i], end[i]))
c_close = sorted(close)
c_opened = sorted(opened)
for i in range(index - 1):
    k = 1
    while  c_close[i + k]  <= c_opened[i] :
        switch1.append(i + k)
        if i + k >= index - 1:
            break
        k += 1
count = 0
starttime = sorted(starttime)
endtime = sorted(endtime)
if switch1 != []:
    for i, i_v in enumerate(switch1):
        x = switch1[i]
        h, m, s = hms(c_opened[x])
        lists[x-i-1] = starttime[x-i-1] + " - " + endtime[x] 
        lists.pop(x-i)
for i, i_v in enumerate(lists):
    if i == len(lists) - 1:
        break
    if interval(c_opened[i], c_close[i+1]):
        lists[i] = starttime[i] + " - " + endtime[i +1] 
        lists.pop(i + 1)
for i in range(len(lists)):
    print(lists[i])
