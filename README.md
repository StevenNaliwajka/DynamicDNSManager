# DynamicDNSManager
Dynamic DNS loader for my server stack.  
Only supports Godaddy.
Tough luck

-----------
Setup:  
1) run the following.
```angular2html
pip install -r /root/requirements.txt
python3 setup.py
```
2) fillout config.json
```angular2html
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
# Replace with your domain name
DOMAIN = "yourdomain.com"
# Assuming you are updating an A record
DNS_RECORD_TYPE = "A"
# Use "@" for root domain, or "subdomain" if updating a subdomain
DNS_RECORD_NAME = "@"
```
------------------

Implementation:  
Setup a cronjob to run every 10 min
1) open cron editor
```angular2html
crontab -e
```
2) add your cronjob at the bottom (update paths)
```angular2html
*/10 * * * * /usr/bin/python3 /path/to/script.py
```
3) save and exit.