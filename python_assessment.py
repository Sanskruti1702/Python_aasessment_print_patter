
# Online Python - IDE, Editor, Compiler, Interpreter
#considering n=3

def print_pattern(n):   #defining a function to print the given pattern
#part 1 for upper triangle
    for i in range(1,n+1):   #looping over the number of rows i.e.(from 1 to 3)
        print(" "*(n-i)+" ".join(chr(65+j) for j in range(i)))  #print the pattern using the chr() function to access the alphabet
#part 2 for lower triangle                                                                  #and concat(+) operator
    for i in range(n-1,0,-1):
        print(" "*(n-i)+" ".join(chr(65+j) for j in range(i)))
    
n=int(input("Enter an number:"))  #taking an input
print_pattern(n)                  #calling the function
    
        
