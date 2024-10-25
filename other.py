"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_m1fqz9ot = self.__tk_button_m1fqz9ot(self)
        self.tk_input_m1fr1n77 = self.__tk_input_m1fr1n77(self)
        self.tk_tabs_m2insk0t = self.__tk_tabs_m2insk0t(self)
        self.tk_text_m2insycu = self.__tk_text_m2insycu(self.tk_tabs_m2insk0t_0)
        self.tk_text_m2int8ee = self.__tk_text_m2int8ee(self.tk_tabs_m2insk0t_1)
        self.tk_frame_m2ipqqo5 = self.__tk_frame_m2ipqqo5(self)
        self.tk_tabs_m2ipqx0q = self.__tk_tabs_m2ipqx0q(self.tk_frame_m2ipqqo5)
        self.tk_text_m2ipr2fa = self.__tk_text_m2ipr2fa(self.tk_tabs_m2ipqx0q_0)
        self.tk_text_m2ipr5d2 = self.__tk_text_m2ipr5d2(self.tk_tabs_m2ipqx0q_1)

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar:
                vbar.lift(widget)
            if hbar:
                hbar.lift(widget)

        def hide():
            if vbar:
                vbar.lower(widget)
            if hbar:
                hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar:
            vbar.bind("<Enter>", lambda e: show())
        if vbar:
            vbar.bind("<Leave>", lambda e: hide())
        if hbar:
            hbar.bind("<Enter>", lambda e: show())
        if hbar:
            hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_button_m1fqz9ot(self, parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=120, y=57, width=50, height=30)
        return btn

    def __tk_input_m1fr1n77(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=50, width=150, height=30)
        return ipt

    def __tk_tabs_m2insk0t(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_m2insk0t_0 = self.__tk_frame_m2insk0t_0(frame)
        frame.add(self.tk_tabs_m2insk0t_0, text="选项卡1")
        self.tk_tabs_m2insk0t_1 = self.__tk_frame_m2insk0t_1(frame)
        frame.add(self.tk_tabs_m2insk0t_1, text="选项卡2")
        frame.place(x=425, y=76, width=175, height=101)
        return frame

    def __tk_frame_m2insk0t_0(self, parent):
        frame = Frame(parent)
        frame.place(x=425, y=76, width=175, height=101)
        return frame

    def __tk_frame_m2insk0t_1(self, parent):
        frame = Frame(parent)
        frame.place(x=425, y=76, width=175, height=101)
        return frame

    def __tk_text_m2insycu(self, parent):
        text = Text(parent)
        text.place(x=0, y=5, width=384, height=143)
        return text

    def __tk_text_m2int8ee(self, parent):
        text = Text(parent)
        text.place(x=3, y=0, width=172, height=81)
        return text

    def __tk_frame_m2ipqqo5(self, parent):
        frame = Frame(parent,)
        frame.place(x=0, y=146, width=200, height=150)
        return frame

    def __tk_tabs_m2ipqx0q(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_m2ipqx0q_0 = self.__tk_frame_m2ipqx0q_0(frame)
        frame.add(self.tk_tabs_m2ipqx0q_0, text="选项卡1")
        self.tk_tabs_m2ipqx0q_1 = self.__tk_frame_m2ipqx0q_1(frame)
        frame.add(self.tk_tabs_m2ipqx0q_1, text="选项卡2")
        frame.place(x=0, y=0, width=200, height=150)
        return frame

    def __tk_frame_m2ipqx0q_0(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=200, height=150)
        return frame

    def __tk_frame_m2ipqx0q_1(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=200, height=150)
        return frame

    def __tk_text_m2ipr2fa(self, parent):
        text = Text(parent)
        text.place(x=0, y=20, width=150, height=100)
        return text

    def __tk_text_m2ipr5d2(self, parent):
        text = Text(parent)
        text.place(x=10, y=20, width=150, height=100)
        return text


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_m1fqz9ot.bind('<Button-1>', self.ctl.button_left)
        self.tk_button_m1fqz9ot.bind('<Double-Button-1>', self.ctl.button_left_doub)
        self.tk_button_m1fqz9ot.bind('<Button-3>', self.ctl.button_right)
        self.tk_button_m1fqz9ot.bind('<Enter>', self.ctl.button_enter)
        self.tk_button_m1fqz9ot.bind('<Leave>', self.ctl.button_leave)
        self.tk_input_m1fr1n77.bind('<Return>', self.ctl.input_enter)
        pass

    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
