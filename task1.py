def group_by_owners(dict_para):
    dict2={}
    for file,owner in dict_para.items():
        if(owner in dict2.keys()):
            dict2[owner].append(file)
        else:
            dict2[owner]=[file]
    return dict2

dict1={
    'input.txt':'Randy',
    'Code.py':'Stan',
    'Output.txt':'Randy'
}
ans = group_by_owners(dict1)
print(ans)
