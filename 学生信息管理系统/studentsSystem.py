
import re
def menu():
    pass

def insert():
    pass

def search():
    pass

def delete():
    pass

def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass

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
            
        