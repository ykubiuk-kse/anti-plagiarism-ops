import os
import mosspy
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Description of your script")

parser.add_argument("--language", type=str, default="cc")
parser.add_argument("--submissions_folder", type=str)
parser.add_argument('--exclude', type=str)

args = parser.parse_args()

def find_files(folder_path, suffixes=['.cpp'], exclude_patterns=[]):
    matching_files = []
    
    for suffix in suffixes:
        clean_suffix = suffix if not suffix.startswith('.') else suffix[1:]
        pattern = f"*.{clean_suffix}"
        
        for path in Path(folder_path).rglob(pattern):
            path_str = str(path)
            
            should_exclude = False
            for exclude in exclude_patterns:
                if exclude in path_str:
                    should_exclude = True
                    break
            
            if not should_exclude:
                matching_files.append(path_str)
            
    return matching_files

def get_file_extensions(language):
   extensions_map = {
       'c': ['.c', '.h'],
       'cc': ['.cpp', '.hpp', '.cc', '.h'],
       'python': ['.py'],
       'java': ['.java'],
       'javascript': ['.js'],
   }
   
   language = language.lower()
   return extensions_map.get(language, [])

userid = os.getenv("MOSS_USER_ID")
language = args.language
submissions_folder = args.submissions_folder

exclude_patterns = args.exclude.split(',')
files = find_files(submissions_folder, get_file_extensions(language=language), exclude_patterns=exclude_patterns)

print("Using language: {}".format(language))

m = mosspy.Moss(userid, language)

for file in files:
    try:
        print(file)
        m.addFile(file)
    except Exception as e:
        print(f"Skipping file {file}: {str(e)}")
        continue

url = m.send(lambda file_path, display_name: print("*", end="", flush=True))
print()

print ("Report Url: " + url)
