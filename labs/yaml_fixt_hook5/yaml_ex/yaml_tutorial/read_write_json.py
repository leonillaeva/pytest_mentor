# TypeError: Object of type date is not JSON serializable
# Problem issues: .inf, -.Inf, .NAN ->  Infinity, -Infinity, NaN -> specific numbers to strings

import json
import yaml
from yaml import CLoader as Loader
from datetime import date


def custom_serializer(obj):
    """
    This function converts non-serializable types to serializable.
    - Transforms `date` to string in the ISO format (YYYY-MM-DD).
    - Transforms special numbers `float` (.inf, -.Inf, .NAN) to strings.
    """

    if isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, float):
        if obj == float('inf'):
            return "Infinity"
        elif obj == float('-inf'):
            return "-Infinity"
        elif obj != obj:
            return "NaN"
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def serialize_data(data):
    """Recursive process data by serializing special types(date, float)"""
    if isinstance(data, dict):
        return {key: serialize_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [serialize_data(item) for item in data]
    elif isinstance(data, date):
        return custom_serializer(data)
    return data


def convert_types_yaml(f_yaml_1, fl_json):
    with open(f_yaml_1, 'r') as f_y_1:
        dictionary_1 = yaml.load(f_y_1, Loader)

        processed_data = serialize_data(dictionary_1)
        with open(fl_json, 'w') as f_j_1:
            json.dump(processed_data, f_j_1, indent=4)


def convert_multiple_yaml_documents(f_yaml_2, fl_json):
    """Reads a YAML file with some documents, converts and writes to JSON"""
    with open(f_yaml_2, 'r') as f_y_2:
        yaml_documents = list(yaml.load_all(f_y_2, Loader))

        processed_data = [serialize_data(doc) for doc in yaml_documents]

        with open(fl_json, 'w') as js_file:
            json.dump(processed_data, js_file, indent=4)


def read_yaml():
    with open(file_yaml_1, 'r') as f_y_1:
        text1 = f_y_1.read()
        return text1


file_yaml_1 = r'simple_file_tutorial_1.yml'
file_yaml_2 = r'multiple_documents_2.yaml'
file_json_types = r'data_yaml_types.json'
file_json_mult = r'data_yaml_mult.json'

# convert_types_yaml(file_yaml_1, file_json_types)
convert_multiple_yaml_documents(file_yaml_2, file_json_mult)

# print(type(text1))  # <class 'str'>
# print(type(dictionary_1))  # <class 'NoneType'>
# print('')
# print(type(text2))  # <class 'str'>
# print(type(dictionary_2))  # <class 'generator'>
