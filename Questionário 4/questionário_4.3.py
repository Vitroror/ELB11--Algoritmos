c = 0
while c <= 100:
    f = c * (9/5) + 32
    print(f"{c:>3d} Celsius -> {f:>5.1f} Fahrenheit")
    c = c + 10