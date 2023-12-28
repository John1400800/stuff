def reverse():
    with (open('input.dat', 'rb') as inp,
          open('output.dat', 'wb') as out):
        out.write(inp.read()[::-1])

reverse()