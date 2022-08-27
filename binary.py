Gowtham naidu
Vdg
Hd
from timeit import default_timer
pos=-1
def search(list,n):
  l=0
  u=len(list)
  while l<=u:
    mid=(l+u)//2
    if list[mid]==n:
       globals()["pos"]=mid
       return True
    else:
        if list[mid]<n:
            l=mid+1;
        else:
            u=mid-1;
start = default_timer()
list=[1,2,3,4,5,6]
n=5
if search(list,n):
 print("found at",pos)
 duration = default_timer() - start
 print("found in", duration, "seconds")
else:
 print("not found")
