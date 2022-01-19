set1 = {10,20,30,40,50,60}
set2 = {30,40,50,60,70,80}


print("첫번째 세트  ", set1)
print("두번째 세트  ", set2)


Q = set1.union(set2)
W = set1 & set2
E = Q - W


print("어느 한쪽에만 있는 요소들", E)
