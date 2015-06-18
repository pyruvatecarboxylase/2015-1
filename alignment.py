# -*- coding: cp949 -*-

from sequences import sequences
import re
from operator import itemgetter


sequence1 = raw_input("input your sequence1:")
sequence2 = raw_input("input your sequence2:")
deletion_number=float(raw_input("Enter deletion add:"))
substitution_number=float(raw_input("Enter subtitution add:"))

#받은 sequence를 대문자로.
sequence1=sequence1.upper()
sequence2=sequence2.upper()

sequenceset = sequences(sequence1,sequence2,substitution_number,deletion_number)


sequenceset.setsequence1(sequence1)
sequenceset.setsequence2(sequence2)
sequenceset.setsubstitution_number(substitution_number)
sequenceset.setdeletion_number(deletion_number)


s1 = sequenceset.getsequence1()
s2 =  sequenceset.getsequence2()
substitution_number = sequenceset.getsubstitution_number()
deletion_number =  sequenceset.getdeletion_number()




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
        return float(min(distance_table[a-1][b-1],distance_table[a-1][b]+deletion_number,distance_table[a][b-1]+deletion_number))
    else:
        return float(min(distance_table[a-1][b-1]+substitution_number,distance_table[a-1][b]+deletion_number,distance_table[a][b-1]+deletion_number))

for a in range(len(s1)):
    distance_table.append([])
    for b in range(len(s2)):
        distance_table[a].append(round(float((distance(a, b))),4))

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
            if distance(a,b) == distance_table[a][b-1]+deletion_number:
                direction.append('right')
            if distance(a,b) == distance_table[a-1][b]+deletion_number:
                direction.append('down')
        else:
            if distance(a,b)== distance_table[a-1][b-1]+substitution_number:
                direction.append('dif_cross')
            if distance(a,b)== distance_table[a][b-1]+deletion_number:
                direction.append('right')
            if distance(a,b)== distance_table[a-1][b]+deletion_number:
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
    if direction == 'dif_cross':
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
alignment={}
for path in path_list:
    whole_align=[]
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
        elif letter == 'cross':
            align_one.append(s1[n])
            n = n+1
            align_two.append(s2[k])
            k = k+1
        elif letter == 'dif_cross':
            align_one.append(s1[n])
            n = n+1
            align_two.append(s2[k])
            k = k+1
        elif letter == 'right':
            align_one.append('-')
            align_two.append(s2[k])
            k = k+1
        elif letter == 'down':
            align_one.append(s1[n])
            n = n+1
            align_two.append('-')
    one = "".join(align_one)
    two = "".join(align_two)
    score=distance_table[len(s1)-1][len(s2)-1]


#1개 base사이로두고 띄엄띄엄 deletion되는 경우에 패널티
    if '-A-' in two[1:]:
        score= score+deletion_number
    if '-T-' in two[1:]:
        score= score+deletion_number
    if '-G-' in two[1:]:
        score= score+deletion_number
    if '-C-' in two[1:]:
        score= score+deletion_number

    whole_align.append(score)
    whole_align.append(one[1:])
    whole_align.append(two[1:])
    alignment[p]=whole_align
    p=p+1

print alignment
#가장 높은 score 찾기
scores=[]
for i in range(1,p):
    scores.append(alignment[i][0])
lowest_score=min(scores)

#score가 낮으면 해당 align을 삭제
for i in range(1,p):
    if alignment[i][0] != lowest_score:
        del alignment[i]




for a in alignment:
    print ''
    print 'align', ':', a
    print alignment[a][1]
    print alignment[a][2]
    print 'score: ',alignment[a][0]