import ttkbootstrap as ttk
from ttkbootstrap.constants import RIGHT
from pathlib import Path
from tkinter.scrolledtext import ScrolledText

img_filefolder_path = Path(__file__).parent / "img"
print(img_filefolder_path)


class WinGUI(ttk.Window):
    def __init__(self):
        super().__init__()
        self.__win()
        self.load_images = self.__load_images()
        self.tk_frame_contain_1 = self.__tk_frame_contain_1(self)
        self.tk_select_box_theme_list = self.__tk_select_box_theme_list(self.tk_frame_contain_1)
        self.tk_label_label_theme = self.__tk_label_label_theme(self.tk_frame_contain_1)
        self.tk_frame_contain_2 = self.__tk_frame_contain_2(self)
        self.tk_label_label_info_1 = self.__tk_label_label_info_1(self.tk_frame_contain_2)
        self.tk_label_label_info_2 = self.__tk_label_label_info_2(self.tk_frame_contain_2)
        self.tk_label_label_info_3 = self.__tk_label_label_info_3(self.tk_frame_contain_2)
        self.tk_label_label_info_4 = self.__tk_label_label_info_4(self.tk_frame_contain_2)
        self.tk_label_label_info_5 = self.__tk_label_label_info_5(self.tk_frame_contain_2)
        self.tk_label_label_info_6 = self.__tk_label_label_info_6(self.tk_frame_contain_2)
        self.tk_label_label_info_7 = self.__tk_label_label_info_7(self.tk_frame_contain_2)
        self.tk_label_label_info_8 = self.__tk_label_label_info_8(self.tk_frame_contain_2)
        self.tk_input_input_info_1 = self.__tk_input_input_info_1(self.tk_frame_contain_2)
        self.tk_input_input_info_2 = self.__tk_input_input_info_2(self.tk_frame_contain_2)
        self.tk_input_input_info_3 = self.__tk_input_input_info_3(self.tk_frame_contain_2)
        self.tk_input_input_info_4 = self.__tk_input_input_info_4(self.tk_frame_contain_2)
        self.tk_input_input_info_5 = self.__tk_input_input_info_5(self.tk_frame_contain_2)
        self.tk_input_input_info_6 = self.__tk_input_input_info_6(self.tk_frame_contain_2)
        self.tk_input_input_info_7 = self.__tk_input_input_info_7(self.tk_frame_contain_2)
        self.tk_input_input_info_8 = self.__tk_input_input_info_8(self.tk_frame_contain_2)
        self.tk_text_text_folder = self.__tk_text_text_folder(self.tk_frame_contain_2)
        self.tk_button_button_file = self.__tk_button_button_file(self.tk_frame_contain_2)
        self.tk_button_test = self.__tk_button_test(self.tk_frame_contain_2)
        self.tk_button_button_login = self.__tk_button_button_login(self.tk_frame_contain_2)
        self.tk_label_label_login = self.__tk_label_label_login(self.tk_frame_contain_2)
        self.tk_frame_Contain_3 = self.__tk_frame_Contain_3(self)
        self.tk_tabs_tab_log = self.__tk_tabs_tab_log(self.tk_frame_Contain_3)
        self.tk_text_text_log_1 = self.__tk_text_text_log_1(self.tk_tabs_tab_log_1)
        self.tk_text_text_log_2 = self.__tk_text_text_log_2(self.tk_tabs_tab_log_2)
        self.tk_text_text_log_3 = self.__tk_text_text_log_3(self.tk_tabs_tab_log_3)
        self.tk_text_text_log_4 = self.__tk_text_text_log_4(self.tk_tabs_tab_log_4)
        self.tk_text_text_log_5 = self.__tk_text_text_log_5(self.tk_tabs_tab_log_5)
        self.tk_text_text_log_6 = self.__tk_text_text_log_6(self.tk_tabs_tab_log_6)
        self.tk_text_text_log_7 = self.__tk_text_text_log_7(self.tk_tabs_tab_log_7)
        self.tk_text_text_log_8 = self.__tk_text_text_log_8(self.tk_tabs_tab_log_8)
        self.tk_tabs_tab_1 = self.__tk_tabs_tab_1(self)
        self.tk_meter_up_1 = self.__tk_meter_up_1(self.tk_tabs_tab_1_1)
        self.tk_meter_dl_1 = self.__tk_meter_dl_1(self.tk_tabs_tab_1_1)
        self.tk_meter_up_2 = self.__tk_meter_up_2(self.tk_tabs_tab_1_2)
        self.tk_meter_dl_2 = self.__tk_meter_dl_2(self.tk_tabs_tab_1_2)
        self.tk_meter_up_3 = self.__tk_meter_up_3(self.tk_tabs_tab_1_3)
        self.tk_meter_dl_3 = self.__tk_meter_dl_3(self.tk_tabs_tab_1_3)
        self.tk_meter_up_4 = self.__tk_meter_up_4(self.tk_tabs_tab_1_4)
        self.tk_meter_dl_4 = self.__tk_meter_dl_4(self.tk_tabs_tab_1_4)
        self.tk_meter_up_5 = self.__tk_meter_up_5(self.tk_tabs_tab_1_5)
        self.tk_meter_dl_5 = self.__tk_meter_dl_5(self.tk_tabs_tab_1_5)
        self.tk_meter_up_6 = self.__tk_meter_up_6(self.tk_tabs_tab_1_6)
        self.tk_meter_dl_6 = self.__tk_meter_dl_6(self.tk_tabs_tab_1_6)
        self.tk_meter_up_7 = self.__tk_meter_up_7(self.tk_tabs_tab_1_7)
        self.tk_meter_dl_7 = self.__tk_meter_dl_7(self.tk_tabs_tab_1_7)
        self.tk_meter_up_8 = self.__tk_meter_up_8(self.tk_tabs_tab_1_8)
        self.tk_meter_dl_8 = self.__tk_meter_dl_8(self.tk_tabs_tab_1_8)
        self.tk_table_table_1 = self.__tk_table_table_1(self)
        self.tk_progressbar_prog_1 = self.__tk_progressbar_prog_1(self)
        self.tk_progressbar_prog_2 = self.__tk_progressbar_prog_2(self)
        self.tk_progressbar_prog_3 = self.__tk_progressbar_prog_3(self)
        self.tk_progressbar_prog_4 = self.__tk_progressbar_prog_4(self)
        self.tk_progressbar_prog_5 = self.__tk_progressbar_prog_5(self)
        self.tk_progressbar_prog_6 = self.__tk_progressbar_prog_6(self)
        self.tk_progressbar_prog_7 = self.__tk_progressbar_prog_7(self)
        self.tk_progressbar_prog_8 = self.__tk_progressbar_prog_8(self)
        self.tk_label_label_prog_b_1 = self.__tk_label_label_prog_b_1(self)
        self.tk_label_label_prog_b_2 = self.__tk_label_label_prog_b_2(self)
        self.tk_label_label_prog_b_3 = self.__tk_label_label_prog_b_3(self)
        self.tk_label_label_prog_b_4 = self.__tk_label_label_prog_b_4(self)
        self.tk_label_label_prog_b_5 = self.__tk_label_label_prog_b_5(self)
        self.tk_label_label_prog_b_6 = self.__tk_label_label_prog_b_6(self)
        self.tk_label_label_prog_b_7 = self.__tk_label_label_prog_b_7(self)
        self.tk_label_label_prog_b_8 = self.__tk_label_label_prog_b_8(self)
        self.tk_label_label_prog_r_1 = self.__tk_label_label_prog_r_1(self)
        self.tk_label_label_prog_r_2 = self.__tk_label_label_prog_r_2(self)
        self.tk_label_label_prog_r_3 = self.__tk_label_label_prog_r_3(self)
        self.tk_label_label_prog_r_4 = self.__tk_label_label_prog_r_4(self)
        self.tk_label_label_prog_r_5 = self.__tk_label_label_prog_r_5(self)
        self.tk_label_label_prog_r_6 = self.__tk_label_label_prog_r_6(self)
        self.tk_label_label_prog_r_7 = self.__tk_label_label_prog_r_7(self)
        self.tk_label_label_prog_r_8 = self.__tk_label_label_prog_r_8(self)
        self.tk_label_label_prog_g_1 = self.__tk_label_label_prog_g_1(self)
        self.tk_label_label_prog_g_2 = self.__tk_label_label_prog_g_2(self)
        self.tk_label_label_prog_g_3 = self.__tk_label_label_prog_g_3(self)
        self.tk_label_label_prog_g_4 = self.__tk_label_label_prog_g_4(self)
        self.tk_label_label_prog_g_5 = self.__tk_label_label_prog_g_5(self)
        self.tk_label_label_prog_g_6 = self.__tk_label_label_prog_g_6(self)
        self.tk_label_label_prog_g_7 = self.__tk_label_label_prog_g_7(self)
        self.tk_label_label_prog_g_8 = self.__tk_label_label_prog_g_8(self)
        self.tk_date_select_box = self.__tk_date_select_box(self)
        self.tk_text_other_text = self.__tk_text_other_text(self)

    def __win(self):
        self.title("BY UI")
        # 设置窗口大小、居中
        width = 1024
        height = 630
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __load_images(self):
        img_filefolder_path = Path(__file__).parent / "img"
        img_files = {
            "folder_24_y": "icons8-folder-24-Y.png",
            "folder_48_y": "icons8-folder-48-Y.png",
            "folder_30_y": "icons8-folder-30-Y.png",
            "point_10_g": "icons8-point-10-G.png",
            "point_10_r": "icons8-point-10-R.png",
            "point_10_b": "icons8-point-10-B.png",
        }
        self.phtoimages = []
        for key, val in img_files.items():
            _path = img_filefolder_path / val
            self.phtoimages.append(ttk.PhotoImage(name=key, file=_path))
            print(f"Loaded image for {key}: {_path}")  # Debug statement

    def __tk_frame_contain_1(self, parent):
        frame = ttk.LabelFrame(parent, bootstyle="primary", text="Choose Theme")
        frame.place(x=0, y=0, width=1018, height=50)
        return frame

    def __tk_select_box_theme_list(self, parent):
        style = ttk.Style()
        theme_names = style.theme_names()
        cb = ttk.Combobox(parent, state="readonly", bootstyle="info", text=style.theme.name,
                          values=theme_names,)
        cb.place(x=860, y=0, width=150, height=25)
        return cb

    def __tk_label_label_theme(self, parent):
        label = ttk.Label(parent, text="Theme_select", anchor="center", bootstyle="inverse-info", font=("Arial", 10))
        label.place(x=760, y=0, width=95, height=25)
        return label

    def __tk_frame_contain_2(self, parent):
        frame = ttk.LabelFrame(parent, bootstyle="primary", text="Test Info")
        frame.place(x=0, y=45, width=1019, height=152)
        return frame

    def __tk_label_label_info_1(self, parent):
        label = ttk.Label(parent, text="MAC1", anchor="center")
        label.place(x=0, y=15, width=100, height=20)
        return label

    def __tk_label_label_info_2(self, parent):
        label = ttk.Label(parent, text="MAC2", anchor="center")
        label.place(x=0, y=45, width=100, height=20)
        return label

    def __tk_label_label_info_3(self, parent):
        label = ttk.Label(parent, text="MAC3", anchor="center")
        label.place(x=0, y=75, width=100, height=20)
        return label

    def __tk_label_label_info_4(self, parent):
        label = ttk.Label(parent, text="MAC4", anchor="center")
        label.place(x=0, y=105, width=100, height=20)
        return label

    def __tk_label_label_info_5(self, parent):
        label = ttk.Label(parent, text="MAC5", anchor="center")
        label.place(x=190, y=15, width=100, height=20)
        return label

    def __tk_label_label_info_6(self, parent):
        label = ttk.Label(parent, text="MAC6", anchor="center")
        label.place(x=190, y=45, width=100, height=20)
        return label

    def __tk_label_label_info_7(self, parent):
        label = ttk.Label(parent, text="MAC7", anchor="center")
        label.place(x=190, y=75, width=100, height=20)
        return label

    def __tk_label_label_info_8(self, parent):
        label = ttk.Label(parent, text="MAC8", anchor="center")
        label.place(x=190, y=105, width=100, height=20)
        return label

    def __tk_input_input_info_1(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=80, y=10, width=100, height=25)
        return ipt

    def __tk_input_input_info_2(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=80, y=40, width=100, height=25)
        return ipt

    def __tk_input_input_info_3(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=80, y=70, width=100, height=25)
        return ipt

    def __tk_input_input_info_4(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=80, y=100, width=100, height=25)
        return ipt

    def __tk_input_input_info_5(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=270, y=10, width=100, height=25)
        return ipt

    def __tk_input_input_info_6(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=270, y=40, width=100, height=25)
        return ipt

    def __tk_input_input_info_7(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=270, y=70, width=100, height=25)
        return ipt

    def __tk_input_input_info_8(self, parent):
        ipt = ttk.Entry(parent)
        ipt.place(x=270, y=100, width=100, height=25)
        return ipt

    def __tk_text_text_folder(self, parent):
        text = ttk.Entry(parent)
        text.place(x=500, y=15, width=500, height=30)
        return text

    def __tk_button_button_file(self, parent):
        btn = ttk.Button(parent, bootstyle='link', image='folder_30_y', compound=RIGHT)
        btn.place(x=410, y=10, width=90, height=35)
        return btn

    def __tk_button_test(self, parent):
        btn = ttk.Button(parent, text="Test", takefocus=False, bootstyle="primary-outline")
        btn.place(x=845, y=69, width=150, height=45)
        return btn

    def __tk_button_button_login(self, parent):
        btn = ttk.Button(parent, text="Login", takefocus=False, bootstyle="primary-outline")
        btn.place(x=645, y=70, width=150, height=45)
        return btn

    def __tk_label_label_login(self, parent):
        label = ttk.Label(parent, text="Login_user", anchor='center')
        label.place(x=420, y=70, width=180, height=45)
        return label

    def __tk_frame_Contain_3(self, parent):
        frame = ttk.Frame(parent)
        frame.place(x=0, y=197, width=676, height=424)
        return frame

    def __tk_tabs_tab_log(self, parent):
        frame = ttk.Notebook(parent, bootstyle="info")
        self.tk_tabs_tab_log_1 = self.__tk_frame_tab_log_1(frame)
        frame.add(self.tk_tabs_tab_log_1, text="#1")
        self.tk_tabs_tab_log_2 = self.__tk_frame_tab_log_2(frame)
        frame.add(self.tk_tabs_tab_log_2, text="#2")
        self.tk_tabs_tab_log_3 = self.__tk_frame_tab_log_3(frame)
        frame.add(self.tk_tabs_tab_log_3, text="#3")
        self.tk_tabs_tab_log_4 = self.__tk_frame_tab_log_4(frame)
        frame.add(self.tk_tabs_tab_log_4, text="#4")
        self.tk_tabs_tab_log_5 = self.__tk_frame_tab_log_5(frame)
        frame.add(self.tk_tabs_tab_log_5, text="#5")
        self.tk_tabs_tab_log_6 = self.__tk_frame_tab_log_6(frame)
        frame.add(self.tk_tabs_tab_log_6, text="#6")
        self.tk_tabs_tab_log_7 = self.__tk_frame_tab_log_7(frame)
        frame.add(self.tk_tabs_tab_log_7, text="#7")
        self.tk_tabs_tab_log_8 = self.__tk_frame_tab_log_8(frame)
        frame.add(self.tk_tabs_tab_log_8, text="#8")
        frame.place(x=0, y=0, width=675, height=420)
        return frame

    def __tk_frame_tab_log_1(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_text_text_log_1(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_2(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_3(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_4(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_5(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_6(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_7(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_text_text_log_8(self, parent):
        text = ScrolledText(parent)
        text.place(x=0, y=0, width=675, height=420)
        return text

    def __tk_frame_tab_log_2(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_log_3(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_log_4(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_log_5(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_log_6(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_log_7(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_log_8(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_tabs_tab_1(self, parent):
        frame = ttk.Notebook(parent, bootstyle="primary")
        self.tk_tabs_tab_1_1 = self.__tk_frame_tab_1_1(frame)
        frame.add(self.tk_tabs_tab_1_1, text="#1")
        self.tk_tabs_tab_1_2 = self.__tk_frame_tab_1_2(frame)
        frame.add(self.tk_tabs_tab_1_2, text="#2")
        self.tk_tabs_tab_1_3 = self.__tk_frame_tab_1_3(frame)
        frame.add(self.tk_tabs_tab_1_3, text="#3")
        self.tk_tabs_tab_1_4 = self.__tk_frame_tab_1_4(frame)
        frame.add(self.tk_tabs_tab_1_3, text="#4")
        self.tk_tabs_tab_1_5 = self.__tk_frame_tab_1_5(frame)
        frame.add(self.tk_tabs_tab_1_5, text="#5")
        self.tk_tabs_tab_1_6 = self.__tk_frame_tab_1_6(frame)
        frame.add(self.tk_tabs_tab_1_6, text="#6")
        self.tk_tabs_tab_1_7 = self.__tk_frame_tab_1_7(frame)
        frame.add(self.tk_tabs_tab_1_7, text="#7")
        self.tk_tabs_tab_1_8 = self.__tk_frame_tab_1_8(frame)
        frame.add(self.tk_tabs_tab_1_8, text="#8")
        frame.place(x=682, y=197, width=335, height=163)
        return frame

    def __tk_frame_tab_1_1(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_2(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_3(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_4(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_5(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_6(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_7(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_frame_tab_1_8(self, parent):
        frame = ttk.Frame(parent)
        return frame

    def __tk_meter_dl_1(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_1(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Upload Speed",
                          textfont='-size 10',
                          bootstyle="success",
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_2(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_2(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_3(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_3(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_4(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_4(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_5(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_5(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_6(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_6(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_7(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_7(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_meter_dl_8(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          subtextstyle="primary",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=0, y=0, width=150, height=150)
        return meter

    def __tk_meter_up_8(self, parent):
        meter = ttk.Meter(parent, metersize=140,
                          padding=5,
                          amountused=100,
                          amounttotal=1000,
                          metertype="semi",
                          subtext="Download Speed",
                          textfont='-size 10',
                          bootstyle='success',
                          subtextstyle="success",
                          interactive=False,
                          textright="Mbps",
                          stripethickness=10,
                          stepsize=1)
        meter.place(x=180, y=0, width=150, height=150)
        return meter

    def __tk_table_table_1(self, parent):
        # 表头字段 表头宽度
        columns = {"#1": 42, "#2": 42, "#3": 42, "#4": 42, "#5": 42, "#6": 42, "#7": 42, "#8": 42}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), bootstyle="primary")
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        tk_table.place(x=682, y=366, width=338, height=108)
        return tk_table

    def __tk_progressbar_prog_1(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=475, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_2(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=490, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_3(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=505, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_4(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=520, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_5(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=535, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_6(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=550, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_7(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=565, width=260, height=10)
        return progressbar

    def __tk_progressbar_prog_8(self, parent):
        progressbar = ttk.Floodgauge(parent, font=(None, 6), bootstyle="success")
        progressbar.place(x=760, y=580, width=260, height=10)
        return progressbar

    def __tk_label_label_prog_b_1(self, parent):
        label_1 = ttk.Label(parent, image="point_10_b", compound="left")
        label_1.place(x=690, y=474, width=12, height=12)
        return label_1

    def __tk_label_label_prog_r_1(self, parent):
        label_1 = ttk.Label(parent, image="point_10_r", compound="left")
        label_1.place(x=705, y=474, width=12, height=12)
        return label_1

    def __tk_label_label_prog_g_1(self, parent):
        label_1 = ttk.Label(parent, image="point_10_g", compound="left")
        label_1.place(x=720, y=474, width=12, height=12)
        return label_1

    def __tk_label_label_prog_b_2(self, parent):
        label_2 = ttk.Label(parent, image="point_10_b", compound="left")
        label_2.place(x=690, y=487, width=12, height=12)
        return label_2

    def __tk_label_label_prog_r_2(self, parent):
        label_2 = ttk.Label(parent, image="point_10_r", compound="left")
        label_2.place(x=705, y=487, width=12, height=12)
        return label_2

    def __tk_label_label_prog_g_2(self, parent):
        label_2 = ttk.Label(parent, image="point_10_g", compound="left")
        label_2.place(x=720, y=487, width=12, height=12)
        return label_2

    def __tk_label_label_prog_b_3(self, parent):
        label_3 = ttk.Label(parent, image="point_10_b", compound="left")
        label_3.place(x=690, y=502, width=12, height=12)
        return label_3

    def __tk_label_label_prog_r_3(self, parent):
        label_3 = ttk.Label(parent, image="point_10_r", compound="left")
        label_3.place(x=705, y=502, width=12, height=12)
        return label_3

    def __tk_label_label_prog_g_3(self, parent):
        label_3 = ttk.Label(parent, image="point_10_g", compound="left")
        label_3.place(x=720, y=502, width=12, height=12)
        return label_3

    def __tk_label_label_prog_b_4(self, parent):
        label_4 = ttk.Label(parent, image="point_10_b", compound="left")
        label_4.place(x=690, y=517, width=12, height=12)
        return label_4

    def __tk_label_label_prog_r_4(self, parent):
        label_4 = ttk.Label(parent, image="point_10_r", compound="left")
        label_4.place(x=705, y=517, width=12, height=12)
        return label_4

    def __tk_label_label_prog_g_4(self, parent):
        label_4 = ttk.Label(parent, image="point_10_g", compound="left")
        label_4.place(x=720, y=517, width=12, height=12)
        return label_4

    def __tk_label_label_prog_b_5(self, parent):
        label_5 = ttk.Label(parent, image="point_10_b", compound="left")
        label_5.place(x=690, y=531, width=12, height=12)
        return label_5

    def __tk_label_label_prog_r_5(self, parent):
        label_5 = ttk.Label(parent, image="point_10_r", compound="left")
        label_5.place(x=705, y=531, width=12, height=12)
        return label_5

    def __tk_label_label_prog_g_5(self, parent):
        label_5 = ttk.Label(parent, image="point_10_g", compound="left")
        label_5.place(x=720, y=531, width=12, height=12)
        return label_5

    def __tk_label_label_prog_b_6(self, parent):
        label_6 = ttk.Label(parent, image="point_10_b", compound="left")
        label_6.place(x=690, y=547, width=12, height=12)
        return label_6

    def __tk_label_label_prog_r_6(self, parent):
        label_6 = ttk.Label(parent, image="point_10_r", compound="left")
        label_6.place(x=705, y=547, width=12, height=12)
        return label_6

    def __tk_label_label_prog_g_6(self, parent):
        label_6 = ttk.Label(parent, image="point_10_g", compound="left")
        label_6.place(x=720, y=547, width=12, height=12)
        return label_6

    def __tk_label_label_prog_b_7(self, parent):
        label_7 = ttk.Label(parent, image="point_10_b", compound="left")
        label_7.place(x=690, y=562, width=12, height=12)
        return label_7

    def __tk_label_label_prog_r_7(self, parent):
        label_7 = ttk.Label(parent, image="point_10_r", compound="left")
        label_7.place(x=705, y=562, width=12, height=12)
        return label_7

    def __tk_label_label_prog_g_7(self, parent):
        label_7 = ttk.Label(parent, image="point_10_g", compound="left")
        label_7.place(x=720, y=562, width=12, height=12)
        return label_7

    def __tk_label_label_prog_b_8(self, parent):
        label_8 = ttk.Label(parent, image="point_10_b", compound="left")
        label_8.place(x=690, y=577, width=12, height=12)
        return label_8

    def __tk_label_label_prog_r_8(self, parent):
        label_8 = ttk.Label(parent, image="point_10_r", compound="left")
        label_8.place(x=705, y=577, width=12, height=12)
        return label_8

    def __tk_label_label_prog_g_8(self, parent):
        label_8 = ttk.Label(parent, image="point_10_g", compound="left")
        label_8.place(x=720, y=577, width=12, height=12)
        return label_8

    def __tk_date_select_box(self, parent):
        date = ttk.DateEntry(parent, bootstyle='primary')
        date.place(x=840, y=598, width=180, height=28)
        return date

    def __tk_text_other_text(self, parent):
        text = ttk.Entry(parent, bootstyle='primary')
        text.place(x=680, y=598, width=150, height=28)
        return text


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)
        self.update_time()

    def __event_bind(self):
        self.tk_button_button_file.bind("<Button-1>", lambda event: self.ctl.open_filename(event))
        self.tk_button_button_login.bind("<Button-1>", lambda event: self.ctl.open_login_dialog(event))
        # self.tk_button_test.bind("<Button-1>", lambda event: self.ctl.set_input_info_text_clear(event, 1))
        # self.tk_button_test.bind("<Button-1>", lambda event: self.ctl.update_meter_value(event, "dl", 1, 700))
        self.tk_button_test.bind("<Button-1>", lambda event: self.ctl.set_log_text(event,  1, "test_log_print"))
        # self.tk_button_test.bind("<Button-1>", self.test_progress)
        self.tk_select_box_theme_list.bind("<<ComboboxSelected>>", self.ctl.change_theme)
        self.tk_input_input_info_1.bind("<Return>", self.ctl.run_test_main_1)
        self.tk_input_input_info_2.bind("<Return>", self.ctl.run_test_main_2)
        # self.tk_input_input_info_1.bind("<Return>", lambda event: self.test_messagebox(event))

    def update_time(self):
        self.ctl.set_current_time()
        self.after(1000, self.update_time)

    def test_progress(self, event):
        # self.tk_progressbar_prog_1.start()
        # self.tk_progressbar_prog_1.stop()
        self.tk_progressbar_prog_1.configure(value=60)
        print("debug gugua")
        # self.tk_progressbar_prog_1.configure(mask='{} %'.format(self.tk_progressbar_prog_1['value']))  # 更新mask
        print("debug gugua2")
        self.tk_progressbar_prog_1.update()


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
