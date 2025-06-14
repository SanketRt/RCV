def calculate_rcv_winner(ballots):
    # Write your code here
    temp=[list(b) for b in ballots]
    c=set(c for b in temp for c in b)
    if not c: return None
    while True:
        cnt={}
        a=0
        for bt in temp:
            for x in bt:
                if x in c:
                    cnt[x]=cnt.get(x,0)+1
                    a+=1
                    break
        if a==0: return None
        for y,z in cnt.items():
            if z>a/2: return y
        for w in c:
            cnt.setdefault(w,0)
        mn=min(cnt[x] for x in c)
        elim=[x for x in c if cnt[x]==mn]
        if len(elim)==len(c): return None
        for e in elim: c.remove(e)