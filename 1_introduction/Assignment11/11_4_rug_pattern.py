

def rug(n):
    B = []
    if n%2 != 0:
        emoji_bank = ["🐠","🐬","🐳","🐟","🐋","🐓","🪼","🦀","🪸","🐚","🦭","🦖","🦈","🦕","🦑","🦎","🐡","🐉","🦋"]
        for i in range (n):
            A = list(emoji_bank[n//2+1] for i in range(n))
            B.append(A)
        for k in range (n//2):
            for i in range(1+k,n-1-k):
                for j in range(1+k,n-1-k):
                    B[i][j] = emoji_bank[k]
    for b in B:
        for c in b:
            print(c, end="")
        print()
      
rug(9)       
