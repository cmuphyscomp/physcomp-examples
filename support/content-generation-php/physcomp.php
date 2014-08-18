<?php session_start();

$lines = file("folders.txt", FILE_IGNORE_NEW_LINES);

$count = count($lines);


if (!isset($_SESSION['max'])){

	$_SESSION['max'] = $count;
	$_SESSION['max'] -=3;
	
}

if (!isset($_SESSION['counter'])){

	$_SESSION['counter'] = 0;
	$tally = $_SESSION['counter'];
	
}elseif ($_SESSION['counter'] >= $_SESSION['max']){

	unset($_SESSION['counter']);
	unset($_SESSION['max']);
	header("Location: http://nascent-rdo.org/cmu/done.php");
	
}else{
	
	$_SESSION['counter'] += 3;
	$tally = $_SESSION['counter'];
	
}

$one = $tally;

$two = $tally+=1;

$three = $tally+=1;

$identif = substr($lines[$one], 0, -5);

$firsturl = $identif . "/" . $lines[$one];

$secondurl = $identif . "/" . $lines[$two];

$thirdurl = $identif . "/" . $lines[$three];

?>

<html>
<body>
<div style="width:50%; margin: 0 auto;">

<p style="text-align:center;"><strong>You are currently viewing:  </strong><?php echo $identif ?></p>

<br />

<textarea rows="20" cols="100" readonly>

<iframe id="assignment-html" onload="resizeIframe(this)" width="100%" frameborder="0" src="http://htmlpreview.github.io/?https://raw.githubusercontent.com/cmuphyscomp/physcomp-examples/master/1_energy-information-transduction/a_basic-circuits/i_ohm/<?php echo $firsturl; ?>" width="960" height="800"></iframe>	 	 

<img id="assignment-image" class="alignnone" src="https://raw.githubusercontent.com/cmuphyscomp/physcomp-examples/master/1_energy-information-transduction/a_basic-circuits/i_ohm/<?php echo $secondurl; ?>" width="960" height="%100" />

<img id="assignment-image" class="alignnone" src="https://raw.githubusercontent.com/cmuphyscomp/physcomp-examples/master/1_energy-information-transduction/a_basic-circuits/i_ohm/<?php echo $thirdurl; ?>" alt="" width="960" height="%100" />

<a id="assignment-backlink" href="http://physcomp.org/assignments/1-energy-information-transduction/a-basic-circuits-overview/">Assignments: Basic Circuits</a>

</textarea>
</div>
</body>

</html>