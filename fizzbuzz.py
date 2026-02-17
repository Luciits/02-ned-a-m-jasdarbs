import sys
if len(sys.argv) < 2:
    print("Kļūda! Nav norādīts skaitlis N.")
    print("Lietošana: python fizzbuzz.py <skaitlis N>")
    sys.exit(1)
try:
    n = int(sys.argv[1])
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 7 == 0:
            print("Jazz")
        elif i % 11 == 0:
            print("Tazz")   
        else:
            print(i)
except ValueError:
    print(f"Kļūda! '{sys.argv[1]}' nav derīgs skaitlis!")
    sys.exit(1)
