import glob, os, re

class Loader:

  def __init__(self, basedir, project="", extension=".yml")
    self.project = "projects" + os.sep + project

    self.ext = extension if extension.startswith(".") else "." + extension
    self.basedir = basedir
    self.projectsdir = self.get_projects_dir()

  def get_projects_dir(self):
    return os.path.join(os.path.dirname(self.basedir), self.project)

  def load_files(self):
    files = self.get_files()
    if self.has_master_file(files):
      filepath = self.get_file_path("all", self.ext)
      return ([self.read_file(filepath)])
    numeric_files = self.get_only_numeric_files(files)
    numeric_map = self.create_numeric_mapping(numeric_files)
    numeral_files = self.create_sorted_file_text_list(numeric_map)
    meta = self.read_file(self.get_file_path("meta", self.ext))
    return (numeral_files, meta)

  def read_file(self, file_to_read):
    with open(file_to_read, 'r') as f:
      data = f.read()
    return data

  def create_numeric_mapping(self, numeric_files):
    numeric_map = {}
    for nf in numeric_files:
      pattern = r"([0-9]+)"
      numeric = re.search(pattern, nf).group(1)
      ntextfile = self.get_file_path(nf)
      numeric_map[numeric] = self.read_file(ntextfile)
    return numeric_map

  def create_sorted_file_text_list(self, numeric_map):
    sorted_keys = sorted(numeric_map.keys())
    return [numeric_map[x] for x in sorted_keys]

  def get_only_numeric_files(self, files):
    pattern = r"([0-9]+)" + re.escape(self.ext)
    return [f for f in files if re.match(pattern, f)]

  def get_file_path(self, file_for_path, extension = ""):
    return os.path.join(self.projectsdir, file_for_path + str(extension))

  def get_files(self):
    return [f for f in os.listdir(self.projectsdir) if f.endswith(self.ext)]

  def has_master_file(self, files):
    allfile = "all" + self.ext
    return allfile in files

