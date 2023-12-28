# def total(lst):
#     for s in lst:
#         lst_s = s.split()
#         yield float(lst_s[2]) * float(lst_s[1])


with (
        open('prices.txt', 'r', encoding='utf-8')
        as f_prices):
    # print('{:.2f}'.format(sum(total(f_prices))))
    # f_prices.seek(0)
    print('{:.2f}'.format(
        sum((float(s.split()[2]) * float(s.split()[1]) for s in f_prices))))
