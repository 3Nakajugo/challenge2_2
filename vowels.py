
def countvowels():
    x =['a','e', 'i','o','u']
    letters = input("enter a sentence:")
    tuple(x)
    tuple(letters)
    dup_x=set(letters)
    dup = len(letters)- len(dup_x)
    count = ""
    for char in x:
        if char in letters:
             count +=str(char)
    print ((count, dup) )
countvowels()
