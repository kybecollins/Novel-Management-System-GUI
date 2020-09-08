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

#Search function
def searchRecord():
    search_window=Toplevel()
    search_window.iconbitmap('images/book.ico')
    search_window.title("Search Novel ")
    search_window.geometry("400x250")
    search_window.resizable(False,False)

    ut_backimage = ImageTk.PhotoImage(Image.open('images/blur.jpg'))
    ut_label= Label(search_window,image=rut_backimage)
    ut_label.place(relwidth=1, relheight=1)

    def inSearch():
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        
        c.execute("select *  from libraryNovel where  author = ?", (z.get(),))
        conn.commit()
        rec= c.fetchall()

        
    
        record_print=" "
        for record in rec:
            record_print += str(record) + " " +"\n"

        search_label = Label(innerFrame,text=record_print ,fg = '#070400', bg ='#d7d9d8')
        search_label.place(x=30,y=10)
        
    def on(e):
        bookSearchButton['bg']= '#6a6e6b' 
    def off(e):
        bookSearchButton['bg']= '#000405'

        
    z=StringVar()

    #search box frames
    frame_Box = Frame(search_window, width = 50 , height = 30 ,bg ='#0fccf0')
    frame_Box.place(x= 188,y=88)
    outerFrame = Frame(search_window, width = 300, height = 70,bg ='#36b4c9')
    outerFrame.place(x= 45,y=150)
    innerFrame = Frame(outerFrame, width = 290, height = 59,bg ='#d7d9d8')
    innerFrame.place(x= 5,y=5)

    #Button
    bookSearchButton = Button(search_window, text = "Search",activebackground = '#26d9cb',fg = '#0cf39c' ,bg = '#000405', command = inSearch)
    bookSearchButton.place(x=190,y=90)

    #Bind hover to button
    bookSearchButton.bind('<Enter>',on)
    bookSearchButton.bind('<Leave>',off)

    #Search Entry
    bookSearchEntry = Entry(search_window, textvariable = z)
    bookSearchEntry.place(x=50,y=90)
    bookSearchEntry.insert(0,"Author Name")
    


    

    

    


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



bookSearchButton = Button(root, text = "Search", command = searchRecord)
bookSearchButton.place(x=250,y=300)


conn.commit()
conn.close()


root.mainloop()