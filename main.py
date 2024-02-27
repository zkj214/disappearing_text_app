from tkinter import *
from tkinter import filedialog,messagebox

instruction="If you don't press any key for 5 seconds, the text you have typed will disappear"

window=Tk()
window.config(width=500,height=500,bg="#F9F6EE",padx=20,pady=20)
window.title("Disappearing Text")

header=Label(text="Dangerous Writing App",font=("Calibri",20,"bold"),bg="#F9F6EE",fg="black")
header.grid(column=0,row=0)

text=Label(text=instruction,font=("Helvetica",12,"normal"),bg="#F9F6EE",fg="black")
text.grid(column=0,row=1)

text_input=Text(width=50,bg="#F9F6EE",fg="black",borderwidth=0)
text_input.grid(column=0,row=2,padx=20,pady=20)
text_input.focus()


def reset_app():
    text_input.delete(1.0,END)


def type_txt(event):
    global timer

    key=event.char

    window.after_cancel(timer)
    timer = window.after(5000, reset_app)


def save_txt():
    global timer
    window.after_cancel(timer)
    user_txt=text_input.get(1.0,"end-1c")

    file_path=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Word File","*.docx"),("Text File","*.txt")])
    file_name=file_path.split('/')[-1]

    with open(f"{file_path}",'w') as file:
        file.write(f"{user_txt}")

    messagebox.showinfo(title="Success!",message=f"{file_name} has been successfully saved.")


timer = window.after(5000, reset_app)

save_btn=Button(text="Save",padx=10,pady=10, font=("arial",12,"normal"),command=save_txt)
save_btn.grid(column=0,row=3)


window.bind("<Key>",type_txt)


window.mainloop()