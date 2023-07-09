#encoding utf-8
import random
import base64



keys = ['!','@','#','$','%','^','&','*','+','(',')','<','>','/','?','{','}','[',']','\\','.',' ','=','-','_','|',':',';']

def xor2(string:str):
    left, right = '', ''
    for s in string:
        key = random.choice(keys) if s not in keys else random.choice([chr(n) for n in range(97, 114)])
        while (ord(s) ^ ord(key) < 31):
            key = random.choice(keys) if s not in keys else random.choice([chr(n) for n in range(97, 114)])
        else:
            left += key
            right += chr(ord(s) ^ ord(key))
    return ("\""+left+"\""+"^"+"\""+right+"\"").replace('\\','\\\\')

def xor2_a(string:str):
    left, right = '', ''
    for s in string:
        key = random.choice(keys) if s not in keys else random.choice([chr(n) for n in range(97, 114)])
        while (ord(s) ^ ord(key) < 31):
            key = random.choice(keys) if s not in keys else random.choice([chr(n) for n in range(97, 114)])
        else:
            left += key
            right += chr(ord(s) ^ ord(key))
    return left,right

def xorN(string:str,nums:int):
    right,res = string,[]
    for n in range(nums-1):
        left,right = xor2_a(right)
        res.append(left)

    res.append(right)
    res = '"'+'"^"'.join(res)+'"'
    res.replace("\\","\\\\")

    return res

def xor2_base64_a(string:str):
    left,right = xor2_a(string)
    left,right = base64.b64encode(left.encode('utf-8')),base64.b64encode(right.encode('utf-8'))
    return (left.decode('utf-8'),right.decode('utf-8'))

def xor2_base64(string:str):
    left,right = xor2_base64_a(string)
    return 'base64_decode("'+left+'")^base64_decode("'+right+'")'

def zeroPadding(data):
    data += b'\x00'
    while len(data) % 16 != 0:
        data += b'\x00'
    return data

def outOfPadding(data):
    return data.replace('\x00','')

# def aes_encrypt(data,key):
#     data = zeroPadding(data.encode('utf-8'))
#     cipher = zeroPadding(key.encode('utf-8'))
#     cipher = AES.new(cipher,mode=AES.MODE_ECB)
#     print(cipher.encrypt(data))
#     res = base64.encodebytes(cipher.encrypt(data))
#
#     return res.decode('utf-8')
#
# def aes_decrypt(data,key):
#     data = base64.decodebytes(data.encode('utf-8'))
#     cipher = zeroPadding(key.encode('utf-8'))
#     cipher = AES.new(cipher,mode=AES.MODE_ECB)
#     res = cipher.decrypt(data)
#     return outOfPadding(res.decode('utf-8'))
#

aes_with_magic = """

 function Decrypt($data)
    {
        $key="e45e329feb5d925b"; //该密钥为连接密码32位md5值的剿16位，默认连接密码rebeyond
        $magicNum=hexdec(substr($key,0,2))%16; //取magic tail长度
        $data=substr($data,0,strlen($data)-$magicNum); //截掉magic tail
        return openssl_decrypt(base64_decode($data), "AES-128-ECB", $key,OPENSSL_PKCS1_PADDING);
    }
"""
