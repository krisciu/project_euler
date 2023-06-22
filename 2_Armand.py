l = 1
r = 2
es = 2
while True:
  tot = l + r
  if tot > 4000000:
    break
  if tot % 2 == 0:
    es = es + tot
  l = r
  r = tot
print(es)
  
