try:
    num1,num2=eval(input("Enter two numbers:") ("separated by comma"))
    result=num1/num2
    print("result is",result)
    #using multiple except block for diffrent types of exception
except ZeroDivisionError as ex:
    print("division by zero is error")
except SyntaxError:
    print("Syntax comma needed")
except:
    print("Wrong input")
finally:
    print("This will execute no matter what")