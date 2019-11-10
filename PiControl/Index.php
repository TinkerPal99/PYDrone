
<div id="body">  <br><br><br><br>

	<form>
        <input id="button" type="submit" name="RPS7" value="start gesture control" />
        <input id="button" type="submit" name="RPS6" value="stop gesture control" />
	<br><br><br>


<p id="output" align="center">
<?php
	$state = "Mark 1 is ready";
        if( isset ( $_REQUEST['RPS7']))
                {
                $inhalt = "start\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
                }
        if( isset ( $_REQUEST['RPS6']))
                {
                $inhalt = "stopp\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
                }
?>
</body>
