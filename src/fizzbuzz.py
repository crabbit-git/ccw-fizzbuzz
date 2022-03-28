def fizzbuzz(int):
    fizz = ""
    buzz = ""
    if int % 3 == 0:
        fizz = "Fizz"
    if int % 5 == 0:
        buzz = "Buzz"
    if fizz+buzz != "":
        return fizz+buzz
    return str(int)
