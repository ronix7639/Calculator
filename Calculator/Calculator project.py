import math

def calc():
        print("Select an operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Find reminder")
        print("6. Absolute division")
        print("7. Sin")
        print("8. Cos")
        print("9. tan")
        print("10. Sin inverse")
        print("11. Cos inverse")
        print("12. Tan inverse")
        print("13. log")
        print("14. Power")
        print("15. Square root")
        print("16. Factorial")
        
        operation = input('Enter your choice: ')

        
        if(operation =='Add'):
            # code for add
            print('Great choice!\n I will like to be extracting some values from you !')
            n = int(input('enter number of entries:'))
            lst= []
            for i in range(1,n+1):
                    values = int(input('Enter the value of %d :'%i))
                    lst.append(values)
            print('Sum of the two numbers is',sum(lst))
        elif(operation =='Subtract'):
            # code for subtract
            print('Great choice!\n I will like to be extracting some values from you !')
            a = float(input('enter a value: '))
            b = float(input('enter a value: '))
            c= a-b
            print('Difference of the two numbers is' ,c)
        elif(operation == 'Multiply'):
            #code for multiplication
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             b = float(input('enter a value: '))
             c= a*b
             print('Product of the two numbers is' ,c)
        elif(operation == 'Divide'):
            #code for multiplication
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             b = float(input('enter a value: '))
             c= a/b
             print('Divided value of the two numbers is' ,c)
        elif(operation =='Find reminder'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             b = float(input('enter a value: '))
             c= a%b
             print('Reminder when these two numbers are divided  is' ,c)
        elif(operation == 'Absolute division'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             b = float(input('enter a value: '))
             c= a//b
             print('Absolute Divided value of the two numbers is' ,c)
             
        elif(operation =='Sin'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the sin function is:',math.sin(a))
        elif(operation =='Cos'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the cos function is:',math.cos(a))
        elif(operation =='tan'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the  function is:',math.tan(a))
        elif(operation == 'Sin inverse'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the inverse function is:',math.asin(a))
        elif(operation =='Cos inverse'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the cos function is:',math.acos(a))
        elif(operation =='tan inverse'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the  function is:',math.atan(a))
        elif(operation == 'log'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a = float(input('enter a value: '))
             print('The value of the log function is:',math.log(a))
        elif(operation == 'Power'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a =  float(input('enter a value: '))
             b =  float(input('enter a value: '))
             print('The value of the  function is:',math.pow(a,b))
        elif(operation == 'Square root'):
             print('Great choice!\n I will like to be extracting some values from you !')
             a =  float(input('enter a value: '))
             print('The value of the  function is:',math.sqrt(a))
        elif(operation == 'Factorial'):
                print('Great choice!\n I will like to be extracting some values from you !')
                a =  int(input('enter a value: '))
                fact =  1
                if a<0:
                        for i in range(a,0,1):
                                fact *= i
                else:
                        for i in range(1,a+1):
                                fact *= i
                print('The value of factorial is :' , fact)
                
                
                
                
#call the function            
calc()