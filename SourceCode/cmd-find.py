import argparse
import glob
import pathlib
import grp


parser = argparse.ArgumentParser(description='This is python find command', prog='find')

parser.add_argument('-name',action='store',dest='name',type=str,help='find by file name')
parser.add_argument('-type',action='store',dest='type',type=str,help='find by file type')
parser.add_argument('-ctime',action='store',dest='ctime',type=str,help='find by file ctime')
parser.add_argument('-mtime',action='store',dest='mtime',type=str,help='find by file mtime')
parser.add_argument('-cnewer',action='store',dest='cnewer',type=str,help='find by file cnewer')
parser.add_argument('-executable',action='store',dest='executable',type=str,help='find by file executable')
parser.add_argument('-newer',action='store',dest='newer',type=str,help='find by file newer')
parser.add_argument('-gid',action='store',dest='gid',type=str,help='find by file gid')
parser.add_argument('-uid',action='store',dest='uid',type=str,help='find by file uid')
parser.add_argument('path',action='store',default='./',nargs='*')

args = parser.parse_args()
#print(args)


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


def _format(item: pathlib.Path) -> str:
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


def _name(name: str, path: pathlib.Path) -> str:
    pattern = path + '/' + name + glob.escape('.*')
    #print('pattern:',pattern)
    # for item in sorted(glob.glob('yield*')):
    for item in sorted(glob.glob(pattern)):
        print('bbbbbb')
        return 'finds item: {}'.format(item)

def _type():
    pass

def _ctime():
    pass

def _gid(item,attr_gid,args_gid=args.gid):
    #print('bbbbb,args.gid: {}'.format(args.gid))
    #print('kkkkkk,item:',item)
    #print('item: {item} {attr_gid} {args_gid}'.format(item,attr_gid,args_gid))

    item = item
    attr_gid = attr_gid
    args_gid = args_gid
    print("item: {item} {attr_gid} {args_gid}".format(item, attr_gid, args_gid))
    #yield from (x for x in pathlib.Path(i).iterdir() if args.gid == attr_gid)
    if args_gid == attr_gid:
        return item
    else:
        return

name = args.name

for i in args.path:
    # print(_name(name,str(i)))
    for m in pathlib.Path(i).iterdir():
        #print('all the file: {}'.format(m))
        st = m.stat()
        attr = {
            'gid': st.st_gid,
            'uid': st.st_uid,
            'atime': st.st_atime
        }
        #if args.gid:
        print(_gid(m,attr['gid']))
        # if args.uid:
        #     print(_uid(m, attr['uid']))

