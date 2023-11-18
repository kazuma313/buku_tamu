list_tuple = [("Python", "24q",2000), ("Spark", "dasf", 2500), ("Pandas", "54d", 3000)]
data_list = []
apid ={
        "nama" : "python",
        "alamat" : "dads",
        "no_telepon" : 2000
    }

import json

for data in list_tuple:
    print(data[0])
    data_list.append(
                        {
                            "nama" : data[0],
                            "alamat" : data[1],
                            "no_telepon" : data[2]
                        }
                    )


print(json.dumps(data_list))