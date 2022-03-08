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

def find_duplicate_files(starting_directory):
    all_files = {}
    stack = [starting_directory]
    results = []

    while len(stack) > 0:
        current_path = stack.pop()
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)
        else:
            file_md5 = hashlib.md5(open(current_path, "rb").read()).hexdigest()
            # we found a duplicate
            if all_files.get(file_md5):
                first_file_name, first_file_time = all_files[file_md5]
                # the file already in the map is newer
                if first_file_time > os.path.getmtime(current_path):
                    results.append((first_file_name, current_path))
                else:
                    results.append((current_path, first_file_name))
            # no duplicate yet
            else:
                all_files[file_md5] = (current_path, os.path.getmtime(current_path))

    print(f"Here are the duplicates: {results}")
    return results


if __name__ == "__main__":
    find_duplicate_files("/Users/juliaherron/Downloads")
