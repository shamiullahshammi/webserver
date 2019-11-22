Simple application using python SQLite3 database with html templating.

Install the requirements in Yocto
	1)SQLLITE3
	2)FLASK

BEfore Run Application
	1)
		echo 46 > /sys/class/gpio/export
		echo out >/sys/class/gpio/gpio46/direction
		echo 0 >/sys/class/gpio/gpio46/value
	2)change Ip Address in Application of python file 
		    app.run(host="192.168.1.143",debug=True,port=8050)          
	
	3)give permission 
		chmod -R 777 app.py
	
		python app.py
```
