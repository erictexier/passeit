<?php
function ft_split($s1)
{
	$tab = explode(" ", $s1);
	
	sort($tab);
	return($tab);
}

?>
