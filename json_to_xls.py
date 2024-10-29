import os
import sys
import json
import pandas as pd
from datetime import datetime


def convert_json_to_xls(input_file):
    file_name, _ = os.path.splitext(input_file)
    with open(input_file) as file:
        data = json.load(file)
    df = pd.DataFrame(data['Result'])
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    df.to_excel(f'{file_name}-{timestamp}.xlsx', index=False)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python json_to_xls.py <input_json_filepath>. It will create the converted in the same directory.")
        sys.exit(1)
    json_file = sys.argv[1]
    convert_json_to_xls(json_file)
