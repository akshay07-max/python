# In Python, method overloading involves creating methods with the same name but different parameters within the same class (mimicked through workarounds), while method overriding involves a subclass redefining a method from its parent class

def add(datatype, *args): 
  
    # if datatype is int initialize answer as 0 
    if datatype =='int': 
        answer = 0
          
    # if datatype is str initialize answer as '' 
    if datatype =='str': 
        answer ='' 
  
    for x in args: 
  
        answer = answer + x 
  
    print(answer) 
  
# Integer 
add('int', 5, 6) 
  
# String 
add('str', 'Hi ', 'Geeks')