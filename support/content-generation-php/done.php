<?php

if ($SESSION_['debug'] == 1) {

$display = "display:block;";

} else {

$display = "display:none;";

}

unset($SESSION_['debug']);

?>

<html>

<body>

<p>
Congrats! You have cleared the text file. Restart the process? (New folders.txt will be loaded)
<br>
<a href="physcomp2.php">RESET</a><br />
________________________________<br />
Dev Tools<br />
<a href="physcomp.php">RESET 2</a>
<a href="physcompdebug.php">Developer RESET</a>
</p>

</body>

</html>