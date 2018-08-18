import re
import os
import urllib2
from six.moves import urllib
import tarfile
from tqdm import tqdm

detection_model_zoo_md = "https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/g3doc/detection_model_zoo.md"
download_dir = "models"


response = urllib2.urlopen(detection_model_zoo_md)
html = response.read()
# print(html)

matches = re.findall('(http[A-Za-z0-9\:\/_\-\.]*tar\.gz)', html, re.DOTALL)

print("Found %d models in %s"%(len(matches), detection_model_zoo_md))
print("Downloading")
for m in tqdm(matches):
    print(m)
    local_file = download_dir + '/' + m.split('/')[-1]
    urllib.request.urlretrieve(m, local_file)
    tar = tarfile.open(local_file)
    tar.extractall(path=download_dir)
    tar.close()
    os.remove(local_file)
