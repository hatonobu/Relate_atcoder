def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    # 制約がai <= 2**60なので
    for d in range(61):
        # d桁目ごとに考える
        x = 0
        for a in A:
            if (a >> d) & 1:
                x += 1
        ans += x * (n-x) * 2**d
    print(ans)

if __name__ == '__main__':
    main()