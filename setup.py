from generic_file_io.core.generic_create_folder import generic_create_folder
from generic_file_io.json_manager.write_json import write_json

from Codebase.Pathing.get_config_folder import get_config_folder

def setup():
    config_folder = get_config_folder()

    generic_create_folder(config_folder)

    json_data = {
        "API_KEY": "",
        "API_SECRET": "",
        "DOMAIN": "",
        "DNS_RECORD_TYPE": "",
        "DNS_RECORD_NAME": ""
    }

    config_path = config_folder / "config.json"
    write_json(config_path, json_data, True)

if __name__ == "__main__":
    setup()
