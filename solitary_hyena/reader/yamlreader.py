import yaml
from structures.module import Module
from structures.entry import Entry
from structures.story import Story

class YamlReader:

  def read_entries(self, filetuple):
    entries_yaml = self.read_yaml_entries(filetuple)
    story = Story()
    story.title = entries_yaml["title"]
    if "description" in entries_yaml:
      story.description = entries_yaml["description"]
    for id, entry_obj in entries_yaml["entries"].iteritems():
      story.entries[id] = self.read_entry(entry_obj)
    return story

  def read_entry(self, entry_obj):
    entry = Entry()
    entry.id = entry_obj["id"]
    entry.text_template = self.get_if_present(entry_obj, "text_template")
    var_modules = self.get_if_present(entry_obj, "var_modules")
    user_modules = self.get_if_present(entry_obj, "user_modules")
    for var_module in var_modules: 
      entry.var_modules.append(Module(var_module))
    for user_module in user_modules:
      entry.user_modules.append(Module(user_module))
    return entry

  def get_if_present(self, entry_obj, key):
    if key in entry_obj and entry_obj[key] is not None:
      return entry_obj[key]
    return None

  def read_yaml_entries(self, filetuple):
    entries = self.read_yaml_list(filetuple[0])
    if len(filetuple) == 2:
      z = entries.copy()
      z.update(self.read_yaml(filetuple[1]))
    return z

  def read_yaml_list(self, yamllist):
    entry_dict = {}
    entry_dict["entries"] = {}
    for yamldoc in yamllist:
      yml = self.read_yaml(yamldoc)
      
      entry_dict["entries"][yml["id"]] = yml
    return entry_dict

  def read_yaml(self, yamldoc):
    return yaml.load(yamldoc)
