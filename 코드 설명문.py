"""
1. �ʱ� ����
���� sequences ������ �����Ѵ�
�������� alignment ������ �����Ѵ�.
ù ��° ����(sequence1), �� ��° ����(sequence2)�� �Է¹޴´�
addition/deletion�� �Ͼ �� distance�� ������ ��(add_del_constant)��
substitution�� �Ͼ �� ������ ��(substitution constant:)�� �Է¹޴´�.


2. distance table �����
2.1 distance table�� ��ǥ��(distance)�� ���ϴ� �Լ��� distance(a,b) �����
2.1.1 a�� b�� distance table�� ��ǥ�� �ǹ��Ѵ�.(���� ������ ����, a�� ������, b�� ������)
2.2 �� ��ǥ���� �ش� distance�� ������ �ϴ� distance_table ����
2.3 distance table�� ������ ��ǥ���� edit distance�̴�. 

3. direction table �����
3.1 �ش� ��ǥ�� direction�̶� distance_table�� �ش� ��ǥ�� �� ��ǥ�� ��, ����, �밢���� �� �� ��� ���� �������� 

����� ������ �ǹ��Ѵ�. ���� ������ direction�� cross, right, down�� �ִ�.
3.2 �� ��ǥ�� direction�� ���ϴ� �Լ��� direction(a,b)����
3.3 �� ��ǥ���� direction�� ������ �ϴ� direction_table����
3.3.1 float�� �νĵȴ� �������� .00000000001�̳� .999999���� ���� ��Ÿ�� ������ ����� ��찡 �־�, round method

�� �̿���

4. �ϳ��� path�� ã��
4.1 path�� (0,0) ���� ������ ��ǥ���� ����Ǵ� direction�� ������ ���Ѵ�.
4.2 path�� ���ϴ� �Լ��� finding path ����
4.2.1 ���� ������ ��ǥ�������� ����. �� ��ǥ�� direction�� path��� list�� �ְ�, �밢��/����/�Ʒ� ��ǥ�� ���� 

recursive function�� �����.
4.2.2 �������� path�� ������ ���, �밢��, �¿�, ���� ���� ������ �ϳ��� �����Ѵ�.
4.2.3 �������� path�� ������ ���, �ش� ����(direction table�� ���� �������� ����)�� ��ǥ�� branch_list��� list

�� �����Ѵ�.
4.2.4 ���� ù ��ǥ(0,0)�� �����ϸ� finding_path �Լ��� �ߴ��Ѵ�.
4.2.5 finding_path�� �ߴ��ϱ� ������ path��� list�� direction�� ������ ��ǥ���� ù ��ǥ�� ���� ������ �����Ǿ� 

������, reverse()�� �̿��Ͽ� ù ��ǥ���� ������ ��ǥ�� ���� ������ �������ش�.

5. �������� ��� ������ path�� list�� path_list �����
5.1 ���� :  path�� �ϳ� ã�� ��, branch ������ ��������, �̹� ã�� path�� direction ���� �����, �ٽ� 

finding_path�� �Ͽ� ���ϴ� path�� ã�� ������.

5.2 while ���� ����
5.2.1 while���� �ѹ� ���ư� �� finding_path�� ���� �ϳ��� path�� ã�´�.
5.2.2 �ش� path�� path_list�� ÷���Ѵ�

5.2.3 finding_path�� ���ư��� ���� branch ������ ������� Ȯ���Ѵ�. 
5.2.3.1 branch_list �� ��ǥ ���� 0�̶��, �̹��� ã�� path�̿��� �ٸ� path�� ���ٴ� ���̴�. while���� �����Ѵ�.

5.2.3.2 branch_list�� ��ǥ ���� 0�� �ƴ϶��, �߰����� path�� �����Ѵ�.
5.2.3.2.1 branch_list�� ���� ù branch, �� (0,0)�� ���� ����� branch ��ǥ�� last_branch��� ����Ѵ�(path�� ã�� 

�������� ���� �������� ���� branch�̹Ƿ� 'last'��� �θ���)
5.2.3.2.2 last branch��ǥ���� direction table�� ���� ù ��(��, ���� path�� ����µ� ���� direction)�� �����.
5.2.3.2.3 ���� ���ο� while���� ������ direction table�� �̿��� path�� ã�´�. �� �̹� ã�� path�̿��� path�� ã

�´�.



6. align�ϱ�
6.1 path�ϳ��� �ϳ��� align�� ���������, �ϳ��� align�� [align ��ȣ, align �� ù��° ����, align �� �ι�° ����]

�� �����ȴ�.
6.2 path_list���� �� path�� �̿��� for loop�� ����Ѵ�.
6.3 �� path���� ������ direction�� �д� for loop�� ����Ѵ�.
6.3.1 �� direction���� 1���ھ� align�ǰ�,�̰��� align_1, align_2��� list�� ���·� ����ȴ�.
6.3.1.1 direction�� cross�� ���, �� ���� ��� �ϳ��� ���ڰ� align_1, align_2�� ����ǰ�, ���� direction�� Ȯ����

��.
6.3.1.2 direction�� right�� ���, align_1���� '-'�� ����ǰ�, align_2���� ���ϴ� ���ڰ� ����ȴ�.
6.3.1.3 direction�� down�� ���, align_1���� ���ϴ� ���ڰ� ����ǰ�, align_2���� '-'�� ����ȴ�. 
6.3.1.4 �ش� path�� ��� direction�� Ȯ�������� for loop�� ����ȴ�. list������ align_1�� align_2�� string���� ��

ȯ���ش�.
6.4 path_ list�� ��� path�� Ȯ�������� for loop����


7. ���� ��� ����
7.1 �� align list�� align���� align ��ȣ, ù ��° ����, �ι�° ���� ������ ����Ʈ�Ѵ�.

"""
