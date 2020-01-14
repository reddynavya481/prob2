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


def insert(d):
  if(not d):
    root=int(input('enter root node'))
    d[root]=''
  else:
    n=int(input('enter node'))
    print('enter edges for',n)
    ed=list(map(int,input().split()))
    f=0
    for i in ed:
      if(i in d.keys()):
        f=1
        break
    if(f==1):
      d[n]=ed
    d[n]=ed
  return d


def delete(d):
  k=int(input('enter node to delete'))
  d.pop(k)
  return d


def dsforgraph():
  d={1:''}
  while(1):
    v=int(input("1 for inserting node and 2 for deleting it"))
    if(v==1):
      d=insert(d)
    elif(v==2):
      d=delete(d)
    k=int(input('do u want to continue enter 1 else enter 0'))
    if(k==0):
      break
  print(d)
  return d
    
    





def texttomorse(s1):
  d={'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
  s1=s1.upper()
  s=''
  for i in s1:
    s+=d[i]
  return s



def morsetotext(s1):
  d={'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
  s1 += ' '
  kl=list(d.keys())
  vl=list(d.values())
  dec = '' 
  wor = '' 
  for i in s1: 
    if (i != ' '): 
      var = 0
      wor += i 
    else: 
      var += 1
      if var == 2 : 
        dec += ' '
      else: 
        dec += kl[vl.index(wor)] 
        wor = '' 
  return dec 

    
    
        


def mulmatrices(m1,m2):
  ar=[]
  ar1=[]
  res=0
  for i in range(len(m1[0])):
    res=0
    ar=[]
    for j in range(len(m2)):
      res=0
      for k in range(len(m2)):
        res+=m1[i][k]*m2[k][j]
      ar.append(res)
    ar1.append(ar)
  return ar1





def rps(val):
  if(val=='rock'):
    res='paper'
  elif(val=='paper'):
    res='scissors'
  elif(val=='scissors'):
    res='rock'
  return res



def sortByLength1(l1):
  l1.sort(key=len)
  return l1


def sortByLength2(l1):
  ar=[]
  ar1=[]
  res=[]
  for i in l1:
    ar.append([len(i),i])
    ar1.append(len(i))
  print(ar)
  print(ar1)
  for i in range(len(ar)):
    k=ar1.count(ar[i][0])
    ar[i][0]=k
  ar.sort(key=lambda x:x[0])
  for i in ar:
    res.append(i[1])
  return res












  

  

      



  






