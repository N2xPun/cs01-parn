x = str(input())

if x == "W":
    print("ติด ร")
else:
    y = str(input())
    z = str(input())
    w = str(input())   
    xi = int(x)
    yi = int(y)
    zi = int(z)
    wi = int(w)
    sum = xi + yi + zi + wi
    if sum >= 80:
        print(4)
    elif sum >= 75:
        print(3.5)
    elif sum >= 70:
        print(3)
    elif sum >= 65:
        print(2.5)
    elif sum >= 60:
        print(2)
    elif sum >= 55:
        print(1.5)
    elif sum >= 50:
        print(1)
    else:
        print(0)