def solution(new_id):
    import re
    a=new_id.lower()
    m = re.findall(r'[a-z0-9\-\_\.]+',a)
    if new_id=="":
        found = 'a'
    else:
        found=''.join(m)

    print("1 "+found)

    while ".." in found:
        found = found.replace("..",".")
#
    print("2 "+found)
    if found[0]=='.':
        found = found[1:]
    if found=="":
        found = 'a'
    if found[-1]=='.':
        found = found[:-1]
    if found=="":
        found = 'a'

    print("3 "+found)

    if len(found)>=16:
        found = found[:15]
    print("4 "+found)

    if found[-1]=='.':
        found = found[:-1]
    print("5 "+found)

    if found=="":
        found = 'a'

    print("6 "+found)
    if len(found) <=2:
        while len(found) < 3:
            found = found + found[-1]

    print(found)
    return found