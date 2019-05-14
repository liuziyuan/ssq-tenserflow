import yaml
import os

def get_config_yaml(file_name='config.yml'):
    # project_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.join(os.getcwd())
    yaml_path = os.path.join(project_dir, file_name)
    yaml_file_stream = open(yaml_path, 'r', encoding='utf-8')
    return yaml.load(yaml_file_stream)



