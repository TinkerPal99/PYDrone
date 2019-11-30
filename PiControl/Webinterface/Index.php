<html>
	<body>
		<div name ="body">
			<h2>PiControl</h2>
       				<input id="button" type="submit" onclick="window.open('On.php')"  name="An" value="Aktivieren" 	 />
				<input id="button" type="submit" onclick="window.open('Off.php')" name="Aus" value="Deaktivieren" />

		<?php
	$datetime = date("Y/m/d") + " " + date("h:i:sa");
	$content = "Lizens ausgestellt am $datetime";
        if( isset ( $_REQUEST["An"]))

                {
	                $datei = fopen("../Lizenzen/Modul1.txt","w");

	                fwrite($datei, $content);
		        fclose($datei);
			echo ("Hello");
                }

        if( isset ( $_REQUEST["Aus"]))
                {
                	$unlink = unlink("../Lizenzen/Modul1.txt");
        		echo ("Hello");
	        }

			?>
		</div>
	</body>
</html>
