import random 

# 33-126
class passwordGen():
    def __init__(self):
        pass

    def genUppercase(self) -> str:
        return chr(random.randint(65, 90))

    def genLowercase(self) -> str:
        return chr(random.randint(97, 122))

    def genSpecialChars(self) -> str:
        x = random.randint(1, 4)
        match x:
            case 1:
                return chr(random.randint(33, 47))
            case 2:
                return chr(random.randint(58, 64))
            case 3:
                return chr(random.randint(91, 96))
            case 4:
                return chr(random.randint(123, 126))

    def genNums(self) -> str:
        return chr(random.randint(48, 57))

    def genPass(self, length:int, addUppers: bool, addLowers: bool, addNums: bool, addSpecs: bool):
        password = ''
        listOfChoices = []
        for choices in range(0, 4):
            if addUppers:
                listOfChoices.append(1)
            if addLowers:
                listOfChoices.append(2)
            if addNums:
                listOfChoices.append(3)
            if addSpecs:
                listOfChoices.append(4)
        
        for i in range(length):
            pw = random.choice(listOfChoices)
            match pw:
                case 1:
                    if addUppers:
                        password += self.genUppercase()
                case 2:
                    if addLowers:
                        password += self.genLowercase()
                case 3:
                    if addNums:
                        password += self.genNums()
                case 4:
                    if addSpecs:
                        password += self.genSpecialChars()    
        return password


if __name__ == '__main__':
    tri = passwordGen()
    print( tri.genPass(15, True, True, True, True) )
