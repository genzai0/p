a,b,c,d,e = 0,0,0,0,0
res = []
for b in range(1,15):
    for c in range(1,15):
        for d in range(1,15):
            for e in range(1,15):
                if ((b**3+c**3)-(d**3+e**3))==0 and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                    if (b**3+c**3) not in res:
                        res.append(b**3+c**3)
else:
    print(res)

