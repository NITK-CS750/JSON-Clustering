import json


    # for line in js:
    #     doc = json.loads(line)
# print(data[0]['id'])


def convlist(li) -> str:
    has = ''
    for item in li:
        if type(item) == type(dict()):
            has = convert(item)
    return 'and ' + has

def convert(doc) -> str:
    s = ''
    for (key, value) in doc.items():
        has = ''
        if type(value) == type(dict()):
            has = convert(value)
            s = f'{key} has {has} '
        elif type(value) == type(list()):
            for item in value:
                has = has + convert(item)
            s = f'{key} has list of {has} '
        else:
            has = value
            continue
        
        print(s)

    return s
    
with open('../datasets/imdb', encoding = 'utf-8') as f:
    js = f.readlines()
    print(js[0])
    print(convert(json.loads(js[0])))