
def rec_dfc(G, s, S=None):
    if S is None:S = set()
    S.add(s)
    for u in G[s]:
        if u in S:continue
        rec_dfc(G, u, S)

def iter_dfs(G,s):
    S,Q=set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:continue
        S.add(u)
        Q.extend(G[u])
        yield u


if __name__=="__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    G = [{b,c,d,e,f},
        {c, e},
         {d},
         {e},
         {f},
         {c,g,h},
         {f,h},
         {f,g}
         ]
    print(list(iter_dfs(G,a)))