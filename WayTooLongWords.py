n=int(input())
for _ in range (n):
  m=(input())
  if len(m)>10:
    print(f"{m[0]}{(len(m)-2)}{m[-1]}")
  else:
    print(m)
