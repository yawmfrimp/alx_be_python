try: #so inside the code, you use the try part to test for where something might go wrong in the code
    vision = open('vision.py')
except FileNotFoundError: 
    #you then use the except keyword together with the error you suspect, so that you can handle it
    #you can have multiple except lines to handle multiple errors
    #you can also use the exit() function in case you don't want the code to continue afer the error
    print('Masa the file no dey')