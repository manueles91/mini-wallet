"""v2 sAERO allocator model (mirrors Mini Wallet Allocator.kt 13.41).
Forecast fees/day = BLEND*fees24h + (1-BLEND)*fees96h; pools with fees24h==0 are not targets.
Allocation: our v in a pool earns R*v/(W+v), W = pool weight minus our own votes; fine-step greedy on marginal $
(concave -> optimal up to one step), at most MAX_GAUGES gauges per position, no per-pool cap."""
BLEND=0.5; STEPS=100; MAX_GAUGES=4
def earn(r,e,v): return r*v/(e+v) if v>0 and e+v>0 else 0.0
def fee_forecast(g): return BLEND*(g.get('fees24hUsdPerDay') or 0)+(1-BLEND)*(g.get('feesUsdPerDay') or 0)
def eligible(g): return (g.get('fees24hUsdPerDay') or 0)>0
def allocate(P,VP,steps=STEPS,maxg=MAX_GAUGES):
    """P: key->(reward $ over window, others' weight excl. ours). Returns key->votes."""
    pl={}; step=VP/steps
    for _ in range(steps):
        ks=list(pl) if len(pl)>=maxg else list(P)
        k=max(ks,key=lambda k:earn(P[k][0],P[k][1],pl.get(k,0)+step)-earn(P[k][0],P[k][1],pl.get(k,0)))
        pl[k]=pl.get(k,0)+step
    return pl
