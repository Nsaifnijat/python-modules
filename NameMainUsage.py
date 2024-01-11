

'''
    Example, suppose we have file by the name of myfirstproject and in this file we have some methods
    and a print() statement which is outside the method or run globally, and later on we want to use this file 
    in our upcoming projects, now if we import this file then we will see that print() statement is already 
    executed before we call its methods, in order for this to be avoided then we have to define that print()
    statement in an
    if __name__='__main__':
        print('this is if statemnt')
    which makes it only executable when myfirstproject file is run directly otherwise when it is imported into other 
    files then this print() statemnent is not gonna be executed, so basically we put what is soley used for the myfirstproject
    file into this 
    if __name__='__main__':   
        statement.
    
    Note:
        if we run this 
        print(__name__)
        inside our myfirstproject file we get the name as    __main__
        but if we import myfirstproject into another file, eg. mysecondproject
        then if we run 
        print(__name__)
        then we get the name as   myfirstproject
    '''