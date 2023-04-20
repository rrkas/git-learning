import re

org = "this is a {} [{}] fruit."
for e in ["good", "bad", "rotten"]:
    print(re.sub("\[{}\]", e, org))

template = "{name} has visited this {temple_name} temple."
print(template.split('{')[-1].split('}')[0])
for e in re.finditer('{[a-z_]+}', template):
    print(e)
