def happy_new_year():
    # countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")  # final line


def square_integers(int_list):
    result = []
    for num in int_list:
        result.append(num * num)
    return result


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
