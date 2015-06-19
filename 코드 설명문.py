"""
1. 초기 조건
alignment 파일에서 sequences파일에 있는 class를 import한다.
첫 번째 서열(sequence1), 두 번째 서열(sequence2)을 입력받는다.
addition/deletion이 일어날 때 distance로 더해줄 값(add_del_constant)과
substitution이 일어날 때 더해줄 값(substitution constant:)를 입력받는다.
setter로 입력받을 때 '-'를 추가하여 입력한다.
각 요소들을 getter로 내보내준다.

2. distance table 만들기
2.1 distance table속 좌표값(distance)를 구하는 함수인 distance(a,b) 만들기
2.1.1 a와 b는 distance table의 좌표를 의미한다.(왼쪽 위에서 시작, a는 세로축, b는 가로축)
2.2 각 좌표에서 해당 distance를 값으로 하는 distance_table 구현
2.3 distance table의 마지막 좌표값이 edit distance이다. 

3. direction table 만들기
3.1 해당 좌표의 direction이란 distance_table의 해당 좌표가 그 좌표의 위, 왼쪽, 대각선의 값 중 어느 것을 기준으로 만들어 졌는지 의미한다. 따라서 가능한 direction은 cross, right, down이 있다.
3.2 각 좌표의 direction을 구하는 함수인 direction(a,b)구현
3.3 각 좌표에서 direction을 값으로 하는 direction_table구현
3.3.1 float가 인식된는 과정에서 근사치로 입력되어 소숫점 아래자리가 많이 생기는 문제를 해결하기 위해, round method 를 이용함

4. 하나의 path를 찾기
4.1 path란 (0,0) 부터 마지막 좌표까지 연결되는 direction의 모임을 말한다.
4.2 path를 구하는 함수인 finding path 구현
4.2.1 가장 마지막 좌표에서부터 시작. 각 좌표의 direction을 path라는 list에 넣고, 대각선/왼쪽/아래 좌표로 가는 recursive function을 만든다.
4.2.2 여러개의 path가 가능한 경우, 대각선, 좌우, 상하 방향 순으로 하나만 선택한다.
4.2.3 여러개의 path가 가능한 경우, 해당 지점(direction table의 값이 여러개인 지점)의 좌표를 branch_list라는 list에 저장한다.
4.2.4 가장 첫 좌표(0,0)에 도달하면 finding_path 함수를 중단한다.
4.2.5 finding_path를 중단하기 직전에 path라는 list는 direction이 마지막 좌표에서 첫 좌표로 가는 순서로 나열되어 있으니, reverse()를 이용하여 첫 좌표에서 마지막 좌표로 가는 순서로 뒤집어준다.

5. 여러개의 모든 가능한 path의 list인 path_list 만들기
5.1 접근 :  path를 하나 찾은 뒤, branch 지점을 기준으로, 이미 찾은 path의 direction 값을 지우고, 다시 finding_path를 하여 원하는 path를 찾아 나간다.
5.2 while 문의 구성
5.2.1 while문이 한번 돌아갈 때 finding_path를 통해 하나의 path를 찾는다.
5.2.2 해당 path를 path_list에 첨가한다
5.2.3 finding_path가 돌아가는 동안 branch 지점이 생겼는지 확인한다. 
5.2.3.1 branch_list 속 좌표 수가 0이라면, 이번에 찾은 path이외의 다른 path가 없다는 뜻이다. while문을 종료한다.
5.2.3.2 branch_list속 좌표 수가 0이 아니라면, 추가적인 path가 존재한다.
5.2.3.2.1 branch_list속 가장 첫 branch, 즉 (0,0)과 가장 가까운 branch 좌표를 last_branch라고 명명한다(path를 찾는 과정에서 가장 마지막에 만난 branch이므로 'last'라고 부른다)
5.2.3.2.2 last branch좌표에서 direction table의 가장 첫 값(즉, 현재 path를 만드는데 사용된 direction)을 지운다.
5.2.3.2.3 이제 새로운 while문은 수정된 direction table을 이용해 path를 찾는다. 즉 이미 찾은 path이외의 path를 찾는다.



6. align하기
6.1 path하나당 하나의 align이 만들어지며, 하나의 align은 [align 번호, align 된 첫번째 서열, align 된 두번째 서열로 구성된다.
6.2 path_list에서 각 path를 이용한 for loop를 사용한다.
6.3 각 path에서 각각의 direction을 읽는 for loop를 사용한다.
6.3.1 한 direction마다 1글자씩 align되고,이것은 align_1, align_2라는 list의 형태로 저장된다.
6.3.1.1 direction이 cross인 경우, 두 서열 모두 하나의 글자가 align_1, align_2에 저장되고, 다음 direction을 확인한다.
6.3.1.2 direction이 right인 경우, align_1에는 '-'가 저장되고, align_2에는 비교하던 글자가 저장된다.
6.3.1.3 direction이 down인 경우, align_1에는 비교하던 글자가 저장되고, align_2에는 '-'가 저장된다. 
6.3.1.4 해당 path의 모든 direction을 확인했으면 for loop가 종료된다. list형태의 align_1와 align_2를 string으로 변환해준다.
6.4 path_ list의 모든 path를 확인했으면 for loop종료


7. 최종 결과 도출
7.1 각 align list의 align들을 align 번호, 첫 번째 서열, 두번째 서열 순으로 프린트한다.


8. 연속된 deletion에 가중치 주기.
sequence1 을 GAATTCGGAATTC
sequence2 를 GAATTCTTTTTTGAATTC와 같이 입력해주면

Alignment 1
-GAATTC-----GGAATTC
-GAATTCTTTTTTGAATTC

Alignment 2
-GAATTC----G-GAATTC
-GAATTCTTTTTTGAATTC

와 같은 결과가 여러개 나온다.

이 때 deletion이 연속적으로 많이 되는 경우가 좋은 align이라고 생각하여
deletion이 연속될 경우에 가중치를 주는 방법을 생각했다.

각 alignment에서 -N-이 발견되는 경우에 score를 더해준 뒤 dictionary에 넣었다.
score를 비교하여 가장 작은것들만 출력햊기 위해 dictionary를 사용했다.

가장 작은 score를 dictionary에서 찾아낸 뒤
나머지 score를 가진 alignment result들을 제거한다
결과를 출력한다.


"""
