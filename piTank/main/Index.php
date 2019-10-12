
<head>
	<title>
	</title>
	<link rel="stylesheet" href="layout.css" >
</head>
<body>

	<div id="headOfBody">
		</img id="logo" src="Bilder/TestLab-Logo_transparent.png" height="115" width="125" ></a>
		<h1><BLOCKQUOTE><BLOCKQUOTE>---------</BLOCKQUOTE></BLOCKQUOTE> </h1>
		<h2><BLOCKQUOTE>PiDrone</BLOCKQUOTE></h2>
	</div>

	<div id="upperNav"><br>
		<a href="Index.php"><span id="button">PiDrone1</span></a>               <a href="index.html"><span id="button">Image-Page</span></a>
	</div>

<div id="body">  <br><br><br><br>

	<form>
        <input id="button" type="submit" name="RPS7" value="Full Speed" />
        <input id="button" type="submit" name="RPS6" value="Half Speed" />
	<br><br><br>
	<input id="button" type="submit" name="RPS1" value="Forward" />
	<br><br><br>
        <input id="button" type="submit" name="RPS3" value="Leftturn" />
        <input id="button" type="submit" name="RPS2" value="Stop driving" />
        <input id="button" type="submit" name="RPS4" value="Rightturn" />
	<br><br><br>
        <input id="button" type="submit" name="RPS5" value="Backward" />

	<br><br><br>
	<a href="senselog.txt" target="_blank"><span id="button">Sensorlog</span></a>
	<br><br><br>
	<br><br><br>
	<a href="purge.php" target="_blank"><span id="button">Delete complete Query, only in case of emergency</span></a>
<br><br><br><br>

<p id="output" align="center">
<?php
	$state = "Mark 1 is ready";
        if( isset ( $_REQUEST['RPS1']))
                {
                $inhalt = "RPS1\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
                $state = "Moving forward";
                }
        if( isset ( $_REQUEST['RPS2']))
                {
                $inhalt = "RPS2\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
		$state = "Stopped";
                }
        if( isset ( $_REQUEST['RPS3']))
                {
                $inhalt = "RPS3\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
                $state = "Turning left";
 		}
        if( isset ( $_REQUEST['RPS4']))
                {
                $inhalt = "RPS4\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
		$state = "Turning right";
                }
        if( isset ( $_REQUEST['RPS5']))
                {
                $inhalt = "RPS5\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
		$state = "Moving backward";
                }
        if( isset ( $_REQUEST['RPS6']))
                {
                $inhalt = "RPS6\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
                $state = "Half Speed";
                }
        if( isset ( $_REQUEST['RPS7']))
                {
                $inhalt = "RPS7\n";

                file_put_contents("test.txt", $inhalt, FILE_APPEND);
                $state = "Full Speed";
                }


	echo $state;
?>
</p>
<p>
<h2>Module</h2>
       Modul 1  <input id="button" type="submit" name="Modul1" value="Aktivieren"  /> <input id="button" type="submit" name="Modul1_OFF" value="Modul 1 deaktivieren" />
        <br><br><br>
       Modul 2 <input id="button" type="submit" name="Modul2" value="Aktivieren" />   <input id="button" type="submit" name="Modul2_OFF" value="Modul 2 deaktivieren" />
        <br>

</p>
<p id="output" align="center">
<?php
	$datetime = date("Y/m/d") + " " + date("h:i:sa");
        $License = " ";
	$content = "Lizens ausgestellt am $datetime";

        if( isset ( $_REQUEST['Modul1']))
                {
                $datei = fopen("Lizenzen/Modul1.txt","w");

                fwrite($datei, $content);
		fclose($datei);
                $License = "Modul 1 Lizenz - aktiv";
                }
        if( isset ( $_REQUEST['Modul2']))
                {
                $datei = fopen("Lizenzen/Modul2.txt","w");

                fwrite($datei, $content);
		fclose($datei);
                $License = "Modul 2 Lizenz - aktiv";
                }

        if( isset ( $_REQUEST['Modul1_OFF']))
                {
                $unlink = unlink('Lizenzen/Modul1.txt');
                $License = "Modul 1 Lizenz entzogen: $unlink";
                }
        if( isset ( $_REQUEST['Modul2_OFF']))
                {
                $unlink = unlink('Lizenzen/Modul2.txt');
                $License = "Modul 2 Lizenz entzogen: $unlink";
                }

                echo $License;

?>

</p>
</div>
<iframe src="senselog.txt" width="21%" id="log1">
<iframe src="senselog.txt" width="25%" id="log2">
</body>
</html>
