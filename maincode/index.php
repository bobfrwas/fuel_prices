<?php
$myfile = fopen("lowest_price.txt", "r") or die("Unable to open file!"); 
echo "The lowest price for fuel from Asda is ";
echo fread($myfile,filesize("lowest_price.txt"));
fclose($myfile);
