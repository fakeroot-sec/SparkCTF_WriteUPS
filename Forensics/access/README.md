
# Access challenge write-up 

## First you need to search in the file 
	- this command will make it easier for you to go directly to the attended string
	- it will also url  decoded it  
	 cat access.log.ctf |grep String |cut -d'=' -f4 > codedUrl &&hURL -ul -f codedUrl |cut -d, -f2-22 > decodedUrl
	
## Second you need to run the javascript code 
	- the result of the url decoded string is a javascript code
	- Use any compiler online or use your own browser 
	console.log it 
	- you  will get the flag but with something wrong 
## Third filter the flag string 
	-by removing unecessary caracter 
	- the added caracter are in the third word 
		3neougnon change it to 3nough
	- and you will get the flag Spark{theString}
## Challenge solved
	
