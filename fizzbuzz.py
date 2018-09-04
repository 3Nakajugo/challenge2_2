A=[]
B=[]    
A= input('enter for list A:')        
B= input('enter for list B:')

def fizzbuzz (A,B):
   
    C=len(A)+len(B)

    if  (C%5==0 and C%3==0):
        print( 'fizzbuzz')
    elif (C%3==0):
        print ('fizz')
    elif (C%5==0):
        print ('buzz')
    else:
         print (C)   
fizzbuzz(A,B)
