n=int(input())
q=[]
for i in range(n):
    job=input().split()
    if job[0]=='dequeue':
        if len(q)==0:
            print('Queue is empty')
        else:
            print('Processed request ID:',q[0][0],'with priority:',q[0][1])
            q.pop(0)
    if job[0]=='enqueue':
        job.pop(0)
        print('Enqueued request ID:',job[0],'with priority:',job[1])
        q.append(job)