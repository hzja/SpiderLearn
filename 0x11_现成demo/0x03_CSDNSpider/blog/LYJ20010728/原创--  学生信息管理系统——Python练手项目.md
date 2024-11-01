# 原创
：  学生信息管理系统——Python练手项目

# 学生信息管理系统——Python练手项目

### 简易版本学生信息管理系统

**程序源码**

```
import os

filename = 'Student_information.txt'        # 全局定义文件名

def main():
    while True:
        menm()
        choice = int(input('请选择您要进行的操作：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                # 确认是否真正要提出系统
                answer = input('您确定要退出系统嘛？(Y/N) ')
                if answer.upper() == 'Y':
                    print('感谢您的使用！')
                    break       # 退出系统
                else:
                    continue    # 继续使用
            elif choice == 1:
                insert()        # 录入学生信息
            elif choice == 2:
                find()          # 查找学生信息
            elif choice == 3:
                delete()        # 删除学生信息
            elif choice == 4:
                modify()        # 修改学生信息
            elif choice == 5:
                sort()          # 学生信息排序
            elif choice == 6:
                total()         # 统计学生信息
            elif choice == 7:
                show()          # 显示学生信息

def menm():
    print('=========================学生信息管理系统=========================\n')
    print('----------------------------功能菜单----------------------------')
    print('\t\t\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t\t\t 5.学生信息排序')
    print('\t\t\t\t\t\t 6.统计学生人数')
    print('\t\t\t\t\t\t 7.显示学生信息')
    print('\t\t\t\t\t\t 0.退出管理系统')
    print('--------------------------------------------------------------')

def insert():
    Student_list = []
    while True:
        Student_id = input('请输入学生的ID：')
        if not Student_id:
            break
        Student_name = input('请输入学生的姓名：')
        if not Student_name:
            break
        try:
            Python_grade = float(input('请输入学生的Python语言成绩：'))
            Java_grade = float(input('请输入学生的Java语言成绩：'))
            C_grade = float(input('请输入学生的C语言成绩：'))
            Go_grade = float(input('请输入学生的Go语言成绩:'))
        except:
            print('输入成绩错误，不是浮点数float类型，请重新输入！')
            continue
        # 将录入的学生成绩保存到字典中
        Student_dict = {'id':Student_id,'name':Student_name,'Python':Python_grade,'Java':Java_grade,'C':C_grade,'Go':Go_grade}
        # 将学生信息添加到列表中
        Student_list.append(Student_dict)
        # 判断是否需要继续录入学生信息
        answer = input('是否继续添加学生信息？(Y/N) ')
        if answer.upper() == 'Y':
            continue
        else:
            break
    # 调用Save函数将学生信息保存到文档当中
    Save(Student_list)
    print('学生信息录入完毕！\n')

def Save(Things_list):
    try:
        Student_information = open(filename,'a',encoding='UTF-8')
    except:
        Student_information = open(filename,'w',encoding='UTF-8')
    for item in Things_list:
        Student_information.write(str(item) + '\n')
    Student_information.close()

def find():
    Student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            find_mode = input('按id查找请输入1 \ 按姓名查找请输入2：')
            if find_mode == '1':
                id = input('请输入学生ID：')
            elif find_mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                find()
            with open(filename,'r',encoding='UTF-8') as rfile:
                Student_old = rfile.readlines()
                for item in Student_old:
                    dict_find = dict(eval(item))
                    if dict_find['id'] == id:
                        Student_query.append(dict_find)
                    elif dict_find['name'] == name:
                        Student_query.append(dict_find)
            # 显示查询结果
            Show_student(Student_query)
            # 清空查询列表
            Student_query.clear()
            answer = input('是否继续查询学生信息？(Y/N) ')
            if answer.upper() == 'Y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息！')
            return

def Show_student(lst):
    if len(lst) == 0:
        print('未查询到学生信息！')
        return
    # 定义标题显示格式
    format_title = '{:^10}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^6}'
    print(format_title.format('ID','姓名','Python成绩','Java成绩','C语言成绩','Go语言成绩','总成绩'))
    # 定义内容的显示格式
    format_data = '{:^10}\t{:^6}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 item.get('C'),
                                 item.get('Go'),
                                 int(item.get('Python') + item.get('Java') + item.get('C') + item.get('Go'))
                                 ))

def delete():
    while True:
        Student_id_delete = input('请输入需要删除的学生ID：')
        if Student_id_delete != '':
            if os.path.exists(filename):
                with open(filename,'r',encoding='UTF-8') as file:
                    Student_old = file.readlines()
            else:
                Student_old = []
            flag = False         # 标记是否删除
            if Student_old:
                with open(filename,'w',encoding='UTF-8') as wfile:
                    dict_delete = {}
                    for item in Student_old:
                        dict_delete = dict(eval(item))    # 将字符串转成一个字典
                        if dict_delete['id'] != Student_id_delete:
                            wfile.write(str(dict_delete) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{Student_id_delete}的学生信息已被删除！\n')
                    else:
                        print(f'没有找到id{Student_id_delete}的学生信息！\n')
            else:
                print('无学生信息！\n')
                break
            show()              # 删除之后重新显示全部学生信息
            answer = input('是否继续删除学生信息？(Y/N) ')
            if answer.upper() == 'Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as rfile:
            Student_old = rfile.readlines()
    else:
        return
    Student_id_modify = input('请输入待修改学生学生信息的学生ID：')
    with open(filename,'w',encoding='UTF-8') as wfile:
        for item in Student_old:
            dict_modify = dict(eval(item))
            if dict_modify['id'] == Student_id_modify:
                print('学生信息已找到，可以开始修改其学生信息！')
                while True:
                    try:
                        dict_modify['name'] = input('请输入学生姓名：')
                        dict_modify['Python'] = float(input('请输入学生的Python语言成绩：'))
                        dict_modify['Java'] = float(input('请输入学生的Java语言成绩：'))
                        dict_modify['C'] = float(input('请输入学生的C语言成绩：'))
                        dict_modify['Go'] = float(input('请输入学生的Go语言成绩:'))
                    except:
                        print('您的输入有误，请重新输入！')
                    else:
                        break
                wfile.write(str(dict_modify) + '\n')
                print('修改完毕！')
            else:
                wfile.write(str(dict_modify) + '\n')
        answer = input('是否继续修改其它学生的学生信息？(Y/N) ')
        if answer.upper() == 'Y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as rfile:
            Student_lst = rfile.readlines()
        Student_new = []
        for item in Student_lst:
            dict_sort = dict(eval(item))
            Student_new.append(dict_sort)
    else:
        return
    answer_asc_or_desc = input('请选择(0.升序 1.降序)显示学生信息：')
    if answer_asc_or_desc == '0':
        answer_asc_or_desc_bool = False
    elif answer_asc_or_desc == '1':
        answer_asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    answer_mode = input('请选择排序方式(a.按Python成绩排序 b.按Java成绩排序 c.按C语言成绩排序 d.按Go语言成绩排序 e.按总成绩排序)：')
    if answer_mode == 'a':
        Student_new.sort(key=lambda any : int(any['Python']), reverse=answer_asc_or_desc_bool)
    elif answer_mode == 'b':
        Student_new.sort(key=lambda any : int(any['Java']), reverse=answer_asc_or_desc_bool)
    elif answer_mode == 'c':
        Student_new.sort(key=lambda any : int(any['C']), reverse=answer_asc_or_desc_bool)
    elif answer_mode == 'd':
        Student_new.sort(key=lambda any : int(any['Go']), reverse=answer_asc_or_desc_bool)
    elif answer_mode == 'e':
        Student_new.sort(key=lambda any : (int(any['Python']) + int(any['Java']) + int(any['C']) + int(any['Go'])), reverse=answer_asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    Show_student(Student_new)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as rfile:
            Student_old = rfile.readlines()
            if Student_old:
                print(f'学生管理系统存储了{len(Student_old)}名学生的信息\n')
            else:
                print('还未录入学生信息\n')
    else:
        print('暂未保存数据信息...\n')

def show():
    Student_lst = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as rfile:
            Student_old = rfile.readlines()
            for item in Student_old:
                Student_lst.append(eval(item))
            if Student_lst:
                Show_student(Student_lst)
    else:
        print('暂未保存数据信息...\n')

main()

```

**程序运行**

```
=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：1
请输入学生的ID：202017030103
请输入学生的姓名：奥特曼
请输入学生的Python语言成绩：100
请输入学生的Java语言成绩：87
请输入学生的C语言成绩：91
请输入学生的Go语言成绩:77
是否继续添加学生信息？(Y/N) n
学生信息录入完毕！

=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：6
学生管理系统存储了3名学生的信息

=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：7
    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030101	 张家梁  	  100.0   	   99.0   	  100.0   	   98.0   	  397   
202017030102	 冯昊昊  	  100.0   	   97.0   	   88.0   	   91.0   	  376   
202017030103	 奥特曼  	  100.0   	   87.0   	   91.0   	   77.0   	  355   
=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：2
按id查找请输入1 \ 按姓名查找请输入2：1
请输入学生ID：202017030101
    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030101	 张家梁  	  100.0   	   99.0   	  100.0   	   98.0   	  397   
是否继续查询学生信息？(Y/N) y
按id查找请输入1 \ 按姓名查找请输入2：2
请输入学生姓名：奥特曼
    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030103	 奥特曼  	  100.0   	   87.0   	   91.0   	   77.0   	  355   
是否继续查询学生信息？(Y/N) n
=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：3
请输入需要删除的学生ID：202017030103
id为202017030103的学生信息已被删除！

    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030101	 张家梁  	  100.0   	   99.0   	  100.0   	   98.0   	  397   
202017030102	 冯昊昊  	  100.0   	   97.0   	   88.0   	   91.0   	  376   
是否继续删除学生信息？(Y/N) n
=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：4
    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030101	 张家梁  	  100.0   	   99.0   	  100.0   	   98.0   	  397   
202017030102	 冯昊昊  	  100.0   	   97.0   	   88.0   	   91.0   	  376   
请输入待修改学生学生信息的学生ID：202017030102
学生信息已找到，可以开始修改其学生信息！
请输入学生姓名：刘浩浩
请输入学生的Python语言成绩：98
请输入学生的Java语言成绩：100
请输入学生的C语言成绩：99
请输入学生的Go语言成绩:100
修改完毕！
是否继续修改其它学生的学生信息？(Y/N) n
=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：5
    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030101	 张家梁  	  100.0   	   99.0   	  100.0   	   98.0   	  397   
202017030102	 刘浩浩  	   98.0   	  100.0   	   99.0   	  100.0   	  397   
请选择(0.升序 1.降序)显示学生信息：0
请选择排序方式(a.按Python成绩排序 b.按Java成绩排序 c.按C语言成绩排序 d.按Go语言成绩排序 e.按总成绩排序)：a
    ID    	     姓名     	Python成绩	 Java成绩 	 C语言成绩  	 Go语言成绩 	 总成绩  
202017030102	 刘浩浩  	   98.0   	  100.0   	   99.0   	  100.0   	  397   
202017030101	 张家梁  	  100.0   	   99.0   	  100.0   	   98.0   	  397   
=========================学生信息管理系统=========================

----------------------------功能菜单----------------------------
						 1.录入学生信息
						 2.查找学生信息
						 3.删除学生信息
						 4.修改学生信息
						 5.学生信息排序
						 6.统计学生人数
						 7.显示学生信息
						 0.退出管理系统
--------------------------------------------------------------
请选择您要进行的操作：0
您确定要退出系统嘛？(Y/N) y
感谢您的使用！

```
