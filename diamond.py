a = 10
t = " "
n = 1
d = "&"

# right-side-up triangle gen

for i in range(10):
    while n <= 10:
        p = (2 * n - 1)
        print((t * a) + (d * p))
        a = a - 1
        n = n + 1

b = 1
j = 19
h = " "
e = "&"
m = 1

# upside down triangle gen

for s in range(10):
    while m <= 10:
        f = (2 * j - 19)
        print ((h * b) + (e * f))
        m = m + 1
        b = b + 1
        j = j - 1
