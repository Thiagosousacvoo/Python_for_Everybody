def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        overtime = h - 40
        pay = (40 * r) + (overtime * r * 1.5)
    return pay

hrs = input("Horas: ")
rate = input("Taxa: ")
h = float(hrs)
r = float(rate)
p = computepay(h, r)

print("Pay", p)
