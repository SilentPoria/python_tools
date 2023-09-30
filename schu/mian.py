import tkinter as tk#tkinter库
import time#时间库
import datetime
import json

with open('lesson.json','r',encoding='utf8') as f:
    lesson = json.loads(f.read())

def get_time():# 每隔1s调用函数 gettime 自身获取时间
    weekday_num = datetime.datetime.now().weekday()
    weekday = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期七']
    var.set(' ' + '当前时间:' + time.strftime("%H:%M:%S") + ' ' + weekday[weekday_num])  # 获取当前时间
    root.after(1000, get_time)

def shou_lesson():
    weekday_num = datetime.datetime.now().weekday()
    weekday = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期七']
    for i in lesson[weekday[weekday_num]]:
        n_time = datetime.datetime.now()        # 当前时间
        start_time = lesson[weekday[weekday_num]][i]['start_time']
        end_time = lesson[weekday[weekday_num]][i]['end_time']
        d_time_start = datetime.datetime.strptime(str(datetime.datetime.now().date()) + start_time, '%Y-%m-%d%H:%M')
        d_time_end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + end_time, '%Y-%m-%d%H:%M')
        if n_time > d_time_start and n_time < d_time_end:
            color = 'red'
        else:
            color ='blue'
        print(lesson[weekday[weekday_num]][i]['name'])
        tk.Label(root, text=lesson[weekday[weekday_num]][i]['name'], fg=color, font=("微软雅黑", 10)).grid(row=0,column=int(i) + 1)
        print(int(i)+1)
    root.after(60000, shou_lesson)
#获取时间
def update_text():
    get_time()
    shou_lesson()


#退出
def myquit(*args):
    root.destroy()

#窗口拖动
def StartMove(event):
    global x, y
    x = event.x
    y = event.y
def StopMove(event):
    global x, y
    x = None
    y = None
def OnMotion(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    root.geometry("+%s+%s" % (root.winfo_x() + deltax, root.winfo_y() + deltay))
    root.update()
    print('当前坐标',event.x, event.y, root.winfo_x(), root.winfo_y(), root.winfo_width(), root.winfo_height())




#创建窗口
root = tk.Tk()
# 设置窗口标题
root.title('test')
root.geometry('400x25')
# 创建Label对象，第一个参数指定该Label放入root
var = tk.StringVar()
w = tk.Label(root, text="Hello Python!", textvariable=var, fg='blue', font=("微软雅黑", 10))
update_text()


root.overrideredirect(1)                 # 去除窗口边框
root.wm_attributes("-alpha", 1)        # 透明度(0.0~1.0)
root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
root.wm_attributes("-topmost", True)     # 永远处于顶层




root.bind("<ButtonPress-1>", StartMove)  # 监听左键按下操作响应函数
root.bind("<ButtonRelease-1>", StopMove)  # 监听左键松开操作响应函数
root.bind("<B1-Motion>", OnMotion)  # 监听鼠标移动操作响应函数
# 测试用途
# 调用pack进行布局
w.grid(row=0,column=0)




# 启动主窗口的消息循环
root.mainloop()
