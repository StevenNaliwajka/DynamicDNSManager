import requests


def update_godaddy_dns(config, new_ip):
    url = f"https://api.godaddy.com/v1/domains/{config.domain}/records/{config.dns_record_type}/{config.dns_record_name}"
    headers = {
        "Authorization": f"sso-key {config.api_key}:{config.api_secret}",
        "Content-Type": "application/json",
    }
    data = [{"data": new_ip, "ttl": 600}]
    response = requests.put(url, json=data, headers=headers)
    return response.status_code == 200
