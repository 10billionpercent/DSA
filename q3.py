def fn(a,str1,target):
    l1=[]
    for i in str1:
        if i.isdigit():
         l1.append(int(i))
    print(l1.count(target))
fn(5,'1 2 3 2 4',2)