from ifccityjson.cityjson2ifc import JSON_TO_IFC

header = "| **CityJSON** | **IFC** | **IFC attributes** |\n|:---|:---|:---|\n"
body = ""
for co_type, ifc_type in JSON_TO_IFC.items():
    body += "| "
    body += co_type
    body += " | "
    body += ifc_type[0]
    body += " | "
    if len(ifc_type) > 1:
        body += ", ".join(f"{k}: {v}" for k,v in ifc_type[1].items())
    body += " |"
    body += "\n"
table = header + body
print(table)