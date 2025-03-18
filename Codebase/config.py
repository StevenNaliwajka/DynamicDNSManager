from Codebase.Pathing.get_config_file import get_config_file
from generic_file_io.json_manager.read_json import read_json


class Config:
    def __init__(self):
        self.api_key = None
        self.api_secret = None
        self.domain = None
        self.dns_record_type = None
        self.dns_record_name = None

        self.load_config()

    def load_config(self):
        config_file = get_config_file()
        self.api_key = read_json(str(config_file), 'api_key')
        self.api_secret = read_json(str(config_file), 'api_secret')
        self.domain = read_json(str(config_file), 'domain')
        self.dns_record_type = read_json(str(config_file), 'dns_record_type')
        self.dns_record_name = read_json(str(config_file), 'dns_record_name')