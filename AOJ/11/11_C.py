class dice:
  def __init__(self,surf):
    self.o = surf[0] 
    self.s = surf[1]
    self.e = surf[2]
    self.w = surf[3]
    self.n = surf[4]
    self.c = surf[5]
  def dice_roll(self,direction):
    if direction == 'S':
      self.n,self.c,self.s,self.o \
      = self.c,self.s,self.o,self.n
    elif direction == 'E':
      self.w,self.c,self.e,self.o \
      = self.c,self.e,self.o,self.w
    elif direction == 'W':
      self.e,self.c,self.w,self.o \
      = self.c,self.w,self.o,self.e
    elif direction == 'N':
      self.s,self.c,self.n,self.o \
      = self.c,self.n,self.o,self.s
    return [self.o,self.s,self.e,self.w,self.n,self.c] 
  def dice_rot(self):
    self.s,self.e,self.n,self.w \
    = self.w,self.s,self.e,self.n
    return [self.o,self.s,self.e,self.w,self.n,self.c]
    
surf1 = list(map(int,input().split())) 
surf2 = list(map(int,input().split())) 
dice1 = dice(surf1)
dice2 = dice(surf2)
judg = False
for i in 'NNNNWWWW':
  surf1 = dice1.dice_roll(i)
  if surf1[0]==surf2[0] and surf1[-1]==surf2[-1]:   
    for j in range(4):
      surf1 = dice1.dice_rot()
      if surf1 == surf2:
        judg = True
        break
if judg == True:
  print('Yes')
else:
  print('No')



    
  	