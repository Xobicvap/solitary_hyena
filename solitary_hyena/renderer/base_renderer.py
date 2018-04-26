from jinja2 import Environment, BaseLoader, meta

class BaseRenderer:

  def __init__(self):
    self.jinja_env = self.get_jinja_environment()

  def title(self, entries, id, parser):
    return entries[id].title

  def stats(self, entries, id, parser):
    stats = {}
    for key in parser.var_repo()['stats']:
      stats[key] = parser.var_repo()['key']
    return stats

  def text(self, entries, id, parser):
    entry_template = entries[id].text_template
    return parse_template(entry_template, parser)

  def user(self, entries, id, parser):
    entry_template = entries[id].user_template
    return parse_template(entry_template, parser)

  def parse_template(self, entry_template, parser):
    unparsed_template = self.get_template_object(entry_template)
    entry_vars = self.get_variable_list(unparsed_template)
    var_dict = self.compile_var_dict(entry_vars, parser.var_repo())
    return unparsed_template.render(var_dict)

  def get_template_object(self, entry_template):
    unparsed = self.jinja_env.from_string(entry_template)
    return unparsed
  
  def get_variable_list(self, unparsed)
    parsed = self.jinja_env.parse(unparsed)
    entry_vars = meta.find_undeclared_variables(parsed)
    return entry_vars

  def compile_var_dict(self, entry_vars, repo):
    var_dict = {}
    for variable in entry_vars:
      var_dict[variable] = repo[variable]
    return var_dict
