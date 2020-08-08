import os


def write_py_file(filename, name, **arguments):
    full_name = filename+'.py'
    if not os.path.exists(full_name):
        with open('../bilibili/bilibili/spiders/'+full_name, 'w', encoding='utf-8')as f:
            f.write("class "+name+":\n")
            for k, v in arguments.items():
                v = v.replace('\\', '\\\\')
                f.write("    " + k+' = \''+v+'\'' + "\n")
        f.close()


def write_class(full_name, class_name, **kwargs):
    with open('../bilibili/bilibili/spiders/'+full_name, 'a', encoding='utf-8')as f:
        f.write('\n')
        f.write('\n')
        f.write("class " + class_name + ":\n")
        for k, v in kwargs.items():
            v = v.replace('\\', '\\\\')
            f.write("    " + k + ' = \'' + v + '\'' + "\n")
    f.close()

