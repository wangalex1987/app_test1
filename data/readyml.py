import yaml
with open("./maodian.yml","r",encoding="utf-8")as f:
    data=yaml.safe_load(f)
    print(data)
    print(type(data.get("value")))