import pathlib
import pwd
import grp
import stat
import argparse
import datetime



# def cmd_ls(pwd='./',para=''):
#     pwd = pathlib.Path(pwd)
#     if pwd.is_dir():
#         # for i in pwd.iterdir():
#         for i in pwd.glob('*'):
#             print(i)
#             #return(i)
# cmd_ls()

#help(pathlib)

## TODO -l 如何获取详细信息
## TODO 默认如何不显示隐藏文件
## TODO 多参数如何拼接



import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.accumulate(args.integers))