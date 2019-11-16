<html>
<body>
<h2>Module</h2>
       		<input id="button" type="submit" name="ON" value="Aktivieren" 	 />
		<input id="button" type="submit" name="OFF" value="Deaktivieren" />

<?php
	$datetime = date("Y/m/d") + " " + date("h:i:sa");
	$content = "Lizens ausgestellt am $datetime";
        if( isset ( $_REQUEST["ON"]))
			 $datei = fopen("Lizenzen/Modul1.txt","w");

                        fwrite($datei, $content);
                        fclose($datei);
                        echo ("Hello");

                {
	                $datei = fopen("Lizenzen/Modul1.txt","w");

	                fwrite($datei, $content);
		        fclose($datei);
			echo ("Hello");
                }

        if( isset ( $_REQUEST["OFF"]))
                {
                	$unlink = unlink("Lizenzen/Modul1.txt");
        		echo ("Hello");
        }

?>
</body>
</html>
