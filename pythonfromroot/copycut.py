from tkinter import *


def cut(editor, event=None):
    editor.event_generate("<<Cut>>")


def copy(editor, event=None):
    editor.event_generate("<<Copy>>")


def paste(editor, event=None):
    editor.event_generate('<<Paste>>')


def clear(editor, event=None):
    editor.event_generate('<<Clear>>')


def undo(editor,event=None):
    editor.event_generate("<<Undo>>")


def select_all(editor, event=None):
    editor.event_generate("<<SelectAll>>")


def display(event):
    if menubar.winfo_ismapped():
        menubar.unpost()
        root.unbind("<<Button-1>>")


def rightKey(editor,event):
    
    if menubar.winfo_ismapped():
        menubar.unpost()
        return

    menubar.delete(0, END)
    menubar.add_command(label='剪切', command=lambda: cut(editor))
    menubar.add_command(label='复制', command=lambda: copy(editor))
    menubar.add_command(label='粘贴', command=lambda: paste(editor))
    menubar.add_command(label='清空', command=lambda: clear(editor))
    menubar.add_command(label='撤销', command=lambda: undo(editor))
    menubar.add_command(label='全选', command=lambda: select_all(editor))
    menubar.post(event.x_root, event.y_root)
    root.bind('<Button-1>', display)


if __name__ == '__main__':
    root = Tk()
    menubar = Menu(root, tearoff=False)

    root.columnconfigure(0,weight=1)
    ent = Entry(root,width=20)
    ent.grid(column=0,row=2, sticky=(N,S))
    ent.bind("<Button-3>", lambda x: rightKey(ent, x))
    w, h = 500, 300
    root.bind('<FocusOut>',display)
    root.bind("<Configure>", display)
    root.geometry("{}x{}".format(w, h))
    root.mainloop()
