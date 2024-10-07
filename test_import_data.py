from twee_d_dict import data
for id,values in data.items():
    for item,waardes in values.items():
        print(waardes,end="\t")
    print("")