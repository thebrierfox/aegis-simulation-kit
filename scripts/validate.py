#!/usr/bin/env python3
"""
A basic JSON validator for scenario and run files.
This script checks that required keys exist. It does not implement full JSON Schema.
"""
import argparse
import json
import sys

REQUIRED_SCENARIO_KEYS = ['id', 'description', 'steps']
REQUIRED_RUN_KEYS = ['scenario_id', 'actions']


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def validate_scenario(data):
    missing = [k for k in REQUIRED_SCENARIO_KEYS if k not in data]
    if missing:
        raise ValueError(f"Scenario missing keys: {', '.join(missing)}")
    if not isinstance(data['steps'], list):
        raise ValueError("Scenario 'steps' must be a list")


def validate_run(data):
    missing = [k for k in REQUIRED_RUN_KEYS if k not in data]
    if missing:
        raise ValueError(f"Run missing keys: {', '.join(missing)}")
    if not isinstance(data['actions'], list):
        raise ValueError("Run 'actions' must be a list")


def main():
    parser = argparse.ArgumentParser(description="Validate scenario or run JSON file.")
    parser.add_argument('--file', required=True, help='Path to JSON file to validate')
    args = parser.parse_args()

    data = load_json(args.file)

    if all(k in data for k in REQUIRED_SCENARIO_KEYS):
        try:
            validate_scenario(data)
            print("Scenario file is valid")
        except Exception as e:
            print(f"Validation error: {e}")
            sys.exit(1)
    elif all(k in data for k in REQUIRED_RUN_KEYS):
        try:
            validate_run(data)
            print("Run file is valid")
        except Exception as e:
            print(f"Validation error: {e}")
            sys.exit(1)
    else:
        print("File does not appear to be a valid scenario or run JSON.")
        sys.exit(1)

if __name__ == '__main__':
    main()
