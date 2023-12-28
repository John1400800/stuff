from mainfoo import foo


if __name__ == '__main__':
    with (open('input.txt', 'r') as inpf,
          open('output.txt', 'w') as outf):
        # print(foo(inpf))

        res = foo(inpf)
        for i in res:
            # print(i[0], i[1], i[2], sep='\n', end='\n\n')
            outf.write('\n'.join([i[0] for i in i[1]]) + '\n')
            outf.write('----------\n')
            outf.write(f'Summary: {i[2]}\n\n')
