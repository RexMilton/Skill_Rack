import datetime 
s=input().strip()
x,y,z=map(int,input().split())
d=datetime.datetime.strptime(s,'%H:%M:%S')
d+=datetime.timedelta(hours=x)
print(d.strftime('%H:%M:%S'))
d+=datetime.timedelta(minutes=y)
print(d.strftime('%H:%M:%S'))
d+=datetime.timedelta(seconds=z)
print(d.strftime('%H:%M:%S'))
