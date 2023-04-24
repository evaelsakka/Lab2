import os
import glob
import hashlib
from collections import defaultdict
from typing import List, Dict, Tuple


def get_files(directory: str) -> List[str]:
    """
    Return a list of all files in the given directory.
    """
    return glob.glob(os.path.join(directory, '**'), recursive=True)


def get_file_hash(file_path: str) -> str:
    """
    Return the MD5 hash of the file at the given path.
    """
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    return hashlib.md5(file_bytes).hexdigest()


def find_duplicate_files(directory: str) -> Dict[str, List[str]]:
    """
    Find all duplicate files in the given directory.
    Returns a dictionary mapping file hashes to lists of file paths.
    """
    file_hashes = defaultdict(list)
    files = get_files(directory)
    for file_path in files:
        if os.path.isfile(file_path):
            file_hash = get_file_hash(file_path)
            file_hashes[file_hash].append(file_path)

    duplicate_files = {hash_: paths for hash_, paths in file_hashes.items() if len(paths) > 1}
    return duplicate_files


def main():
    directory = input("/Users/evaelsakka/Desktop:")
    duplicate_files = find_duplicate_files(directory)
    if duplicate_files:
        print("Duplicate files found:")
        for hash_, paths in duplicate_files.items():
            print(f"Hash: {hash_}")
            for path in paths:
                print(f" - {path}")
    else:
        print("No duplicate files found.")


if __name__ == "__main__":
    main()
