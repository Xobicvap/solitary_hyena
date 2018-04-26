from loader.loader import Loader
from reader.yamlreader import YamlReader
import os
import sys

#sys.path.append("..")


lo = Loader(os.path.realpath(__file__), "readtest")
files = lo.load_files()
reader = YamlReader()
entries = reader.read_entries(files)
print entries.entries[1].id
print entries.entries[1].text_template
print "\n\n"
print entries.entries[2].id
print entries.entries[2].text_template


