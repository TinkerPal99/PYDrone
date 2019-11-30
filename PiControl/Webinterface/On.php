<html>
	<body>
		<div name ="body">
			<h2>PiControl</h2>
				<input id="button" type="submit" onclick="window.open('Off.php')" name="Aus" value="Deaktivieren" />

	<?php
	$datetime = date("Y/m/d") + " " + date("h:i:sa");
	$content = "Lizens ausgestellt am $datetime";

	$datei = fopen("Lizenzen/Modul1.txt","w");

        fwrite($datei, $content);
        fclose($datei);
       	echo ("Gestenkontrolle aktiviert");

	?>
		</div>
	</body>
</html>
