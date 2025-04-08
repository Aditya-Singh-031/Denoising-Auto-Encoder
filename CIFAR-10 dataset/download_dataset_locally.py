# Download CIFAR-10 dataset locally as raw files

import urllib.request
import tarfile
import os

url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
filename = "cifar-10-python.tar.gz"
extract_folder = "cifar-10-data"

# Download
print("Downloading CIFAR-10 dataset...")
urllib.request.urlretrieve(url, filename)

# Extract
print("Extracting files...")
with tarfile.open(filename, "r:gz") as tar:
    tar.extractall(path=extract_folder)

# Optional: delete the tar.gz
print("Cleaning up...")
os.remove(filename)

print("Done! Dataset is available in:", extract_folder)
