import yaml
import json


def read_JSON(filePath):
    with open(filePath, 'r') as template:
        data = json.load(template)
    return data


def read_YAML_from_config():
    filename = '/Users/dipanjankundu/Mindtickle_Projects/mindtickle-performance-testing-locust/config/mobile_load_test.yml'
    print('yaml file: {}'.format(filename))
    yaml_data = None
    with open(filename, 'r') as template:
        try:
            yaml_data = yaml.safe_load(template)
            print('my yaml: {}'.format(yaml_data))
        except yaml.YAMLError as exc:
            print(exc)
    print(yaml_data)
    return yaml_data


def get_value_from_yaml(key):
    data_dict = read_YAML_from_config()
    return data_dict[key]


if __name__ == '__main__':
    # read_YAML_from_config()
    print(get_value_from_yaml('new_UM'))
