def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
        
def create_dict(seq):
    dict = {}
    for i in seq:
        dict[i] = seq.count(i)
    return dict


list = ['1','1','2','2','3','3','5']
print(create_dict(list))
print(find_it(list))
