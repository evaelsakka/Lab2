import os
import hashlib
import glob
from collections import defaultdict

class Photo:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.created = os.path.getctime(path)
        self.md5 = self.get_md5()

    def get_md5(self):
        with open(self.path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

def find_duplicate_photos(directory):
    photos = glob.glob(directory + '/**/*.jpg', recursive=True)
    photo_dict = defaultdict(list)

    for photo_path in photos:
        photo = Photo(photo_path)
        photo_dict[photo.md5].append(photo)

    return photo_dict

# Example usage
directory = '/Users/evaelsakka/git'
duplicate_photos = find_duplicate_photos(directory)

for md5, photo_list in duplicate_photos.items():
    if len(photo_list) > 1:
        print(f"Photos with MD5 hash {md5}:")
        for photo in photo_list:
            print(f"- {photo.path}")

