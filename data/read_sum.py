import yaml
def read_data():
    with open("D://phpStudy//app_test//data//sum_number.yml","r",encoding="utf-8")as f:
        data=yaml.safe_load(f)
        read_list=[]
        for i in data.values():
            read_list.append(i.values())
        return read_list

