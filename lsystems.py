import types

def result_to_list(result, default):
    if isinstance(result, list):
        return result
    elif isinstance(result, tuple):
        return list(result)
    elif isinstance(result, types.NoneType):
        return [default]
    else:
        return [result]


def Rule(cf):
    symbol = cf.__name__ #gets the name of the rule
    
    def wrapper(*args):
        # TODO: support kwargs
        continuation = lambda: result_to_list(
            cf(*args), 
            wrapper(*args)
        )
        # added for pretty printing
        continuation.pretty = "%s(%s)" % (symbol, ",".join(map(str, args)))
        return continuation

    return wrapper

def expand(terms, iterations):
    if not isinstance(terms, list):
        terms = [terms]

    for i in xrange(iterations):
        newterms = []
        for t in terms:
            newterms.extend(t())
        terms = newterms

    return terms
