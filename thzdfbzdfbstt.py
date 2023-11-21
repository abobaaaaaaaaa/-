print('add,del,redact,show')
f=open('library.txt','w')
f.close
numbers=[]
while True:
    f=open('library.txt','a')
    funct=str(input('what doing'))
    if funct=='add':
        author_add=str(input('author'))
        f.write(author_add)
        name_add=str(input('name'))
        f.write(name_add)
        year_add=str(input('year'))
        f.write(year_add)
        num_add=int(input('book number'))
        numbers.append(num_add)
        f.close
    elif funct=='del':
        deelete_num=int(input('номер который надо заменить'))
        f.replace(deelete_num,'','')
        f.close
    elif funct=='redact':
        red=str(input('what replace'))
        new_red=str(input('for what replace'))
        num_red=int(input('where replace'))
        f.replace(new_red,red,new_red)
        f.close
    elif funct=='show':
        f.close
        f=open('library.txt','r')
        f.read()
        f.close