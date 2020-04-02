def factorise(x: int):  # O(sqrt(n))
    factors = []
    d = 2
    a = math.sqrt(x)
    while d <= a:
        if x % d == 0:
            factors.append(d)
            x //= d
        else:
            d += 1
    if x > 1:
        factors.append(int(x))
    return factors
  
  n = input()
  print(factorise(n))
