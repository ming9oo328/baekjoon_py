A=list(map(int,input().split()))
B=list(map(int,input().split()))


if A==B:
    print(10,10)
    print("D")
else:
    acount=bcount=0
    for i in range(10):
      if A[i]>B[i]:
          acount+=3;win=A
      elif A[i]<B[i]:
          bcount+=3;win=B
      else:
          acount+=1
          bcount+=1
          
    print(acount,bcount)
    if acount>bcount:
      print("A")
    elif acount<bcount:
      print("B")
    else:
      print(win)