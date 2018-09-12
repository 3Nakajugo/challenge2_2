

def fizzbuzz(A, B):
    
    if not (isinstance(A, list) and isinstance(B, list)):
        return "Invalid input"
    C = len(A)+len(B)

    if (C % 5 == 0 and C % 3 == 0):
        return('fizzbuzz')
    elif (C % 3 == 0):
        return('fizz')
    elif (C % 5 == 0):
        return('buzz')
    else:
        return(C)


A = [1, 2, 3, 4]
B = [1, 2, 3, 4]
fizzbuzz(A, B)
