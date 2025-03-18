from Codebase.DNS.get.get_current_dns_ip import get_current_dns_ip
from Codebase.DNS.get.get_public_ip import get_public_ip
from Codebase.DNS.set.set_godaddy_dns import update_godaddy_dns
from Codebase.config import Config

if __name__ == "__main__":

    config = Config()

    public_ip = get_public_ip()
    dns_ip = get_current_dns_ip()

    if dns_ip and public_ip != dns_ip:
        if update_godaddy_dns(config, public_ip):
            print(f"Updated DNS: {dns_ip} -> {public_ip}")
        else:
            print("Failed to update DNS.")
    else:
        print("No update needed.")