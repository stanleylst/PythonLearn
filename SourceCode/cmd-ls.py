import argparse
import pathlib
import stat
import pwd
import grp
import datetime

parser = argparse.ArgumentParser(prog='ls',add_help=False,description='sum the integers at the command line')

parser.add_argument('-a',action='store_true',default=False,dest='all')
parser.add_argument('-l',action='store_true',default=False,dest='long')
parser.add_argument('-h',action='store_true',default=False,dest='human')
parser.add_argument('path',action='store',default='.',nargs='*')

args = parser.parse_args()

def scan(path: str) -> pathlib.Path:
    #pwd = pathlib.Path(args.path)
    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))


def size_setup(size: int) -> str:
    if not args.human:
        return size
    units = ['','K','M','G','T','P','E']
    idx = 0
    while size/1024 > 1:
        size /= 1024
        idx += 1
    return '{}{}'.format(round(size,1),units[idx])


def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp(mtime)
    return '{:>2} {:>2} {:>2}:{:>2}'.format(dt.month, dt.hour, dt.hour, dt.minute)

def _format(item: pathlib.Path) -> str:
    if not args.long:
        return item
    st = item.stat()
    arg = {
        'mode': stat.filemode(st.st_mode),
        'links': st.st_nlink,
        'owner': pwd.getpwuid(st.st_uid).pw_name,
        'group': grp.getgrgid(st.st_gid).gr_name,
        'size': size_setup(st.st_size),
        'mtime': time_format(st.st_mtime)
    }

    return '{mode} {links} {owner} {group} {size} {mtime}'.format(**arg)

for i in args.path:
    #print(i)
    for item in scan(i):
        #print(item)
        print(_format(item))




