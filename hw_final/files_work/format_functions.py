from pathlib import Path
import csv
import json
import pickle
import os

def json_to_pickle (path:Path)->None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(f'{file.stem}.pickle','wb') as f_write:
                pickle.dump (data,f_write)

def pickle_to_csv (file:Path)->None:
    with (
        open(file,'rb') as f_read,
        open(f'{file.stem}.csv', 'w', newline='', encoding ='utf-8') as f_write  #перезапись в csv
    ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write,fieldnames=headers_list, dialect='excel-tab',
        quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


def get_size(path='.'):
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_size(entry.path)
    return result


def dir_info(dir_path):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            the_path = os.path.join(root, file)
            results.append({"parent_directory": root, 
                            "dir_or_file": 'File',
                            "name": file,
                            "size_in_bytes": os.path.getsize(the_path)})

        for dir in dirs:
            the_path = os.path.join(root, dir)
            size = get_size(the_path)
            results.append({"parent_directory": root, 
                            "dir_or_file": 'Directory',
                            "name": dir,
                            "size_in_bytes": size})

    with open("result.json", "w") as json_f:
        json.dump(results, json_f)

    with open("result.csv", "w") as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=results[0].keys(), dialect='excel-tab')
        writer.writeheader()
        writer.writerows(results)

    with open("result.pickle", "wb") as pickle_f:
        pickle.dump(results, pickle_f)