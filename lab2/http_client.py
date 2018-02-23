import asyncio
import requests
import sys
from time import sleep

#def custom_sleep():
    #print('SLEEP', datetime.now())
#    time.sleep(1)

async def asynch(n):
    r = requests.get('https://requestb.in/1jw165x1')
    print("This is async "+str(n)+" "+str(r.content) +"enter")
    await asyncio.sleep(1)
    print("This is async "+str(n)+" "+str(r.content) +"exit")

def sync(n):
    r = requests.get('https://requestb.in/1jw165x1')
    print("This is sync "+str(n)+" "+str(r.content) +"enter")
    #await custom_sleep()
    print("This is sync "+str(n)+" "+str(r.content) +"exit")

if __name__ == '__main__':
    l=sys.argv

    if l[1]=='async':
        loop = asyncio.get_event_loop()
        for i in range(1,int(l[2])+1):
            t=[]
            t.append(asyncio.ensure_future(asynch(i)))
        loop.run_until_complete(asyncio.wait(t))
        loop.close()
    if l[1]=='sync'  :
        loop = asyncio.get_event_loop()
        for i in range(1,int(l[2])+1):
            sync(i)
