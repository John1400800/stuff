def countsProdAndComb(alphabet, count, condition):
    from itertools import product, combinations_with_replacement
    return (sum(map(condition, product(alphabet, repeat=count))),
            sum(map(condition, combinations_with_replacement(alphabet, count))))

if __name__ == "__main__":
    print(countsProdAndComb("abcd", 6, lambda tpl: tpl.count("b")-tpl.count("c")==2))
