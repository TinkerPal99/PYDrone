# PYDrone V1.0
**Repository for Pydrone Project, running on RPI, coded in Python** <br>
**Author :** TinkerPal99 <br>
**Start of project on github:** 12.10.2019 <br>
Contributors:<br>
**Documentation can be found right here :** https://github.com/TinkerPal99/PYDrone/blob/master/Doku/html/index.html


__*Summary*__
1. First things First 
2. Preparation
3. Important informations


__First things First__

Dies ist eine Kontrollsoftware für verschiedene Dronen, Rover und ähnliches. 
Basierend auf einem RPI, und programmiert in Python.
Die tatsächliche init kann unter _main/py-scripts_ gefunden werden.
Das Webinterface kann in _/main_ gefunden werden und heißt _Index.php_.


__Preparation__

Für die Nutzung des Webinterface benötigt das Pi php und apache. Setup wird erstellt.

**Für Apache und PHP**

1. sudo apt-get install apache2
2. sudo apt-get install -t stretch php7.0 php7.0-curl php7.0-gd php7.0-fpm php7.0-cli php7.0-opcache php7.0-json php7.0-mbstring php7.0-xml php7.0-zip php7.0-mysql -y
3. sudo apt-get install -t stretch libapache2-mod-php7.0 -y

**Für Anbindung der library für DHT11 und DHT22 (Temperatur-&Luftfeuchtigkeitssensor)**

1. sudo apt-get install build-essential python-dev python-openssl git
2. git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
3. sudo python setup.py install

**Webinterface Schreibrechte erteilen**

Und damit das Webinterface in die Joblist schreiben und Zertifikate erstellen kann, 
müssen die entsprechenden Teile für den www-user freigegeben werden, beispielsweise so:
1. sudo chown -r -s www-data  /var/www/html/*

__Important informations__


Im Moment versuche ich das ganze objektorientiert neu aufzubauen, erste Versuche können 
in _main/py-scripts/PiTank.py_ und _autonomousDrive.py_ gefunden werden.
