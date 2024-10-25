from ui import Win
# 导入UI 将 Controller 的属性 ui 类型设置成 Win
from test_1 import test_1
from test_2 import test_2
import asyncio
from check_re import check_re
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog
from ui_son import Son_WinGUI
from datetime import datetime
from ui_logger import get_logger
import threading


class test_reuslt:
    @staticmethod
    def get_result_sync(logger, log_widget, asyncfunction):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(test_reuslt.get_result_async(logger, log_widget, asyncfunction))
        loop.close()
        return result

    @staticmethod
    async def get_result_async(logger, log_widget, asyncfunction):
        print("get test result")
        try:
            result = await asyncfunction(logger, log_widget)
            if result is True:
                return True
            elif result is False:
                return False
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win

    def __init__(self):
        self.pass_conut_1 = 0
        self.fail_count_1 = 0
        self.total_cout_1 = 0
        self.num_test_1 = 0
        self.dict_test_1 = {"Test_num": self.num_test_1, "Pass_count": self.pass_conut_1,
                            "Fail_count": self.fail_count_1, "Total_count": self.total_cout_1}
        self.result_1 = None  # 初始化 result 为 None
        self.pass_conut_2 = 0
        self.fail_count_2 = 0
        self.total_cout_2 = 0
        self.num_test_2 = 0
        self.dict_test_2 = {"Test_num": self.num_test_2, "Pass_count": self.pass_conut_2,
                            "Fail_count": self.fail_count_2, "Total_count": self.total_cout_2}
        self.result_2 = None  # 初始化 result 为 None
        self.logger = get_logger()
        self.thread1_running = threading.Event()
        self.thread2_running = threading.Event()

    def set_current_time(self):
        # 获取当前时间
        now = datetime.now()
        # 格式化时间字符串
        time_str = now.strftime("%H:%M:%S")
        self.ui.tk_text_other_text.delete(0, 'end')
        self.ui.tk_text_other_text.insert("end", f"{time_str}")
        # self.ui.after(1000, lambda: self.set_current_time)
        return time_str

    def init(self, ui):
        """
        得到UI实例,对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def open_file(self, event):
        '''
        打开单个文件，返回文件对象，用于读取文件内容'''
        file_name = filedialog.askopenfile(title="opensigl file", filetypes=[(
            "Text files", "*.txt"), ("Excel Files", "*.xls"), ("Excel Files", "*.xlsx")], initialdir='c:/')
        print(file_name)
        return file_name

    # def open_file():
        # file_obj = filedialog.askopenfile(title="Open Signal File", filetypes=[
        #     ("Text files", "*.txt"), ("Excel Files", "*.xls"), ("Excel Files", "*.xlsx")], initialdir='c:/')
        # if file_obj:
        #     with file_obj:  # 使用 with 语句自动管理文件的打开和关闭
        #         content = file_obj.read()  # 读取文件的全部内容
        #         print(content)
        # else:
        #     print("No file selected")
        # return file_obj

    def open_files(self, event):
        # 调用askopenfiles方法获取多个打开的文件
        files_name = filedialog.askopenfiles(title='打开多个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],
                                             initialdir='d:/')
        print(files_name)
        return files_name

    def open_filename(self, event):
        # 调用askopenfilename方法获取单个文件的文件名
        file_name = filedialog.askopenfilename(title='打开单个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],
                                               initialdir='d:/')
        print(file_name)
        if file_name:
            self.ui.tk_text_text_folder.delete(0, 'end')
            self.ui.tk_text_text_folder.insert(0, file_name)
        return file_name

    def open_filenames(self, event):
        # 调用askopenfilenames方法获取多个文件的文件名
        file_names = filedialog.askopenfilenames(title='打开多个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],
                                                 initialdir='d:/')
        print(file_names)
        return file_names

    def tree_insert(self, evnt, *args):
        print("tree insert------")
        # print(evnt, args)
        self.ui.tk_table_table_1.insert("", "end", values=args)

    def change_theme(self, event) -> None:
        theme_cbo_value = self.ui.tk_select_box_theme_list.get()
        self.ui.style.theme_use(theme_cbo_value)
        self.ui.tk_select_box_theme_list.selection_clear()

    def update_table(self, event, row_index: int, column_index: int, value: int) -> None:
        """
        更新表格数据
        """
        # # 列表获取值，typing做int类型判断
        # fail_row = int(2)
        # pass_row = int(1)
        # total_row = int(0)

        # 获取所有列的名称
        columns = self.ui.tk_table_table_1.cget('columns')
        print(f"Columns: {columns}")

        # 获取所有行的 ID
        all_items = self.ui.tk_table_table_1.get_children()
        print(all_items)

        # 如果表格为空，先插入3行数据,可以根据自定义
        if not all_items:
            initial_data = [""] * len(columns)
            for _in in range(3):
                item_id = self.ui.tk_table_table_1.insert('', 'end', values=initial_data)
            all_items = [item_id]
            all_items = self.ui.tk_table_table_1.get_children()  # 重新获取所有行的 ID
            print(len(all_items))

        # # 检查行索引是否有效
        # if row_index < 0 or row_index >= len(all_items):
        #     print("Invalid row index.")
        #     return False

        # 获取指定行的数据
        item_id = all_items[row_index]
        current_values = list(self.ui.tk_table_table_1.item(item_id, "values"))

        # 检查列索引是否有效
        if column_index < 0 or column_index >= len(current_values):
            print("Invalid column index.")
            return False

        # 更新指定列的数据
        current_values[column_index] = value

        # 更新 Treeview 中的数据
        self.ui.tk_table_table_1.item(item_id, values=current_values)

        # 打印更新后的行数据
        updated_values = self.ui.tk_table_table_1.item(item_id, "values")
        print(f"Updated values: {updated_values}")
        print(f"update data is: {row_index + 1} row  {column_index +1} coulum {value} value")
        return updated_values

    def get_input_content(self, input) -> None:
        """
        获取输入框内容
        """
        input_content = input.get()
        return input_content

    def update_input_disable(self, input) -> None:
        """
        禁用输入框
        """
        print("disable input")
        input.config(state="disabled")

    def update_input_enable(self, input) -> None:
        print("enable input")
        input.config(state="normal")

    def upate_input_clear(self, input) -> None:
        print("Clear input")
        input.delete(0, 'end')

    def set_input_focus(self, position) -> None:
        """
        设置焦点
        """
        input_info_text = f"tk_input_input_info_{position}"
        input_info = getattr(self.ui, input_info_text)
        input_info.focus_set()

    def get_input_content_by_position(self, position) -> None:
        """
        获取输入框内容
        """
        input_info_text = f"tk_input_input_info_{position}"
        input_info = getattr(self.ui, input_info_text)
        return input_info.get()

    def set_input_info_text_disable(self, event, position) -> None:
        """
        禁用输入框
        """
        input_info_text = f"tk_input_input_info_{position}"
        input_info = getattr(self.ui, input_info_text)
        input_info.config(state="disabled")

    def set_input_info_text_enable(self, event, position) -> None:
        """
        启用输入框
        """
        input_info_text = f"tk_input_input_info_{position}"
        input_info = getattr(self.ui, input_info_text)
        input_info.config(state="normal")

    def set_input_info_text_clear(self, evnent, position) -> None:
        """
        清空输入框
        """
        input_info_text = f"tk_input_input_info_{position}"
        input_info = getattr(self.ui, input_info_text)
        input_info.delete(0, 'end')

    def update_label_no_img(self, label) -> None:
        """
        清除图片
        """
        label.config(image="")
        label.image = ""

    def set_prog_label_norg(self, event, position):
        """
        设置不显示红色和绿色图片
        """
        label_name_r = f"tk_label_label_prog_r_{position}"
        label_name_g = f"tk_label_label_prog_g_{position}"
        label_r = getattr(self.ui, label_name_r)
        label_g = getattr(self.ui, label_name_g)
        self.update_label_no_img(label_r)
        self.update_label_no_img(label_g)

    def set_prog_label_nob(self, event, position):
        """
        设置不显示蓝色图片
        """
        label_name_b = f"tk_label_label_prog_b_{position}"
        label_r = getattr(self.ui, label_name_b)
        self.update_label_no_img(label_r)

    def update_label_with_img(self, label, iamge_name) -> None:
        """
        设置图片
        """
        label.config(image=iamge_name)

    def set_prog_label_with_img(self, event, rgb, position,  image_name):
        """
        设置图片
        """
        label_name_text = f"tk_label_label_prog_{rgb}_{position}"
        label_name = getattr(self.ui, label_name_text)
        self.update_label_with_img(label_name, image_name)

    def update_progress(self, progress, progress_value):
        progress.configure(value=progress_value)
        progress.update()

    def set_progress_value(self, event, position, value):
        progress_name_text = f"tk_progressbar_prog_{position}"
        progress_name = getattr(self.ui, progress_name_text)
        progress_name.configure(value=value)
        # self.update_progress(progress_name, value)

    def show_message(self, info):
        Messagebox.show_info(info, "Info")

    def show_warning(self, waring_info):
        Messagebox.showwarning(waring_info, "Warning",)

    def show_error(self, error_info):
        Messagebox.showerror(error_info, "Error")

    def get_log_attr(self, position):
        log_text_name_text = f"tk_text_text_log_{position}"
        log_text_name = getattr(self.ui, log_text_name_text)
        return log_text_name

    def set_log_text(self, position, text):
        log_attr = self.get_log_attr(position)
        self.logger.log(text, log_attr)

    def open_login_dialog(self, event):
        Son_WinGUI(self, self.update_label)  # Pass the update_label method as a callback

    def update_label(self, username, password, event):
        self.ui.tk_label_label_login.config(text=f"Username: {username}")
        print(f"password: {password}")

    def update_meter_value(self, event, dlup: str, position: int, value: int):
        meter_name_text = f"tk_meter_{dlup}_{position}"
        meter_name = getattr(self.ui, meter_name_text)
        meter_name.configure(amountused=value)

    def test_main_1(self, event):
        try:
            self.perform_steps_1(event, 1)
        finally:
            self.thread1_running.clear()

    def perform_steps_1(self, event, step):
        if step == 1:
            mac1 = self.get_input_content_by_position(1)
            if check_re.is_valid_mac_address(mac1) is False:
                self.show_message("MAC address is invalid")
                self.set_input_info_text_clear(event, 1)
                self.set_input_focus(1)
                return
            else:
                self.set_log_text(1, "Begin Test...")
                self.set_log_text(1, "MAC1 is valid")
                self.set_log_text(1, "MAC1 is: " + mac1)
            self.set_input_info_text_disable(event, 1)
            self.set_progress_value(event, 1, 10)
            self.set_input_focus(2)
            self.ui.after(1000, lambda: self.perform_steps_1(event, 2))
        elif step == 2:
            log_attr_1 = self.get_log_attr(1)
            self.set_prog_label_norg(event, 1)
            self.set_log_text(1, "Testing...")
            self.result_1 = test_reuslt.get_result_sync(self.logger, log_attr_1, test_1.main_1)
            self.set_progress_value(event, 1, 50)
            self.ui.after(1000, lambda: self.perform_steps_1(event, 3))
        elif step == 3:
            if self.result_1 is True:
                self.set_prog_label_with_img(event, "g", 1, "point_10_g")
                self.set_prog_label_nob(event, 1)
                self.set_progress_value(event, 1, 100)
                self.pass_conut_1 += 1
                self.total_cout_1 += 1
                self.num_test_1 = 1
                print(self.pass_conut_1)
                self.update_table(event, 0, 0, self.pass_conut_1)
                self.update_table(event, 1, 0, self.fail_count_1)
                self.update_table(event, 2, 0, self.total_cout_1)
                self.dict_test_1.update({"Test_num": self.num_test_1, "Pass_count": self.pass_conut_1,
                                         "Fail_count": self.fail_count_1, "Total_count": self.total_cout_1})
                self.set_input_info_text_enable(event, 1)
                self.update_meter_value(event, "dl", 1, 800)
                self.set_input_info_text_clear(event, 1)
                self.set_input_focus(1)
            else:
                print("Test Fail.........")
                self.set_prog_label_with_img(event, "r", 1, "point_10_r")
                self.set_prog_label_nob(event, 1)
                self.fail_conut_1 += 1
                self.total_cout_1 += 1
                self.update_table(event, 0, 0, self.pass_conut_1)
                self.update_table(event, 1, 0, self.fail_count_1)
                self.update_table(event, 2, 0, self.total_cout_1)
                self.dict_test_1.update({"Test_num": self.num_test_1, "Pass_count": self.pass_conut_1,
                                         "Fail_count": self.fail_count_1, "Total_count": self.total_cout_1})
                self.set_input_info_text_enable(event, 1)
                self.set_input_info_text_clear(event, 1)
                self.set_input_focus(1)

    def run_test_main_1(self, event):
        '''
        使用 threading.Event 来管理线程状态，并确保 UI 保持响应性。
        '''
        if not self.thread1_running.is_set():
            self.thread1_running.set()
            thread1 = threading.Thread(target=self.test_main_1, args=(event,))
            thread1.start()
            # thread1.join() 会阻塞进程

    def test_main_2(self, event):
        try:
            self.perform_steps_2(event, 1)
        finally:
            self.thread2_running.clear()

    def perform_steps_2(self, event, step):
        if step == 1:
            mac2 = self.get_input_content_by_position(2)
            if check_re.is_valid_mac_address(mac2) is False:
                self.show_message("MAC address is invalid")
                self.set_input_info_text_clear(event, 2)
                self.set_input_focus(1)
                return
            else:
                self.set_log_text(2, "Begin Test...")
                self.set_log_text(2, "MAC2 is valid")
                self.set_log_text(2, "MAC2 is: " + mac2)
            self.set_input_info_text_disable(event, 2)
            self.set_progress_value(event, 2, 10)
            self.set_input_focus(3)
            self.ui.after(1000, lambda: self.perform_steps_2(event, 2))
        elif step == 2:
            log_attr_2 = self.get_log_attr(2)
            self.set_prog_label_norg(event, 2)
            self.set_log_text(2, "Testing...")
            self.result_2 = test_reuslt.get_result_sync(self.logger, log_attr_2, test_2.main_2)
            self.set_progress_value(event, 2, 50)
            self.ui.after(1000, lambda: self.perform_steps_2(event, 3))
        elif step == 3:
            if self.result_2 is True:
                self.set_prog_label_with_img(event, "g", 2, "point_10_g")
                self.set_prog_label_nob(event, 2)
                self.set_progress_value(event, 2, 100)
                self.pass_conut_2 += 1
                self.total_cout_2 += 1
                self.num_test_2 = 2
                print(self.pass_conut_2)
                self.update_table(event, 0, 1, self.pass_conut_2)
                self.update_table(event, 1, 1, self.fail_count_2)
                self.update_table(event, 2, 1, self.total_cout_2)
                self.dict_test_2.update({"Test_num": self.num_test_2, "Pass_count": self.pass_conut_2,
                                         "Fail_count": self.fail_count_2, "Total_count": self.total_cout_2})
                self.set_input_info_text_enable(event, 2)
                self.update_meter_value(event, "dl", 2, 800)
                self.set_input_info_text_clear(event, 2)
                self.set_input_focus(2)
            else:
                print("Test Fail.........")
                self.set_prog_label_with_img(event, "r", 2, "point_10_r")
                self.set_prog_label_nob(event, 2)
                self.fail_conut_2 += 1
                self.total_cout_2 += 1
                self.update_table(event, 0, 1, self.pass_conut_2)
                self.update_table(event, 1, 1, self.fail_count_2)
                self.update_table(event, 2, 1, self.total_cout_2)
                self.dict_test_2.update({"Test_num": self.num_test_2, "Pass_count": self.pass_conut_2,
                                         "Fail_count": self.fail_count_2, "Total_count": self.total_cout_2})
                self.set_input_info_text_enable(event, 2)
                self.set_input_info_text_clear(event, 2)
                self.set_input_focus(2)

    def run_test_main_2(self, event):
        if not self.thread2_running.is_set():
            self.thread2_running.set()
            thread2 = threading.Thread(target=self.test_main_2, args=(event,))
            thread2.start()
