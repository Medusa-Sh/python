class myclass:
    
    __private_var =27

    def __privMeth(self):
        print("I'm inside of private method")


    def hello(self):
        print("Hello from public method", myclass.__private_var)
        self.__privMeth()
foo=myclass()
foo.hello()
foo.__privMeth