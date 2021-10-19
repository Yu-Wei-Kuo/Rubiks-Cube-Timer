import random
def scramble3():
     
     moves = [1, 2, 11 , 12 , 21 , 22]
     director = ["" , "'" , "2"]
     lengh = random.randint(18, 21)


     #隨機打亂
     scmoves = []
     scdir = []
     for x in range(lengh):
          scmoves.append(random.choice(moves))
          scdir.append(random.choice(director))

     #檢查不合情況
     for x in range(1, lengh):
          if scmoves[x] == scmoves[x-2] or scmoves[x] == scmoves[x-1]:
               while scmoves[x] == scmoves[x-1] or abs(scmoves[x] - scmoves[x-1]) == 1:
                    scmoves[x] = random.choice(moves)
                         
     #資料整理
     letter = {1:'R', 2:'L', 11:'U', 12:'D', 21:'F', 22:'B'}
     scletter = [letter[x] if x in letter else x for x in scmoves]
     sc=[]
     for x in range(lengh):
          sc.append(scletter[x] + scdir[x])

     return sc