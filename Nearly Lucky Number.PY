nums=(list(input()))
count=0
for num in nums:
    if num  in["4","7"]:
        count+=1
count=str(count)
if all (d in "47" for d in count):
    print("YES")
else:
    print("NO")
