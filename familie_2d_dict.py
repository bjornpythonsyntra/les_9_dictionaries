myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#item toevoegen aan dictionary
myfamily.update({"child4":{"name":"Bjorn","year":2000}})
for kind in myfamily.values():
    for k,v in kind.items():
        print(k,v)