def fizzbuzz(int):
    fizz = ""
    buzz = ""
    if int % 3 == 0:
        fizz = "Fizz"
    if int % 5 == 0:
        buzz = "Buzz"
    return fizz+buzz
