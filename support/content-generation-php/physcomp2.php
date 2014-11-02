<?php session_start();

$lines = file("folders.txt", FILE_IGNORE_NEW_LINES); 	//loads folders.txt into an array and removes the linebreaks

$count = count($lines); 	//counts the number of lines in folders to determine the max below


if (!isset($_SESSION['max'])){

	$_SESSION['max'] = $count;
	$_SESSION['max']--;		//this is done because array values start at 0
	
}

if (!isset($_SESSION['counter'])){ //no while loop, not sure it would work here due to needing each iteration displayed

	$_SESSION['counter'] = 0;
	$tally = $_SESSION['counter'];
	
}elseif ($_SESSION['counter'] >= $_SESSION['max']){

	unset($_SESSION['counter']);
	unset($_SESSION['max']);
	header("Location: http://nascent-rdo.org/cmu/done.php"); //once we're done iterating we're sent to the done page
	
}else{
	
	$_SESSION['counter'] += 1;
	$tally = $_SESSION['counter'];
	
}

$identif = substr($lines[$tally], 0, -5);

$filepath = "1_energy-information-transduction/b_arduino-starter/ii_basic-examples/" . $identif . "/";

/* I was changing the filepath above manually for each set of folders, 
my initial idea was to set up a simple lookup table with urls but I 
realize now there's no need if I can get a text file that searches 
for html files only and includes their path starting from /1_energy-.... */

$firsturl = $filepath . $lines[$tally]; //each of these creates the unique file name with the appropriate extension

$secondurl = $filepath . $identif . "_bb.png";

$thirdurl = $filepath . $identif. "_schem.png";

?>

<html>
<body>
<div style="width:50%; margin: 0 auto;">

<p style="text-align:center;"><strong>You are currently viewing:  </strong><?php echo $identif ?></p> <!-- at a glance, what activity you're on -->

<br />

<textarea rows="20" cols="100" readonly> <!-- this creates a boxed area for the html, which cannot be edited. handy -->

<iframe id="assignment-html" onload="resizeIframe(this)" width="100%" frameborder="0" src="http://cmuphyscomp.github.io/physcomp-examples/<?php echo $firsturl; ?>" width="960" height="800"></iframe>	 	 

<img id="assignment-image" class="alignnone" src="http://cmuphyscomp.github.io/physcomp-examples/<?php echo $secondurl; ?>" width="960" height="%100" />

<img id="assignment-image" class="alignnone" src="http://cmuphyscomp.github.io/physcomp-examples/<?php echo $thirdurl; ?>" width="960" height="%100" />

</textarea>
</div>
</body>

</html>