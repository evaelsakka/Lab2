
import hashlib
import os
import sys
import glob

def find_duplicate_photos(directory):
    # Create a dictionary to store MD5 hashes and file paths
    files_by_hash = {}
    
    # Iterate over all files in the directory
    for file_path in glob.glob(os.path.join(directory, '*.*')):
        # Ignore non-image files
        if not file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            continue
        
        # Calculate the MD5 hash of the file's contents
        with open(file_path, 'rb') as f:
            file_contents = f.read()
            file_hash = hashlib.md5(file_contents).hexdigest()
        
        # Add the file path to the dictionary
        if file_hash in files_by_hash:
            files_by_hash[file_hash].append(file_path)
        else:
            files_by_hash[file_hash] = [file_path]
    
    # Filter out non-duplicate files
    return {hash_: paths for hash_, paths in files_by_hash.items() if len(paths) > 1}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <directory>')
        sys.exit(1)
    
    directory = sys.argv[1]
    
    duplicates = find_duplicate_photos(directory)
    
    if duplicates:
        print('Duplicate photos found:')
        for hash_, paths in duplicates.items():
            print(f'Hash: {hash_}')
            for path in paths:
                print(f'\t{path}')
    else:
        print('No duplicate photos found.')
