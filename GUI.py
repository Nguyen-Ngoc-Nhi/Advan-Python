import tkinter as tk
window = tk.Tk()
window.title("Student Information System")
window.geometry("800x600")

#def onClick():
#    messagebox.showinfo(message="Button 1 clicked")
    
#btn = tk.Button(window, text = "Button 1", command = onClick)
#btn.place(x=350, y=400, width=100)

tk.Label(window, text = "Username").grid(
column = 0, row = 0, sticky = tk.EW, padx = 3, pady = 3)
tk.Label(window, text = "Password").grid(
column = 0, row = 1, sticky = tk.EW, padx = 3, pady = 3)
tk.Entry(window).grid(
column = 1, row = 0, sticky = tk.EW, padx = 3, pady = 3, columnspan = 4)
tk.Entry(window).grid(
column = 1, row = 1, sticky = tk.EW, padx = 3, pady = 3, columnspan = 4)
tk.Button(window, text = "Login").grid(
column = 0, row = 2, columnspan = 2)
tk.Button(window, text = "Exit").grid(
column = 2, row = 2, columnspan = 2)

window.mainloop()