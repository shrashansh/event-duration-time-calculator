hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mx=mins+dura
h1=mx//60
m1=mx%60
hy=h1+hour
hm=hy%24
print(hm,":",m1)