t=int(input())
for _ in range(t):
    characters=list(input())
    word=list(input())
    count=0

    for i in range(1,len(word)):
        k=word[i]
        b=word[i-1]
        count+= abs(characters.index(k)-characters.index(b))
    
    print(count)
