def library():
    class borrow:
        set_is_borrowed=True
        if set_is_borrowed==True:
            print("You borrowed the bookA.")
        set_is_borrowed2=True
        if set_is_borrowed2==True:
            print("You borrowed the bookB.")
        set_is_borrowed3=True
        if set_is_borrowed3==True:
            print("You borrowed the bookC.")      
    class returned:
        set_is_borrowed=False
        if set_is_borrowed==False:
            print("The bookA is returned successfully.")
        set_is_borrowed2=False
        if set_is_borrowed2==False:
            print("The bookB is returned successfully.")
        set_is_borrowed3=False
        if set_is_borrowed3==False:
            print("The bookC is returned successfully.")
library()