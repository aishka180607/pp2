#ex1
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")

for el in data["imdata"]:
    DN = el["l1PhysIf"]["attributes"]["dn"]
    Description = el["l1PhysIf"]["attributes"]["descr"]
    Speed = el["l1PhysIf"]["attributes"]["speed"]
    MTU = el["l1PhysIf"]["attributes"]["mtu"]
    if len(DN) == 42:
        print(DN, Description, "                           ", Speed, " ", MTU)
    else:
        print(DN, Description, "                            ", Speed, " ", MTU)

#or
import json

with open('1json.json') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<10}{:<8}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<50}{:<20}{:<8}{:<6}".format(dn, description, speed, mtu))