from passwordGenerator import passwordGen

if __name__ == '__main__':
    tri = passwordGen()
    print( tri.genPass(15, True, True, True, True) )