from array import array



class Sudoku:
    
  
    
    
    
                    
                    
    

    @staticmethod
    def check_column_intern(a):
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
                       return true
               
                    else:
                       return false
   
 
 
 
    @staticmethod
    def check_column(a):
                    if len(a)!= 9:
                        print("In der Spalte stehen keine neun Elemente") #ersetze später durch ein return statement
                
                    else:
                        check_column_intern(a)
                        
               
langeweile = Sudoku()
testliste = [1,2,3,4,5,6,7,8,9]
print(langeweile.check_column(testliste))
print(len(testliste))
                       
   
    
    
    
    
    
    
    
    
    
