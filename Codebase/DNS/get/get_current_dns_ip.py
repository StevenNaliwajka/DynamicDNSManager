import requests


def get_current_dns_ip(config):
    url = f"https://api.godaddy.com/v1/domains/{config.domain}/records/{config.dns_record_type}/{config.dns_record_name}"
    headers = {"Authorization": f"sso-key {config.api_key}:{config.api_secret}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()[0]["data"]
    return None
