#!/usr/local/bin/php
<?php
## Converts a xml file to json
#
$xml_file = $argv[1]; # Gets the first parameter set by the CLI ($arg[0] is the name of this script ie converter.php)
$xml_string = simplexml_load_file($xml_file);
$json_conversion = json_encode($xml_string, JSON_UNESCAPED_UNICODE); # The flag prevents char encoding issues
$file_name = pathinfo($xml_file, PATHINFO_FILENAME); # Gets the file name without the extension
$destination_path = $argv[2]; 
file_put_contents($destination_path.$file_name.".json", $json_conversion);
?>
