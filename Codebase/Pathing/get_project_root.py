from pathlib import Path


def get_project_root():
    current_path = Path(__file__).resolve()
    parent_path = current_path.parents[2]
    return parent_path

if __name__ == '__main__':
    print(get_project_root())