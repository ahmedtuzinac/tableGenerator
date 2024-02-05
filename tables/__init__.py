import pathlib
import json
import sys


def open_and_load_json(json_file_path):
    number_of_tries_to_open_file = 0

    while number_of_tries_to_open_file < 5:
        try:
            with open(f'{json_file_path}', 'r') as file:
                data = json.load(file)
                return data
        except Exception:
            number_of_tries_to_open_file += 1

    return None


file_path = pathlib.Path(__file__).parent
name_of_json_file = 'request.json'

data = open_and_load_json(f'{file_path}/{name_of_json_file}')
if data and name_of_json_file == 'table.json':
    document = data.get('doc')
    document_styles = document.get('styles')

    table_data = data.get('table')
    header_data = table_data.get('header')
    rows_data = table_data.get('rows')

else:
    document = data['document']
    tables = document['tables']

available_styles = [
    "font-name",
    "font-size"
]
