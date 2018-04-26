import yaml

f = "/home/rusty.hamilton/projects/python/solitary_hyena/solitary_hyena/projects/1.yml"
with open(f, "r") as mf:
  data = mf.read()

yml = yaml.load(data)
print yml

