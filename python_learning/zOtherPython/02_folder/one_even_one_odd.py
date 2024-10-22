if __name__ == "__main__":
    numbers = tuple(int(input()) for _ in range(3))
    print("YES" if all(map(lambda func: any(filter(func, numbers)), (lambda n: n%2+1, lambda n: n%2)))
                else
          "NO")
