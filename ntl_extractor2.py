import json

json_dict = []
count = 0
with open('imdb', encoding='utf-8') as f:
    for line in f:
        doc = json.loads(line)
        json_dict.append(doc)
        count+=1
json_dict = [{"a":{"b":"c","d":["e","f",{"g":{"h":"i"}}]}}]
count = 1 
print(count, "documents loaded.")

stack = []
final_dict = {}
all_keys = set()

def do_walk(datadict):
    if isinstance(datadict, dict):
        for key, value in datadict.items():
            stack.append(key)
            if isinstance(value, dict) and len(value.keys()) == 0:
                for val in stack:
                    all_keys.add(val)
                final_dict["/".join(stack)] = "EMPTY_DICT"
            if isinstance(value, list) and len(value) == 0:
                for val in stack:
                    all_keys.add(val)
                final_dict["/".join(stack)] = 'EMPTY_LIST'
            if isinstance(value, dict):
                do_walk(value)
            if isinstance(value, list):
                do_walk(value)
            if isinstance(value, str):
                for val in stack:
                    all_keys.add(val)
                final_dict["/".join(stack)] = value
            stack.pop()

    if isinstance(datadict, list):
        n = 0
        for key in datadict:
            n = n + 1
            if isinstance(key, dict):
                do_walk(key)
            if isinstance(key, list):
                do_walk(key)
            if isinstance(key, str):
                for val in stack:
                    all_keys.add(val)
                final_dict["/".join(stack)] = key

keys_list = []
rtl_paths_list = []
for i in range(0,len(json_dict)):
    do_walk(json_dict[i])
    keys_list.append(all_keys)
    rtl_paths_list.append([x for x in final_dict.keys()])
    final_dict={}
    all_keys=set()

def flatten(t):
    return [item for sublist in t for item in sublist]

import re
final_append_array = []
for document in rtl_paths_list:
    for path in document:
        if path is not None:
            result = [path[_.start()+1:] for _ in re.finditer("/", path)]
        for item in result : document.append(item)
    final_append_array.append(list(set(document)))
rtl_paths_list = final_append_array

f = open("NTL_paths_list.json", "w")
f.write(json.dumps(rtl_paths_list, indent=4))
f.close()