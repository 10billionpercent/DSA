def sorting(n,str1):
    l1=[]
    for i in str1:
        if i.isdigit():
            l1.append(int(i))
    l1.sort()
    for i in l1:
        print(i,end=' ')
sorting(5,'1 2 3 4 5')