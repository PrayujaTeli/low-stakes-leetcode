def median(FirstNumber,SecondNumber,ThirdNumber):
    if (FirstNumber > SecondNumber and FirstNumber < ThirdNumber) or (FirstNumber < SecondNumber and FirstNumber > ThirdNumber):
        return FirstNumber
    elif (SecondNumber > FirstNumber and SecondNumber < ThirdNumber) or (SecondNumber < FirstNumber and SecondNumber > ThirdNumber):
        return SecondNumber
    elif (ThirdNumber > FirstNumber and ThirdNumber < SecondNumber) or (ThirdNumber < FirstNumber and ThirdNumber > SecondNumber):
        return ThirdNumber
    else:
        return None

if __name__ == "__main__":
    FirstNumber = int(input())
    SecondNumber = int(input())
    ThirdNumber = int(input())
    
    mediannumber =  median(FirstNumber,SecondNumber,ThirdNumber)
    
    print(mediannumber)