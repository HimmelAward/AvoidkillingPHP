# AvoidkillingPHP
免杀PHP木马生成器
## 查杀效果
### VT查杀 0/58
![微信截图_20230707203828](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/1000d855-fffb-422c-8942-4cab4fd9cdf5)
### 微步查杀 0/24
![微信截图_20230707203936](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/bb721c31-27a4-456f-b325-f3ffe20c081d)
![微信截图_20230707204118](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/adbca13e-edad-4473-8e5b-17099a8d939f)
### Virscan查杀 0/46
![微信截图_20230707205321](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/d33dfb28-a212-48ce-b57b-0392236208c7)
### 使用aes加混淆的webdir+无法查杀
![微信截图_20230708094528](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/7b506633-efd7-40ad-92e0-58654252e517)
### 使用inject的木马河马webshell无法查杀
![微信截图_20230708094448](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/a5db1485-b26f-4b65-be19-83f4c073f466)
## 安装
python 方式
`pip install -r requirements.txt`
## 用法
连接的url需要密码<br>
一般木马的密码为2，behinder的密码为默认的rebeyond<br>
同时在get请求设置了校验<br>
http://127.0.0.1/html/webshell/injectaes_xor2_3.php?1=admin<br>
这里设置的是一个GET请求1=admin的验证<br>
如果不是返回404，防止被非上传webshell人员发现<br>
![1688955122815](https://github.com/Z0fhack/AvoidkillingPHP/assets/66540608/994b2555-a5e5-4522-b473-1b31211c0e91)
**`-type` 选择webshell的类型**:<br>
default  蚁剑，菜刀，哥斯拉都可以连接<br>
default_for_aes aes加密并混淆过的webshell<br>
behinder  冰蝎可以连接<br>
behinder_for_aes aes加密并混淆过的webshell<br>
inject 不直接执行命令，向注入木马<br>
inject_for_aes 对inject的混淆<br>
**`-e `选择加密类型**：<br>
xor2  xor2加密方式`")[&/-]"^"H(UJ_)" === assert`<br>
xorN xorN加密方式对其xor拆分多次加密`"%#/@ <"^"#!ak}:"^"*\i*d("^"{q|\)#"^"@co\>#"^"v?Gd\Z" === assert`，需要指定-n 加密次数<br>
xor2_base64  综合base64加密 `base64_decode("KD87Xl8o")^base64_decode("SUxIOy1c") === assert`<br>
**`-name` webshell的名字可以输入多个**<br>
**`-target` inject需要 注入的目标文件默认为index.php 被注入的页面可以被behinder连接**<br>
**`-n` xorN的次数**<br>
**`-all` 生成默认所有webshell**<br>
