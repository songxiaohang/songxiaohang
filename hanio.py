while True:
  def hanoi(a,b,c,n):
    if n==1:
      print(a,'=>','c')
    else:
      hanoi(a,c,b,n-1)
      print(a,'=>',c)
      hanoi(b,a,c,n-1)

  try:
    n=int(input('Please input a number:'))
    hanoi('a','b','c',n)
  except:
    print("It's not a positive integer")
    
  Y=input('Do you want again?(y or n)\n')
  if Y=='n':
    break
  else:
    continue
    
print('The game is over!')
