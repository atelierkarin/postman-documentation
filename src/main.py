import argparse
import json
import os

from utils import print_postman_title, read_item_to_md

parser = argparse.ArgumentParser(description='A tool to convert Postman collection file to markdown file.')
parser.add_argument('arg1', help='File path of Postman collection file')
parser.add_argument('-o', '--output', help='File path of the output markdown')

args = parser.parse_args()

collection_file = args.arg1
target_file = args.output if args.output else "output.md"

if __name__ == "__main__":
    postman = json.load(open(collection_file, "r"))

    output = ""
    output += print_postman_title(postman)
    output += read_item_to_md(postman["item"])

    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    with open(target_file, "w") as f:
        f.write(output)
        print("Markdown Generated at: " + target_file)