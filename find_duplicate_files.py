"""
Write a function that returns a list of all the duplicate files.

Return a list of tuples where:

- the first item is the duplicate file (this will have a NEWER time_updated)
- the second item is the original file

For example:

[
 ('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
 ('/home/trololol.mov', '/etc/apache2/httpd.conf')
]

You can assume each file was only duplicated once.

"""

# depth-first will go down into each directory first, then move over

# breadth-first will go across each directory, then down into each folder

# let's do an md5 checksum on the file to see if they're the same
# info we need for each file: md5, file name, time updated

import hashlib
import os

def find_duplicate_files():
    all_files = {}
    results = []
    root_dir = "/Users/juliaherron/Downloads"
    for dir_name, subdir_list, file_list in os.walk(root_dir):
        for short_name in file_list:
            file_name = f"{root_dir}/{short_name}"
            try:
                file_md5 = hashlib.md5(open(file_name, "rb").read()).hexdigest()
                # we found a duplicate
                if all_files.get(file_md5):
                    first_file_name, first_file_time = all_files[file_md5]
                    # the file already in the map is newer
                    if first_file_time > os.path.getmtime(file_name):
                        results.append((first_file_name, file_name))
                    else:
                        results.append((file_name, first_file_name))
                    print(f"Here are the duplicates: {results}")
                    return
                # no duplicate yet
                else:
                    all_files[file_md5] = (file_name, os.path.getmtime(file_name))

            except FileNotFoundError:
                print(f"Cannot hash file {file_name}")

    print(f"Here are the duplicates: {results}")


if __name__ == "__main__":
    find_duplicate_files()
