n=int(input())
nn=int(input())
q=[]
for i in range(n):
    job=input().split()
    if job[0]=='dequeue':
        if len(q)==0:
            print('Queue is empty')
        else:
            print('Processed request ID:',q[0][0])
            q.pop(0)
    elif job[0]=='enqueue':
        if len(q)<nn:
            job.pop(0)
            print('Enqueued request ID:',job[0])
            q.append(job[0])
        else:
            print('Queue is full')
    elif job[0]=='size':
        print('Current queue size:',len(q))
    elif job[0]=='display':
        if len(q)==0:
            print('Queue is empty')
        else:
            print('Queue elements:',' '.join(q))