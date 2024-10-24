import random

def main():
    print("Enter a number for A: ")
    a = float(input())
    b = random.randint(-10, 10)
    
    while b == 0:
        b = random.randint(-10, 10)
    
    print("Generate number B:", b)
    print("A/B =", a / b)
        
if __name__ == "__main__":
    main()
