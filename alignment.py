s1='GCTGATATAGCT'
s2='GGGTGATTAGCT'
s1="-"+s1
s2="-"+s2

distance_table=[[0]]
path_table=[[['-']]]

for i in range(1,len(s1)):
    distance_table.append([i])
    path_table.append([['down']])

for k in range(1,len(s2)):
    distance_table[0].append(k)
    path_table[0].append(['right'])

def specific_distance(a,b):
    if s1[a]==s2[b]:
        return min(distance_table[a-1][b-1],distance_table[a-1][b]+1,distance_table[a][b-1]+1)
    else:
        return min(distance_table[a-1][b-1]+1,distance_table[a-1][b]+1,distance_table[a][b-1]+1)

    
for a in range(1,len(s1)):
    path_table.append([])
    for b in range(1,len(s2)):
        path_table[a].append([])
        distance_table[a].append(specific_distance(a,b))

        if s1[a]==s2[b]:
            if specific_distance(a,b)==distance_table[a-1][b-1]:
                path_table[a][b].append('cross')
            if specific_distance(a,b)==distance_table[a-1][b]+1:
                path_table[a][b].append('down')
            if specific_distance(a,b)==distance_table[a][b-1]+1:
                path_table[a][b].append('right')
        else:
            if specific_distance(a,b)==distance_table[a-1][b-1]+1:
                path_table[a][b].append('cross')
            if specific_distance(a,b)==distance_table[a-1][b]+1:
                path_table[a][b].append('down')
            if specific_distance(a,b)==distance_table[a][b-1]+1:
                path_table[a][b].append('right')

total_path=[]

def finding_path(a,b):
    if a==0 and b==0:
        total_path.append('-')
    elif 'cross' in path_table[a][b]:
        total_path.append('cross')
        return finding_path(a-1,b-1)
    elif 'right' in path_table[a][b]:
        total_path.append('right')
        return finding_path(a,b-1)
    else:
        total_path.append('down')
        return finding_path(a-1,b)
    
for i in range(len(s1)):
    print s1[i], distance_table[i]
for i in range(len(s1)):
    print path_table[i]
finding_path(12,12)
total_path.reverse()

align_one=[]
align_two=[]
n=0
k=0
for letter in total_path:
    if letter == '-':
        align_one.append('-')
        n=n+1
        align_two.append('-')
        k=k+1
    elif letter=='cross':
        align_one.append(s1[n])
        n=n+1
        align_two.append(s2[k])
        k=k+1
    elif letter=='right':
        align_one.append('-')
        align_two.append(s2[k])
        k=k+1
    elif letter=='down':
        align_one.append(s1[n])
        n=n+1
        align_two.append('-')
        
        

    
print total_path
print align_one
print align_two
