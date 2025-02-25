"""
Consider a linear queue used in a print server that manages multiple print jobs. Due to heavy load, the queue frequently overflows. Propose and implement a solution using a linear queue that minimizes the overflow while ensuring fair scheduling of print jobs.
"""
n=int(input())
q=[]
for i in range(n):
    job=input().split()
    if job[0]=='process_jobs':
        print('Processing print jobs:')
        while len(q)>0:
            print('Processing Job ID:',q[0][0]+',','Priority:',q[0][1])
            q.pop(0)
    elif job[0]=='add_job':
        job.pop(0)
        print('Added: Job ID:',job[0]+',','Priority:',job[1])
        q.append(job)
    elif job[0]=='queue_size':
        print('Current queue size:',len(q))