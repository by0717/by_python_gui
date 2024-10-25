import ttkbootstrap as ttk


class Son_WinGUI(ttk.Toplevel):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.on_login = on_login  # Callback function to handle login
        self.__win()
        self.tk_label_user_label = self.__tk_label_user_label(self)
        self.tk_label_pw_label = self.__tk_label_pw_label(self)
        self.tk_input_username_input = self.__tk_input_username_input(self)
        self.tk_button_cancle = self.__tk_button_cancle(self)
        self.tk_button_confirm = self.__tk_button_confirm(self)
        self.tk_input_pw_input = self.__tk_input_pw_input(self)

    def __win(self):
        self.title("Login Information")
        # Set window size and center it
        width = 336
        height = 120
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = f'{width}x{height}+{(screenwidth - width) // 2}+{(screenheight - height) // 2}'
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_user_label(self, parent):
        label = ttk.Label(parent, text="Username", font=("Microsoft YaHei", 12, "italic"), anchor="center")
        label.place(x=1, y=3, width=118, height=30)
        return label

    def __tk_label_pw_label(self, parent):
        label = ttk.Label(parent, text="Password", font=("Microsoft YaHei", 12, "italic"), anchor="center")
        label.place(x=2, y=43, width=118, height=30)
        return label

    def __tk_input_username_input(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=150, y=3, width=178, height=30)
        return ipt

    def __tk_button_cancle(self, parent):
        btn = ttk.Button(parent, text="Cancel", takefocus=False, command=self.destroy)
        btn.place(x=32, y=85, width=104, height=30)
        return btn

    def __tk_button_confirm(self, parent):
        btn = ttk.Button(parent, text="Confirm", takefocus=False, command=self.login)  # Use command here
        btn.place(x=196, y=85, width=115, height=30)
        btn.bind("<Button-1>", self.login)  # Bind the button click to the login method
        return btn

    def __tk_input_pw_input(self, parent):
        ipt = ttk.Entry(parent, show='*')  # Use show='*' to hide password input
        ipt.place(x=149, y=43, width=178, height=30)
        return ipt

    def login(self, event):
        username = self.tk_input_username_input.get()
        password = self.tk_input_pw_input.get()
        self.on_login(username, password, event)  # Call the callback function
        self.destroy()  # Close the dialog


class MainApp(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("400x200")
        self.label_info = ttk.Label(self, text="Please log in.")
        self.label_info.pack(pady=20)

        self.button_open_login = ttk.Button(self, text="Open Login", command=self.open_login_dialog)
        self.button_open_login.pack(pady=(10, 0))

    def open_login_dialog(self):
        Son_WinGUI(self, self.update_label)  # Pass the update_label method as a callback

    def update_label(self, username, password):
        self.label_info.config(text=f"Username: {username}, Password: {password}")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
