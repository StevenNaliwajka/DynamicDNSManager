from Codebase.Pathing.get_config_folder import get_config_folder


def get_config_file():
    config_folder = get_config_folder()
    return config_folder / "config.json"