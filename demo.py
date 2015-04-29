from lsystems import Rule, expand

@Rule
def F(x, y):
    if x > 0:
        return F(x-1, y+1), G(x)

# rules return a comma-separated list of other rules
@Rule
def G(x):
    if x > 0:
        return push(), G(x-1), pop()
    return

# terminals should return nothing
@Rule
def push():
    pass

@Rule
def pop():
    pass
    
        
if __name__ == "__main__":
    # expand takes an axiom and a depth parameter
    result = expand(F(2,0), 3)
    s = map(lambda x: x.pretty, result)
    print s

#22
