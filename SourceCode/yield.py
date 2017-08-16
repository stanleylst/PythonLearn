def read():
    for i in range(5):
        yield '<< %s' % i
        #print('<< {}'.format(i))

def reader_wrapper(g):
    yield from g

wrap = reader_wrapper(read())

for m in wrap:
    print(m)

# def wrap_read(g):
#     for k in g:
#         #print(k)
#         yield k
#
# wrap = wrap_read(read())
#
# for m in wrap:
#     print(m)