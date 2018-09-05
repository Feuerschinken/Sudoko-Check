from array import array
import numpy as np


class Sudoku:

# All values with a refer to the first (zero) row.
    sudoku = [None, None, None, None, None, None, None, None, None]
    
    def __init__(self, a0, a1, a2, a3, a4, a5, a6, a7, a8, b0, b1, b2, b3, b4, b5, b6, b7, b8, c0, c1, c2, c3, c4, c5, c6, c7, c8, d0, d1, d2, d3, d4, d5, d6, d7, d8, e0, e1, e2, e3, e4, e5, e6, e7, e8, f0, f1, f2, f3, f4, f5, f6, f7, f8, g0, g1, g2, g3, g4, g5, g6, g7, g8, h0, h1, h2, h3, h4, h5, h6, h7, h8, i0, i1, i2, i3, i4, i5, i6, i7, i8):
        self.sudokua = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
        self.sudokub = [b0, b1, b2, b3, b4, b5, b6, b7, b8]
        self.sudokuc = [c0, c1, c2, c3, c4, c5, c6, c7, c8]
        self.sudokud = [d0, d1, d2, d3, d4, d5, d6, d7, d8]
        self.sudokue = [e0, e1, e2, e3, e4, e5, e6, e7, e8]
        self.sudokuf = [f0, f1, f2, f3, f4, f5, f6, f7, f8]
        self.sudokug = [g0, g1, g2, g3, g4, g5, g6, g7, g8]
        self.sudokuh = [h0, h1, h2, h3, h4, h5, h6, h7, h8]
        self.sudokui = [i0, i1, i2, i3, i4, i5, i6, i7, i8]

    @staticmethod
    def check_row_intern(a):
                    one = 0
                    two = 0
                    three = 0
                    four = 0
                    five = 0
                    six = 0
                    seven = 0
                    eight = 0
                    nine = 0
                    wrong_number= 0
                    
                    i = 0
                    for i in range (0, len(a)):
                       if a[i] == 1:
                           one += 1
   
                       elif a[i] == 2:
                           two += 1
                           
                       elif a[i] == 3:
                           three += 1
   
                       elif a[i] == 4:
                           four += 1
   
                       elif a[i] == 5:
                           five += 1
                    
                       elif a[i] == 6:
                           six += 1
    
                       elif a[i] == 7:
                           seven += 1
   
                       elif a[i] == 8:
                           eight += 1
    
    
                       elif a[i] == 9:
                           nine += 1
   
           
                       else:
                           wrong_number += 1
   
   
                    if (one == 1 and two == 1 and three == 1 and four == 1 and five == 1 and six == 1 and seven == 1 and eight == 1 and nine == 1):
                       return True
               
                    else:
                       return False
   
 
 
 
    @staticmethod
    def check_row(a):
                    if len(a)!= 9:
                        print("In der Spalte stehen keine neun Elemente") #ersetze später durch ein return statement
                
                    else:
                        return langeweile.check_row_intern(a)
                        
               

    @staticmethod
    def check_column(column, a, b, c, d, e, f, g, h, i):
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        wrong_number= 0
                    
        
    
        if  a[column] == 1:
            one += 1
   
        elif a[column] == 2:
            two += 1
                           
        elif a[column] == 3:
            three += 1
   
        elif a[column] == 4:
            four += 1
   
        elif a[column] == 5:
            five += 1
                    
        elif a[column] == 6:
            six += 1
    
        elif a[column] == 7:
            seven += 1
   
        elif a[column] == 8:
            eight += 1
    
    
        elif a[column] == 9:
            nine += 1
            
            
        
        if  b[column] == 1:
            one += 1
   
        elif b[column] == 2:
            two += 1
                           
        elif b[column] == 3:
            three += 1
   
        elif b[column] == 4:
            four += 1
   
        elif b[column] == 5:
            five += 1
                    
        elif b[column] == 6:
            six += 1
    
        elif b[column] == 7:
            seven += 1
   
        elif b[column] == 8:
            eight += 1
    
    
        elif b[column] == 9:
            nine += 1
   
           
        
        if  c[column] == 1:
            one += 1
   
        elif c[column] == 2:
            two += 1
                           
        elif c[column] == 3:
            three += 1
   
        elif c[column] == 4:
            four += 1
   
        elif c[column] == 5:
            five += 1
                    
        elif c[column] == 6:
            six += 1
    
        elif c[column] == 7:
            seven += 1
   
        elif c[column] == 8:
            eight += 1
    
    
        elif c[column] == 9:
            nine += 1
   
        
        if  d[column] == 1:
            one += 1
   
        elif d[column] == 2:
            two += 1
                           
        elif d[column] == 3:
            three += 1
   
        elif d[column] == 4:
            four += 1
   
        elif d[column] == 5:
            five += 1
                    
        elif d[column] == 6:
            six += 1
    
        elif d[column] == 7:
            seven += 1
   
        elif d[column] == 8:
            eight += 1
    
    
        elif d[column] == 9:
            nine += 1
        

        if  e[column] == 1:
            one += 1
   
        elif e[column] == 2:
            two += 1
                           
        elif e[column] == 3:
            three += 1
   
        elif e[column] == 4:
            four += 1
   
        elif e[column] == 5:
            five += 1
                    
        elif e[column] == 6:
            six += 1
    
        elif e[column] == 7:
            seven += 1
   
        elif e[column] == 8:
            eight += 1
    
    
        elif e[column] == 9:
            nine += 1            
        
        
        if  f[column] == 1:
            one += 1
   
        elif f[column] == 2:
            two += 1
                           
        elif f[column] == 3:
            three += 1
   
        elif f[column] == 4:
            four += 1
   
        elif f[column] == 5:
            five += 1
                    
        elif f[column] == 6:
            six += 1
    
        elif f[column] == 7:
            seven += 1
   
        elif f[column] == 8:
            eight += 1
    
    
        elif f[column] == 9:
            nine += 1
        
        if  g[column] == 1:
            one += 1
   
        elif g[column] == 2:
            two += 1
                           
        elif g[column] == 3:
            three += 1
   
        elif g[column] == 4:
            four += 1
   
        elif g[column] == 5:
            five += 1
                    
        elif g[column] == 6:
            six += 1
    
        elif g[column] == 7:
            seven += 1
   
        elif g[column] == 8:
            eight += 1
    
    
        elif g[column] == 9:
            nine += 1
        
        
        if  h[column] == 1:
            one += 1
   
        elif h[column] == 2:
            two += 1
                           
        elif h[column] == 3:
            three += 1
   
        elif h[column] == 4:
            four += 1
   
        elif h[column] == 5:
            five += 1
                    
        elif h[column] == 6:
            six += 1
    
        elif h[column] == 7:
            seven += 1
   
        elif h[column] == 8:
            eight += 1
    
    
        elif h[column] == 9:
            nine += 1
        
        
        if  i[column] == 1:
            one += 1
   
        elif i[column] == 2:
            two += 1
                           
        elif i[column] == 3:
            three += 1
   
        elif i[column] == 4:
            four += 1
   
        elif i[column] == 5:
            five += 1
                    
        elif i[column] == 6:
            six += 1
    
        elif i[column] == 7:
            seven += 1
   
        elif i[column] == 8:
            eight += 1
    
    
        elif i[column] == 9:
            nine += 1
        
        if (one == 1 and two == 1 and three == 1 and four == 1 and five == 1 and six == 1 and seven == 1 and eight == 1 and nine == 1):
            
            return True
               
        else:
            
            return False

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    @staticmethod
    def check_sudoku():
       a = langeweile.check_row(langeweile.sudokua)
       b = langeweile.check_row(langeweile.sudokub)
       c = langeweile.check_row(langeweile.sudokuc)
       d = langeweile.check_row(langeweile.sudokud)
       e = langeweile.check_row(langeweile.sudokue)
       f = langeweile.check_row(langeweile.sudokuf)
       g = langeweile.check_row(langeweile.sudokug)
       h = langeweile.check_row(langeweile.sudokuh)
       i = langeweile.check_row(langeweile.sudokui)
       j = langeweile.check_column(0, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       k = langeweile.check_column(1, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       l = langeweile.check_column(2, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       m = langeweile.check_column(3, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       n = langeweile.check_column(4, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       o = langeweile.check_column(5, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       p = langeweile.check_column(6, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       q = langeweile.check_column(7, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
       r = langeweile.check_column(8, langeweile.sudokua, langeweile.sudokub,langeweile.sudokuc,langeweile.sudokud,langeweile.sudokue,langeweile.sudokuf,langeweile.sudokug,langeweile.sudokuh,langeweile.sudokui)
        
       if (a and b and c and d and e and f and g and h and i and j and k and l and m  and n and o and p and q and r):
           return True
       else:
           return False

       #print("j:" + str(j))
       #print("k:" + str(k))
       #print("l:" + str(l))
       #print("m:" + str(m))
       #print("n:" + str(n))
       #print("o:" + str(o))
       #print("p:" + str(p))
       #print("q:" + str(q))
       #print("r:" + str(r))





















langeweile = Sudoku(1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,1,3,4,5,6,7,8,9,1,2,4,5,6,7,8,9,1,2,3,5,6,7,8,9,1,2,3,4,6,7,8,9,1,2,3,4,5,7,8,9,1,2,3,4,5,6,8,9,1,2,3,4,5,6,7,9,1,2,3,4,5,6,7,8)
#print(langeweile.check_row(langeweile.sudoku))

print(langeweile.sudokua)
print(langeweile.sudokub)
print(langeweile.sudokuc)
print(langeweile.sudokud)
print(langeweile.sudokue)
print(langeweile.sudokuf)
print(langeweile.sudokug)
print(langeweile.sudokuh)
print(langeweile.sudokui)

print("Der Test auf Korrektheit liefert " + str(langeweile.check_sudoku()))





langeweile.check_sudoku()                

    
    
    
    
    
    
    
    
    
