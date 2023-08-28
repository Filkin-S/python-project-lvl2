import os.path
import json
import yaml


def parsed(file_path):
    _, format = os.path.splitext(file_path)
    with open(file_path) as f:
        if format == '.json':
            return json.load(f)
        elif format == '.yml':
            return yaml.safe_load(f)
