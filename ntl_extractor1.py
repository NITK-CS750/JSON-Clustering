import json
import pprint
from pathlib import Path


json_data = open('imdb_movies_0.json', 'r').read()
json_dict = json.loads(json_data)
# json_dict = [{"a":{"b":"c","d":["e","f",{"g":{"h":"i"}}]}},{"d":["e","f",{"g":{"h":"i"}}]}]

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
                # print("/".join(stack))
                # print(key)

    return (all_keys,final_dict)            



def internal(json_map,level):
    if(len(final_list)<level+1):
        final_list.append({"keys":set(),"rtl_paths":set()})        
    (all_keys, final_dict) = do_walk(json_map)
    # print(all_keys)
    # pprint.pprint(json_map)
    # pprint.pprint(all_keys)
    # print(level)
    # print(len(final_list))
    for key in all_keys:
        keys_list.add(str(key))
    for rtl_pth in final_dict.keys():
        rtl_paths_list.add(rtl_pth)
    for key in keys_list:
        final_list[level]['keys'].add(key)
    for rtl_path in rtl_paths_list:
        final_list[level]['rtl_paths'].add(rtl_path)  

stack = []
final_dict = {}
all_keys = set()                
keys_list = set()
rtl_paths_list = set()
final_list = []
f = open("keys_list.txt", "w")
def getDictFromList(input_list):
    l = []
    for ob in input_list:
        if(type(ob) is list):
            l.append(getDictFromList(ob))
        elif(type(ob) is dict):
            l.append(ob)    
    return l


for i in range(0,len(json_dict)):
    stack = []
    final_dict = {}
    all_keys = set()                
    keys_list = set()
    rtl_paths_list = set()
    final_list=[]
    internal(json_dict[i],0)
    keys = json_dict[i].keys()
    q = []
    for key in keys:
        if(type(json_dict[i][key]) is dict):q.append((json_dict[i][key],1))
        elif(type(json_dict[i][key]) is list):
            for object in getDictFromList(json_dict[i][key]):
                q.append((object,1))
    while(len(q)!=0):
        stack = []
        final_dict = {}
        all_keys = set()                
        keys_list = set()
        rtl_paths_list = set()
        (map,level) = q.pop(0)
        internal(map,level)
        for key in map.keys():
            if(type(map[key]) is dict):
                q.append((map[key],level+1))
            elif(type(map[key]) is list):
                for object in getDictFromList(map[key]):
                    q.append((object,level+1))
    f.write(str(final_list)+"\n")               
    # print("ITERATION "+str(i)+" : LEN_KEY_0 : "+str(len(final_list[0]['keys']))+" : LEN_RTL_0 : "+str(len(final_list[0]['rtl_paths']))+" : LEN_KEY_1 : "+str(len(final_list[1]['keys']))+" : LEN_RTL_1 : "+str(len(final_list[0]['rtl_paths'])))                

f.close()



# print((final_list))    

# f = open("keys_list.txt", "w")
# f.write(str(keys_list))
# f.close()    
# f = open("rtl_paths_list.txt", "w")
# f.write(str(rtl_paths_list))
# f.close()    
