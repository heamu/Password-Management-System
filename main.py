# i have to do this
from tkinter import *##it only imports all the classes
from tkinter import messagebox
import password_function

def password_gen():
    password_req = password_function.generator()
    password_entry.insert(0,password_req)
def save():
    website_name=website_entry.get()
    email_data = email_entry.get()
    password_data=password_entry.get()
 
    if len(password_data)==0 or len(website_name)==0:
        messagebox.showinfo(title="oops",message="Please make sure that you have entered every thing")
    else:
        is_ok=messagebox.askokcancel(title=website_name,message=f"These are the details entered :\nEmail:{email_data}\nPassword:{password_data}\nIs it ok to save ?")
        if is_ok:
            with open("data_password.txt","a") as file_:
                file_.write(f"website : {website_name} || email : {email_data}  || password : {password_data}. \n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)

#***********************UI SET UP *******************************


window = Tk()
window.title("password_manager")
window.config(padx=50,pady=50)
#window.minsize(width=500,height = 500)

canvas = Canvas(width= 200,height=200)
bg_image = PhotoImage(file="pass_word.png")
canvas.create_image(100,100,image = bg_image)
canvas.grid(column=1,row=0)

website_label = Label(text="website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry(width=48)
website_entry.grid(column=1,row=1,columnspan=2)

website_entry.focus()#this is to place the cursor in this field

email_entry = Entry(width=48)
email_entry.grid(column=1,row=2,columnspan=2)

email_entry.insert(0,"hemanthkumarvaddipalli@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(column=1,row=3)
add_button = Button(text="Add",width= 36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

generate_button= Button(text="Generate Password",command=password_gen)
generate_button.grid(column=2,row=3)

window.mainloop()

