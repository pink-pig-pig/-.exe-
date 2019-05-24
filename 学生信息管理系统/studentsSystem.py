import re
#主菜单
def menu():
    print("【----------------------------学生信息管理系统-------------------------------】")      
    print("【                             0: 退出该系统                                ")                              
    print("【                             1：插入学生信息                              ") 
    print("【                             2：查找学生信息                              ")  
    print("【                             3：删除学生信息                              ")  
    print("【                             4：修改学生信息                              ")  
    print("【                             5：排序                                     ")  
    print("【                             6：统计                                     ")  
    print("【                             7：展示所有信息                              ") 
    print("【         使用中有任何问题，可以重新登录来解决，万能解决方法                   】")                               
                                    

#插入学生信息
def insert():
    pass
#查找
def search():
    pass
#删除
def delete():
    pass
#修改
def modify():
    pass
#对学生成绩排序
def sort():
    pass
#统计
def total():
    pass
#展示所有信息
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
            
        
main()