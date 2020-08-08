import os
# with open('testing_zip.py', 'r') as f:
#     c = f.readlines()
#     c.remove(c[21])
#     print(len(c))
#     print(c)
#     with open('test_write_line.py','w') as f:
#         f.writelines(c)
#


# path 路径 ， num要删除的某一行
def delete_line_py(path, num):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines.remove(lines[num-1])
        f.close()
        import os
        os.remove(path)
        with open(path, 'w') as f:
            f.writelines(lines)
            f.close()


def change_line_py(path, num,str):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines[num-1] = str
        f.close()
        import os
        os.remove(path)
        with open(path, 'w') as fe:
            fe.writelines(lines)
            fe.close()
