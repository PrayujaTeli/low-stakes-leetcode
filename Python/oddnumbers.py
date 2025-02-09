def countOdds(num1, num2, num3, num4, num5):
    def odd(n):
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            return odd(n-2)
    return sum(1 for n in [num1, num2, num3, num4, num5]  if odd(n))
    
if __name__ == '__main__':
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        num4 = int(input())
        num5 = int(input())
        result = countOdds(num1, num2, num3, num4, num5)
        print(f'Total odds: { result }')
    
