import random
def main(e, es, ef):
    n = 0
    d = []
    s = random.randrange(25, 225)
    while n < 100000:
        max_weight = [25]
        weight = random.randrange(max_weight[-1], 225)
        counter = e
        while counter > 0:
            if s > weight:
                counter -= es
                max_weight.append(weight)
                weight = random.randrange(max_weight[-1], max(int(max_weight[-1] * 1.5), 225))
            else:
                counter -= ef
                weight = random.randrange(max_weight[-1], weight)
    
        d.append(s - max_weight[-1])
        n += 1
    print(sum(d) / len(d))
    
    
    
    
    

# Code is already compliant with Codon rules.
e = 10
es = 2
ef = 3
main(e, es, ef)
