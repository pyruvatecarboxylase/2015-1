# -*- coding: cp949 -*-

from sequences import sequences


sequence1 = raw_input("input your sequence1:")
sequence2 = raw_input("input your sequence2:")

sequenceset = sequences(sequence1,sequence2)

sequenceset.setsequence1(sequence1)
sequenceset.setsequence2(sequence2)

s1 = sequenceset.getsequence1()
s2 =  sequenceset.getsequence2()

#class없을때  test할 때 쓰는 부분
'''
s1 = 'GCTGATATAGCT'
s2 = 'GGGTGATTAGCT'
s1 = "-"+s1
s2 = "-"+s2
'''


# 각 좌표의 distance로 구성된 distance table 만들기
distance_table = []
def distance(a, b):
    if a == 0 and b == 0:
        return 0
    elif a != 0 and b == 0:
        return a
    elif a == 0:
        return b
    elif s1[a] == s2[b]:
        return min(distance_table[a-1][b-1],distance_table[a-1][b]+1,distance_table[a][b-1]+1)
    else:
        return min(distance_table[a-1][b-1]+1,distance_table[a-1][b]+1,distance_table[a][b-1]+1)
for a in range(len(s1)):
    distance_table.append([])
    for b in range(len(s2)):
        distance_table[a].append(distance(a, b))

#각 distance가 유래 해 온 direction으로 구성된 direction table 만들기
direction_table=[]
def direction(a, b):
    if a == 0 and b == 0:
        return ['-']
    elif a != 0 and b == 0:
        return ['down']
    elif a == 0 :
        return ['right']
    else:
        direction = []
        if s1[a] == s2[b]:
            if distance(a,b) == distance_table[a-1][b-1]:
                direction.append('cross')
            if distance(a,b) == distance_table[a][b-1]+1:
                direction.append('right')
            if distance(a,b) == distance_table[a-1][b]+1:
                direction.append('down')
        else:
            if distance(a,b)== distance_table[a-1][b-1]+1:
                direction.append('cross')
            if distance(a,b)== distance_table[a][b-1]+1:
                direction.append('right')
            if distance(a,b)== distance_table[a-1][b]+1:
               direction.append('down')
        return direction
for a in range(len(s1)):
    direction_table.append([])
    for b in range(len(s2)):
        direction_table[a].append(direction(a, b))

#첫 좌표에서 마지막 좌표로 가는 direction들을 연결한 path 구하는 함수 만들기
def finding_path(a ,b):
    direction = direction_table[a][b][0]
    path.append(direction)
    if len(direction_table[a][b])>1:
        branch_list.append([a, b])
    if direction == '-':
        path.reverse()
        return path
    if direction == 'cross':
        return finding_path(a-1, b-1)
    if direction =='right':
        return finding_path(a, b-1)
    if direction == 'down':
        return finding_path(a-1, b)
    
#모든 가능한 path들의 list 만들기
path_list = []
while 1:
    path=[]
    branch_list = []
    last_branch = []
    finding_path(len(s1)-1, len(s2)-1)
    path_list.append(path)
    if len(branch_list) == 0:
        break
    branch_list.reverse()
    last_branch = branch_list[0]
    del direction_table[last_branch[0]][last_branch[1]][0]


#각 path를 이용해 align하기 + path score 계산하기
p = 0
for path in path_list:
    align_one = []
    align_two = []
    n = 0
    k = 0
    score = 0
    for letter in path:
        if letter == '-':
            align_one.append('-')
            n = n+1
            align_two.append('-')
            k = k+1
            score = score+1
        elif letter == 'cross':
            align_one.append(s1[n])
            n = n+1
            align_two.append(s2[k])
            k = k+1
        elif letter == 'right':
            align_one.append('-')
            align_two.append(s2[k])
            k = k+1
            score = score+1
        elif letter == 'down':
            align_one.append(s1[n])
            n = n+1
            align_two.append('-')
            score = score+1
    one = "".join(align_one)
    two = "".join(align_two)
    print 'align', p
    p = p+1
    print one[1:]
    print two[1:]
    print 'score', ':', score
    print ""