<html>
	<body>
		<div name ="body">
			<h2>PiControl</h2>
       			<input id="button" type="submit" onclick="window.open('On.php')"  name="An" value="Aktivieren" 	  />
				<input id="button" type="submit" onclick="window.open('Off.php')" name="Aus" value="Deaktivieren" />

		<?php
	$path = "../Lizenzen/"
	$datetime = date("Y/m/d") + " " + date("h:i:sa");
	$content = "Lizens ausgestellt am $datetime";
        if( isset ( $_REQUEST["An"]))

                {
	                $datei = fopen($path + "Modul1.txt","w");
	                fwrite($datei, $content);
		            fclose($datei);
			    
			    echo ("Lizenz wurde ausgestellt. ");
                }

        if( isset ( $_REQUEST["Aus"]))
                {
                	$unlink = unlink($path + "Modul1.txt");
        		echo ("Lizenz wurde entfernt.");
	        }

			?>
		</div>
	</body>
</html>
