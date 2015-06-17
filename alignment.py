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
s1 = 'AAAAAAAAAAAA'
s2 = 'AAAAATAAAAAA'
s1 = "-"+ s1
s2 = "-"+ s2
'''
deletion_number=raw_input("Enter deletion add:")
right_number = deletion_number
down_number = deletion_number
substitution_number=raw_input("Enter subtitution add:")


# 각 좌표의 distance로 구성된 distance table 만들기
distance_table = []
def distance(a, b):
    if a == 0.0 and b == 0.0:
        return 0.0
    elif a != 0.0 and b == 0.0:
        return a * deletion_number
    elif a == 0.0 and b != 0.0:
        return b * deletion_number
    elif s1[a] == s2[b]:
        return min(distance_table[a-1][b-1],distance_table[a-1][b]+down_number,distance_table[a][b-1]+right_number)
    else:
        return min(distance_table[a-1][b-1]+substitution_number,distance_table[a-1][b]+down_number,distance_table[a][b-1]+right_number)

for a in range(len(s1)):
    distance_table.append([])
    for b in range(len(s2)):
        distance_table[a].append(round(distance(a, b),4))
for a in distance_table:
    print a
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
            if distance(a,b) == distance_table[a][b-1]+right_number:
                direction.append('right')
            if distance(a,b) == distance_table[a-1][b]+down_number:
                direction.append('down')
        else:
            if distance(a,b)== distance_table[a-1][b-1]+substitution_number:
                direction.append('cross')
            if distance(a,b)== distance_table[a][b-1]+right_number:
                direction.append('right')
            if distance(a,b)== distance_table[a-1][b]+down_number:
               direction.append('down')
        return direction
for a in range(len(s1)):
    direction_table.append([])
    for b in range(len(s2)):
        direction_table[a].append(direction(a, b))
for a in direction_table:
    print a
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
    elif direction =='right':
        return finding_path(a, b-1)
    elif direction == 'down':
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
p = 1
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
            score = score+substitution_number
        elif letter == 'cross':
            align_one.append(s1[n])
            n = n+1
            align_two.append(s2[k])
            k = k+1
        elif letter == 'right':
            align_one.append('-')
            align_two.append(s2[k])
            k = k+1
            score = score+deletion_number
        elif letter == 'down':
            align_one.append(s1[n])
            n = n+1
            align_two.append('-')
            score = score+deletion_number
    one = "".join(align_one)
    two = "".join(align_two)
    print 'align', p
    p = p+1
    print one[1:]
    print two[1:]
    print 'score', ':', score
    print ""