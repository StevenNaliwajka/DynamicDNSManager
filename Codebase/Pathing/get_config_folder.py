from Codebase.Pathing.get_project_root import get_project_root


def get_config_folder():
    root = get_project_root()
    return root / "Config"