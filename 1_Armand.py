t = 0
f = 0
s = 0
for i in range(1, 1000):
  a = False
  if i == t + 3:
    if not a:
      s = s + i
      a = True
    t = i
  if i == f + 5:
    if not a:
      s = s + i
      a = True
    f = i
print(s)
    

