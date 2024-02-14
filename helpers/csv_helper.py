import os
import csv


def get_data_from_csv(path, filename):
    data = []

    file_path = f'{path}{os.path.sep}{filename}'

    try:
        with open(file_path, encoding="UTF-8-SIG") as csv_file:
            csv_dictionary = csv.DictReader(csv_file, delimiter=',')

            for dictionary_row in csv_dictionary:
                # Check if 'Photos Names' exists in the row
                if 'Photos Names' in dictionary_row:
                    # Split 'Photos Names' into a list if it exists
                    dictionary_row['Photos Names'] = dictionary_row['Photos Names'].split(';')
                data.append(dictionary_row)
    except FileNotFoundError:
        print(f'File .\\{file_path} was not found.')
        raise
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

    return data
