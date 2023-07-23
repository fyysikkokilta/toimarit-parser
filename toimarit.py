"""
Python script for converting The Guild of Physics volunteer list to JSON
from Excel format.

Input as a text file in the following format:
  [XYZ]JAOS
  [ROLE]
  [FIRST NAME] [SURNAME]*

  [ROLE]
  [FIRST NAME] [SURNAME]*

  [XYZ]JAOS
  ...

Example:
  TAPAHTUMAJAOS
  DJ
  Sun Mutsis

  N-VASTAAVA
  Sun Isäs
  Joku Muu

  IHMEJUTTUJAOS
  KILLANISUKKI
  Diktaattori Diktaattorinen
"""

import json

text = open("volunteers.txt", "r").read()
# Remove trailing spaces from each row
text = '\n'.join(_.strip() for _ in text.splitlines())

parts = text.split("JAOS\n")
jaokset = [name.split("\n")[-1] for name in parts][:-1]
duunarit = [part.split("\n\n") for part in parts][1:]


# Section -> Role -> Names
tekijät: dict[str, dict[str, list[str]]] = {}
assert len(jaokset) == len(duunarit), "jaokset and duunarit have different lengths"
for jaos, duunarit in zip(jaokset, duunarit):
    jaos = f"{jaos}JAOS".title()
    roles_list = [
        (duunari.split("\n")[0].title(), duunari.split("\n")[1:])
        for duunari in duunarit
    ][:-1]
    roles: dict[str, list[str]] = dict(roles_list)
    # Convert \t in names to spaces
    roles = {
        role: [name.replace("\t", " ") for name in names]
        for role, names in roles.items()
    }
    tekijät[jaos] = roles

# Convert to Name -> Roles
name_to_roles: dict[str, list[str]] = {}
for jaos, roles in tekijät.items():
    for role, names in roles.items():
        for name in names:
            if name not in name_to_roles:
                name_to_roles[name] = []
            # Convert role from
            name_to_roles[name].append(role)

# Generate files
with open("toimarit.json", "w") as f:
    json.dump(name_to_roles, f, indent=2, ensure_ascii=False)
with open("jaokset.json", "w") as f:
    # Jaos -> Roles
    jaos_to_roles: dict[str, list[str]] = {
        jaos: list(roles.keys()) for jaos, roles in tekijät.items()
    }
    json.dump(jaos_to_roles, f, indent=2, ensure_ascii=False)
with open("kuvat.json", "w") as f:
    names = {
        name: name.replace(" ", "-") + ".jpg"
        for roles in tekijät.values()
        for names in roles.values()
        for name in names
    }
    json.dump(names, f, indent=2, ensure_ascii=False)

