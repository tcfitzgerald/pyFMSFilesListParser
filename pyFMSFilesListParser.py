import argparse
import re
from urllib.parse import quote
from staticjinja import make_site


parser = argparse.ArgumentParser(description='Python script to parse results of fmsadmin list files into HTML page.')
parser.add_argument('input_file', metavar='input_file', type=str, help='Full path to file list you want to process.')
parser.add_argument('fmp_server', metavar='server', type=str, help='FileMaker server FQDN (e.g. filemaker.example.com)')
parser.add_argument('output_file', metavar='output_file', type=str, help='Name of file you want to render output to.')

args = parser.parse_args()

list_file = args.input_file
server = args.fmp_server
server_url = 'fmp://' + args.fmp_server + '/'
output_file = args.output_file

with open(list_file, 'r') as f:
    lines = f.readlines()

find_database_regex = r"Databases[\/\-\w\d\/. ]{1,500}"
remove_database_regex = r"Databases\/"
remove_folder_regex = r"[0-9a-zA-Z_\- ]{1,500}\/"
folder_and_file_list = []
files_list = []

for line in lines:

    db_line_search = re.search(find_database_regex, line)
    db_line = db_line_search.group()
    folder_and_file = re.sub(remove_database_regex, "", db_line)

    folder_and_file_list.append(folder_and_file)

folder_and_file_list.sort()

db_list = []

for folder in folder_and_file_list:

    file_only = re.sub(remove_folder_regex, "", folder)
    file_only_html_safe = quote(file_only)
    files_list.append(file_only_html_safe)

    db_list.append({'display': folder, 'url': server_url + file_only_html_safe})

context = {'db_list': db_list, 'server': server}

site = make_site(contexts=[('index.html', context)])

template = site.get_template('index.html')

# site.render()

site.render_template(template, context=context, filepath=output_file)
