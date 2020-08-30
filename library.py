from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root =Tk()
root.title('Novels')
root.iconbitmap('images/book.ico')
root.geometry("500x500")
root.resizable(False,False)


# background image
rut_backimage = ImageTk.PhotoImage(Image.open('images/blur.jpg'))
rut_label= Label(root,image=rut_backimage)
rut_label.place(relwidth=1, relheight=1)

# Create a database and cursor
conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS libraryNovel(book TEXT,author TEXT, type TEXT)')

def add():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    #data entry
    c.execute('INSERT INTO libraryNovel(book,author,type) VALUES(?,?,?)',
    (book_name_entry.get(),author_entry.get(),type_entry.get()))

    conn.commit()
    conn.close()

    #clear text box
    book_name_entry.delete(0, END)
    author_entry.delete(0, END)
    type_entry.delete(0, END)

#Query function
def query():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # new window for showing records
    new_window=Toplevel()
    new_window.title("Novel records")
    new_window.geometry("500x500")
    new_window.resizable(False,False)
    c.execute("SELECT *, oid FROM libraryNovel ")
    records=c.fetchall()


    record_print=" "
    for record in records:
        record_print += str(record) + " " +"\n"

    query_label = Label(new_window,text=record_print)
    query_label.pack()



    conn.commit()
    conn.close()



#Labels
book_name = Label(root,text='Book Name', width=15)
book_name.place(x=30,y=150)
author=Label(root,text='Author', width =15)
author.place(x=30,y=200)
type_novel=Label(root, text='Genre', width=15)
type_novel.place(x=30,y=250)

#entry
book_name_entry = Entry(root, width=25,bg="#FFFFFF")
book_name_entry.place(x=170,y=150)
author_entry = Entry(root, width=25,bg="#FFFFFF")
author_entry.place(x=170,y=200)
type_entry = Entry(root, width=25,bg="#FFFFFF")
type_entry.place(x=170,y=250)

#button
add_button =Button(root,text="Add Novel", width=10,height=1,cursor = "plus",command=add)
add_button.place(x=30,y=300)

query_button = Button(root, text="Show Novels", command=query)
query_button.place(x=150,y=300)

conn.commit()
conn.close()


root.mainloop()