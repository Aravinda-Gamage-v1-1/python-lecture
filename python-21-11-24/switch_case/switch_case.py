response_code = 404

match response_code:
    case 200: 
        print("OK")
    case 201:
        print("Created")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Something else")


index = "E"

match index:
    case "A":
        print(100)
    case "B":
        print(80)
    case "C":
        print(60)
    case "D":
        print(40)
    case "E":
        print(20)
    case _:
        print(10)


numbers = [4, 6, 10]

match numbers:
    case [x, y]:
        print(x * y)
    case [x, y, z]:
        print(x + y + z)
    case _:
        print("Invalid")

length = []

match length:
    case []:
        print("Empty")
    case [x]:
        print("Has one element")
    case[x, y]:
        print("Has two elements")
    case _:
        print("Something else")