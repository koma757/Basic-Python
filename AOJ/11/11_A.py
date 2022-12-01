class dice:
  def __init__(self,surf):
    self.o = surf[0] 
    self.s = surf[1]
    self.e = surf[2]
    self.w = surf[3]
    self.n = surf[4]
    self.c = surf[5]
  def dice_rot(self,direction):
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
    return self.o
##
##
surf = list(map(int,input().split())) 
direct = str(input())
Dice = dice(surf)
for i in direct:
  ans = Dice.dice_rot(i)
print(ans)
    
  	