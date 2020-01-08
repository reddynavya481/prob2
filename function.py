def prime(n):
  c=0
  for i in range(1,n):
    if(n%i==0):
      c+=1
  if(c==1):
    return "yes"
  else:
    return "no"
    
    
def revlist(arr):
  return arr[::-1]


def rotating(k,ar):
  for i in range(0,k):
    k2=ar.pop(0)
    ar.append(k2)
  return ar


def sortlists(ar1,ar2):
  l1=ar1[:]
  #l2=ar2[:]
  ar1.sort()
  #ar2.sort()
  if(ar1==l1):
    if(ar2==sorted(ar2)):
      return ar1+ar2
    else:
      return "second array is not sorted"
  else:
    return "first array is not sorted"


def numtoarr(k):
  l=[]
  while(k>0):
    r=k%10
    l.append(r)
    k=k//10
  return revlist(l)


def kthlargest(ar,k):
  ar1=ar[:]
  ar1.sort()
  k2=ar1[len(ar)-k]
  ar.remove(k2)
  return ar

def mulmatrices(m1,m2):

  






