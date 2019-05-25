#author：zhangyazhong
#time：2019-5-24
import re
import os

filename = "students.txt"


# 学生信息保存到文件
def save(studentList):
    try:
        student_text = open(filename, "a")  # 追加模式
    except Exception as e:
        student_text = open(filename, "w")  # 文件不存在，创建并打开
    for info in studentList:
        student_text.write(str(info) + "\n")

    student_text.close()

#主菜单
def menu():
    print('''
    ╔———————学生信息管理系统————————---------------╗
    │                                            │
    │   =============== 功能菜单 ===============  │
    │                                            │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                    │
    │   6 统计学生总人数                            │
    │   7 显示所有学生信息                          │
    │   0 退出系统                                 │
    │  ========================================== │
    │  说明：通过数字或↑↓方向键选择菜单               │
    ╚——————————————————————----------------------—╝
    ''')                              

#插入学生信息
def insert():
    studenList = []
    mark = True

    while mark:
        id = input("请输入学生ID（如100）:")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩:"))
            python  = int(input("请输入python成绩："))
            c       = int(input("请输入c语言成绩"))
        except:
            print("输入无效，不是整形数值！请重新输入---")
            continue
        student = {"id":id, "name":name, "english":english, "python":python, "c":c}
        studenList.append(student)

        inputMark = input("是否继续添加？（y/n）：")
        if inputMark is "y":
            mark = True
        else:
            mark = False

        save(studenList) #将学生信息保存到文件
        print("学生信息录入完毕！")


# 将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:
        print("*-*无数据信息*-*")
        return
    format_title = "{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t"
    format_data = "{:^6}\t{:^13}\t{:^12}\t{:^12}\t{:^5}\t{:^12}\t"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), info.get("english"), info.get("python"), info.get("c"),
                                 info.get("english") + info.get("python") + info.get("c")))


#查找
def search():
    mark = True
    student_query = []# 保存查询结果的学生列表
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input('''
             按ID查输入1:
             按姓名查输入2：
                        ''')
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生名字：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename, "r") as file:
                students = file.readlines()
                for list in students:
                    d = dict(eval(list)) # 字符串转字典
                    if id is not "":
                        if d['id'] == id:
                            student_query.append(d)
                    elif name is not None:
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询？y/n：")
                if inputMark == "y":
                    mark = True
                elif inputMark == 'n':
                    mark = False
        else:
            print("暂时没有数据可查询----")
            return




#删除
def delete():
    mark = True
    while mark:
        id = input("请输入您要删除的学生ID：")
        if id is not "":
            if os.path.exists(filename):
                with open(filename, "r") as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, "w") as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['id'] != id:
                            wfile.write(str(d) + "\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % id)
                    else:
                        print("未找到ID为%s的学生信息！" % id)
            else:
                print("无学生信息")
                break
            show()
            inputMark = input("是否继续删除？y/n:")
            if inputMark is "y":
                mark = True
            elif inputMark is "n":
                mark = False




#修改
def modify():
    show()
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()

    else :
        return

    studentId = input("请输入要修改的学生ID“")

    with open(filename, 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d['id'] == studentId:
                print("学生已经找到，请修改！")
                while True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d["c"] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入...")
                    else:
                        break
                student = str(d)
                wfile.write(student + "\n")
                print("修改成功！")
            else:
                wfile.write(student)
    mark = input("是否继续修改其他学生信息？y/n：")
    if mark is 'y':
        modify()
    else:
        return



#对学生成绩排序
def sort():
    show()

    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)


    ascOrdesc = input("请选择（0：升序；1：降序）：")
    if ascOrdesc == "0":
        ascOrdescBool = False     # 标记变量，为False表示升序排序
    elif ascOrdesc == "1":
        ascOrdescBool = True
    else:

        print("您的输入有误，请重新输入...")
        sort()

    mode = input("请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）：")
    if mode == "1":
        student_new.sort(key=lambda x:x['english'], reverse=ascOrdescBool)
    elif mode == "2":
        student_new.sort(key=lambda x:x['python'], reverse=ascOrdescBool)
    elif mode == "3":
        student_new.sort(key=lambda x: x['c'], reverse=ascOrdescBool)
    elif mode == "0":
        student_new.sort(key=lambda x: x['python'] + x['english'] + x['c'], reverse=ascOrdescBool)
    else:
        print("您的输入有误，请重新输入...")

    show_student(student_new)





#统计
def total():
    if os.path.exists(filename):
        with open(filename, "r" ) as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("一共有%d名学生" % len(student_old))
            else:
                print("还没有录入信息...")
    else:
        print("无保存数据")

#展示所有信息
def show():
    student_show = []
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_show.append(eval(list))
        if student_show:
            show_student(student_show)
    else:
        print("无数据保存！")


def main():
    ctrl = True #是否在系统内
    
    while (ctrl):
        menu()
        options = input("请选择：")
        option_str = re.sub("\D", "", options)
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option_str)
            if option_int == 0:
                print("您已经退出学生信息管理系统")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()
                
        else:
            print("请输入正确的数字！")    
            
        
if __name__ == '__main__':
    main()
