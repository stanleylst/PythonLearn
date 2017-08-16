import argparse
import pathlib
import pwd
import grp
import stat
import datetime

parser = argparse.ArgumentParser(description='This is python ls command', prog='ls', add_help=False)

parser.add_argument('-a', action="store_true", dest='all', default=False, help='-a help')
parser.add_argument('-h', action='store_true', dest='human', default=False, help='-H help')
parser.add_argument('-l', action='store_true', dest='long', default=False, help='-l help')
# parser.add_argument('-path',nargs='2',default='.')
parser.add_argument('path', nargs='*', default='.')

args = parser.parse_args()


def scan(path: str) -> pathlib.Path:
    # for item in  pathlib.Path(path).iterdir():
    # 	yield item
    # TODO , yield from 函数没搞明白什么意思
    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))
	#return (x for x in pathlib.Path(path).iterdir())


def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp(mtime)
    return '{:>2} {:>2} {:>2}:{:>2}'.format(dt.month, dt.hour, dt.hour, dt.minute)


def size_setup(size: int) -> str:
    if not args.human:
        return str(size)
    units = ['', 'K', 'M', 'G', 'T', 'P', 'E']
    idx = 0
    while size > 1024:
        size /= 1024
        idx += 1
    return '{}{}'.format(round(size, 1), units[idx])


def format(item: pathlib.Path) -> str:
    if not args.long:
        return item.name
    st = item.stat()

    attr = {
        'mode': stat.filemode(st.st_mode),
        'links': st.st_nlink,
        'user': pwd.getpwuid(st.st_uid).pw_name,
        'group': grp.getgrgid(st.st_gid).gr_name,
        'size': size_setup(st.st_size),
        'mtime': time_format(st.st_mtime),
        'name': item.name
    }
    return '{mode} {links} {user} {group} {size} {mtime} {name}'.format(**attr)


def main():
    if isinstance(args.path, list):
        for path in args.path:
            print('{}:'.format(path))
            for item in scan(path):
                print(format(item))
            print()
    else:
        for item in scan(args.path):
            print(format(item))


main()

# def scan():
# 	pwd = pathlib.Path(results.path)
# 	def _a():
# 		for i in pwd.iterdir():
# 			print(i)
# 	def _h():
# 		for i in pwd.iterdir():
# 			print('human output: {}',format(i))
# 	def _l():
# 		for i in pwd.iterdir():
# 			print('long output: {}',format(i))
#
# scan()
