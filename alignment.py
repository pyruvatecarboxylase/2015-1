# -*- coding: cp949 -*-

from sequences import sequences
from operator import itemgetter

sequence1 = raw_input("input your sequence1:")
sequence2 = raw_input("input your sequence2:")
add_del_constant=float(raw_input("Enter addition and deletion constant:"))
substitution_constant=float(raw_input("Enter subtitution constant:"))

#���� sequence�� �빮�ڷ�.
sequence1=sequence1.upper()
sequence2=sequence2.upper()

sequenceset = sequences(sequence1,sequence2,substitution_constant,add_del_constant)

sequenceset.setsequence1(sequence1)
sequenceset.setsequence2(sequence2)
sequenceset.setsubstitution_constant(substitution_constant)
sequenceset.setadd_del_constant(add_del_constant)

s1 = sequenceset.getsequence1()
s2 =  sequenceset.getsequence2()
substitution_constant = sequenceset.getsubstitution_constant()
add_del_constant =  sequenceset.getadd_del_constant()



# �� ��ǥ�� distance�� ������ distance table �����
distance_table = []
def distance(a, b):
    if a == 0.0 and b == 0.0:
        return 0.0
    elif a != 0.0 and b == 0.0:
        return a * add_del_constant
    elif a == 0.0 and b != 0.0:
        return b * add_del_constant
    elif s1[a] == s2[b]:
        return float(min(distance_table[a-1][b-1],distance_table[a-1][b]+add_del_constant,distance_table[a][b-1]+add_del_constant))
    else:
        return float(min(distance_table[a-1][b-1]+substitution_constant,distance_table[a-1][b]+add_del_constant,distance_table[a][b-1]+add_del_constant))

for a in range(len(s1)):
    distance_table.append([])
    for b in range(len(s2)):
        distance_table[a].append(round(float((distance(a, b))),4))


#�� distance�� ���� �� �� direction���� ������ direction table �����
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
            if distance(a,b) == distance_table[a][b-1]+add_del_constant:
                direction.append('right')
            if distance(a,b) == distance_table[a-1][b]+add_del_constant:
                direction.append('down')
        else:
            if distance(a,b)== distance_table[a-1][b-1]+substitution_constant:
                direction.append('cross')
            if distance(a,b)== distance_table[a][b-1]+add_del_constant:
                direction.append('right')
            if distance(a,b)== distance_table[a-1][b]+add_del_constant:
               direction.append('down')
        return direction

for a in range(len(s1)):
    direction_table.append([])
    for b in range(len(s2)):
        direction_table[a].append(direction(a, b))
edit_distance=distance_table[len(s1)-1][len(s2)-1]

#ù ��ǥ���� ������ ��ǥ�� ���� direction���� ������ path ���ϴ� �Լ� �����
#�������� path�� ����� ��ǥ�� branch�� ã��
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
    
#��� ������ path���� list �����
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


#�� path�� �̿��� align�ϱ� 
align_count = 0
align_list=[]
for path in path_list:
    align_1 = []
    align_2 = []
    n = 0
    k = 0
    p=1
    align_count=align_count+1
    for letter in path:
        if letter == '-':
            align_1.append('-')
            n = n+1
            align_2.append('-')
            k = k+1
        elif letter == 'cross':
            align_1.append(s1[n])
            n = n+1
            align_2.append(s2[k])
            k = k+1
        elif letter == 'right':
            align_1.append('-')
            align_2.append(s2[k])
            k = k+1
        elif letter == 'down':
            align_1.append(s1[n])
            n = n+1
            align_2.append('-')
    align_list.append([align_count,"".join(align_1),"".join(align_2)])
# ���� ��� ����
for align in align_list:
    for letter in align:
        print letter

print 'edit distance : ', edit_distance
"""
def segment_count(a,b):
   """ 
"""

#1�� base���̷εΰ� ������ deletion�Ǵ� ��쿡 �г�Ƽ
    if '-A-' in two[1:]:
        score= score+add_del_constant
    if '-T-' in two[1:]:
        score= score+add_del_constant
    if '-G-' in two[1:]:
        score= score+add_del_constant
    if '-C-' in two[1:]:
        score= score+add_del_constant

    whole_align.append(score)
    whole_align.append(one[1:])
    whole_align.append(two[1:])
    alignment[p]=whole_align
    p=p+1

print alignment
#���� ���� score ã��
scores=[]
for i in range(1,p):
    scores.append(alignment[i][0])
lowest_score=min(scores)

#score�� ������ �ش� align�� ����
for i in range(1,p):
    if alignment[i][0] != lowest_score:
        del alignment[i]




for a in alignment:
    print ''
    print 'align', ':', a
    print alignment[a][1]
    print alignment[a][2]
    print 'score: ',alignment[a][0]
"""
