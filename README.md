# by_python_gui
ttkboostrap（tkinter）gui demo 
Add guague and meter widget
Add all bind test method 
参照了后端开发中常用的 MVC 架构，我将代码重新分为了四个部分，程序入口、UI、窗口控制器、服务。
这样每一层的变化都不会影响下一层，如果UI布局发生了变化，只需替换UI文件即可。

当前示例项目，分为三个文件 main.py ，ui.py， controller.py

分别是入口文件、界面文件，界面控制器。在controller 中可以导入其他的测试function 或者py文件，这样可以直接更省心，当然ui界面的动作和控制可以修改。
另外采用了异步和多线程的方式，让程序运行不阻塞和加快效率。


