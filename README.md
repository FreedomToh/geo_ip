
# Deploy  
  
1) download last database BIN file from https://lite.ip2location.com/database-download and unzip to ./db  
2) add variables to .env file at project's root  
	- **PORT**  
	- **DB_PATH**  as path to db in (1)
	- **AUTH_SERVER** or set variable **NEED_AUTH**=False  
3) docker-compose up -d --build

# Endpoints
- /ip_info/**195.238.246.203**/

> **Headers** (If auth is enabled): 

    Authorization: {prefix} {token}

> **Response**

    {
	    "ip":  "217.118.87.98", 
	    "country":  "Russian Federation", 
	    "region":  "Moskva", 
	    "city":  "Moscow"
	}