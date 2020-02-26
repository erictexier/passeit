#!/usr/bin/php
<?php
while(1)
{
	echo "Entrez un nombre: ";
	$line = trim(fgets(STDIN));
	if (feof(STDIN) == TRUE)
		exit();
	if (!is_numeric($line))
	{
		echo  $line. ' n\'est pas un chiffre';
		echo "\n";
	}
	else
	{
		echo 'Le nombre '.$line.' est ';
		if ($line % 2 == 1)
		{
			echo  "Impair\n";
		}
		else
		{
			echo "Pair\n";
		}
	}
}
?>
