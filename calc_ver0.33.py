#Program: MiniCalc, it is a minimalistic calculator for simple calculations.
#The main task of the author was to create a simple and convenient everyday tool 
#Author: Anastasiya Parnasova
#My contacts:
#anastasiya.parnasova@gmail.com
#https://github.com/parnasova
#https://parnasova.info
'''
Copyright (c) 2022 Anastasiya Parnasova

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

#Current version:
str_version = "0.33"

import customtkinter
import pyperclip
from math import modf

#Состояния программы
program_state = {
    0: "Start",
    1: "Var1",
    2: "Var2",
    3: "Oper",
    4: "Rez"
}

flag_statusbar_visible = True

current_state = program_state[0]

program_display = "0"

str_variable1 = ""
str_variable2 = ""
str_operation = ""

flag_point = False

#Окно с информацией о программе
def information_fun(event):
    str_about = ("Author: Anastasiya Parnasova\n"
                    "anastasiya.parnasova@gmail.com\n"
                    "https://github.com/parnasova\n"
                    "https://parnasova.info\n")
    str_keys = ("Keyboard shortcut:\n"
                    "\"0..9\" - number keys\n"
                    "\"+,-,*,/\" - mathematic operation\n"
                    "\"$\" - replace plus/minus\n"
                    "\".\" or \",\" - decimal fraction\n"
                    "\"Enter\" - get the result\n"
                    "\"Escape\" - reset\n"
                    "\"Delete\" or \"Backspace\" - delete\n"
                    "\"c\" - copying to the clipboard\n"
                    "\"s\" - hide/show status-bar\n"
                    "\"i\" - open this window\n"
                    "\"q\" - exit")
    
    info_window = customtkinter.CTkToplevel(root)
    info_window.geometry("300x400+600+400")
    info_window.title("Info")
    
    #Клавиша "q" для выхода из текущего окна
    info_window.bind("q", (lambda event: info_window.destroy()))
    
    #По клику мышью выходим из текущего окна
    info_window.bind("<Button-1>", (lambda event: info_window.destroy()))
    
    #Авторство
    author_label = customtkinter.CTkLabel(info_window, text_font=('Verdana', 9), text=str_about)
    author_label.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)
    
    #Горячие клавиши
    info_frame = customtkinter.CTkFrame(master=info_window,
                               width=250,
                               height=350,
                               corner_radius=5)
    info_frame.pack(side="top", anchor="e", expand=True, padx=20, pady=20)
    
    
    key_label = customtkinter.CTkLabel(info_frame, text_font=('Consolas', 11), text=str_keys)
    key_label.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)
    
    #Информируем пользователя, что окно закрывается по нажатию на него
    status = customtkinter.CTkLabel(
        master = info_window,
        text = "Click on the window to close it",
        anchor = customtkinter.W,
        text_font = ("Verdana", 8),
        fg_color = "#000000",
        bg_color = "#000000",
        width=350,
        height=25,
        text_color = "#FFFFFF")

    status.place(x=0, y=380)

#Прячем/показываем статусбар
def hide_status_fun(event):

    global flag_statusbar_visible
    
    flag_statusbar_visible = not flag_statusbar_visible
    
    if (flag_statusbar_visible):
    
        status.configure(width=350)
        status.configure(height=25)
        
    else:
    
        status.configure(text="")
    
        status.configure(width=0)
        status.configure(height=0)

#Показываем клавиатурные сокращения в статусной строке
#Информация, что строку можно убрать/показать клавишей "s"
#Также здесь есть сообщение, что дополнительную информацию о программе можно получить по клавише "i"
def statusbar_fun(str_wx, b_focus):

    global flag_statusbar_visible

    #print("str_wx = " + str_wx + ", b_focus = " + str(b_focus))
    
    str_status = ""
    
    if ((flag_statusbar_visible) and (b_focus)):
            
        if (str_wx == "0"):
            str_status = "Key: \"0\""
            
        if (str_wx == "1"):
            str_status = "Key: \"1\""
            
        if (str_wx == "2"):
            str_status = "Key: \"2\""
            
        if (str_wx == "3"):
            str_status = "Key: \"3\""
            
        if (str_wx == "4"):
            str_status = "Key: \"4\""
            
        if (str_wx == "5"):
            str_status = "Key: \"5\""
            
        if (str_wx == "6"):
            str_status = "Key: \"6\""
            
        if (str_wx == "7"):
            str_status = "Key: \"7\""
            
        if (str_wx == "8"):
            str_status = "Key: \"8\""
            
        if (str_wx == "9"):
            str_status = "Key: \"9\""
        
        if (str_wx == "sum"):
            str_status = "Key: \"+\""
            
        if (str_wx == "sub"):
            str_status = "Key: \"-\""
            
        if (str_wx == "mul"):
            str_status = "Key: \"*\""
            
        if (str_wx == "div"):
            str_status = "Key: \"/\""
            
        if (str_wx == "rst"):
            str_status = "Key: \"Escape\""
            
        if (str_wx == "del"):
            str_status = "Key: \"Delete\" or \"Backspace\""
            
        if (str_wx == "ent"):
            str_status = "Key: \"Enter\""
            
        if (str_wx == "cpy"):
            str_status = "Key: \"c\""
            
        if (str_wx == "p_or_m"):
            str_status = "Key: \"$\""
            
        if (str_wx == "pnt"):
            str_status = "Key: \".\" or \",\""
            
        if (str_wx == "stt"):
            str_status = "Press key \"s\" for open/hide this statusbar"
            
        if (str_wx == "ver"):
            str_status = "Press key \"i\" for more information"
            
    status.configure(text=str_status)
    

#Сброс состояния программы в ноль
def reset_fun():
    
    global current_state
    global program_display
    global str_variable1
    global str_variable2
    global str_operation
    global flag_point

    current_state = program_state[0]
    str_variable1 = ""
    str_variable2 = ""
    str_operation = ""
    program_display = "0"
    display.configure(text=program_display)
    flag_point = False

#Конвертор из числа с плавающей точкой в строку
#Вторым параметром задаётся степень округления дробной части числа
def convert_float_to_str(f_num, n_round = 2):

    #Устраняем дробную часть если имеем дело с целым числом
    #и наоборот для дробных чисел оставляем округлённую дробную часть
    f_int_frac = modf(f_num)
    
    if (f_int_frac[0] != 0):
    
        #Имеем в наличии дробную часть числа
        #Оставляем число как есть, только округляем дробную часть
        str_num = str(round(f_num, n_round))
        
    else:
        #Целое число без дробной части
        str_num = str(int(f_int_frac[1]))
    
    return str_num

#Имея на руках все данные(мы проверим это) вычисляем результат
def calc_fun(str_var1, str_var2, str_oper):

    #showinfo(title="Debug", message=str_var1)
    #showinfo(title="Debug", message=str_var2)
    #showinfo(title="Debug", message=str_oper)

    #Если ничего не вышло
    str_rez = "error"
    
    #Все ли данные есть?
    if ((len(str_var1) == 0) or (len(str_oper) == 0) or (len(str_var2) == 0) or
        (str_var1.isspace()) or (str_oper.isspace()) or (str_var2.isspace())):
        return str_rez
    
    #Деление на ноль
    if (str_oper == "div") and (str_var2 == "0"):
        return str_rez

    f_var1 = float(str_var1)
    f_var2 = float(str_var2)
    
    if (str_oper == "sum"):
        f_rez = f_var1 + f_var2
        
    if (str_oper == "sub"):
        f_rez = f_var1 - f_var2
        
    if (str_oper == "mul"):
        f_rez = f_var1 * f_var2
        
    if (str_oper == "div"):
        f_rez = f_var1 / f_var2
        
    #Преобразуем дробное число в строку
    #Дроби округляем до 8 символов 
    str_rez = convert_float_to_str(f_rez, 8)
        
    return str_rez
    

#Обработка интерфейсных событий. Сюда отправляются нажатия всех клавишь
def interface_fun(str_input):

    global current_state
    global program_display
    global str_variable1
    global str_variable2
    global str_operation
    global flag_point
    
    #Цифры 0-9
    #Заносим цифры в первый или второй операнд
    for n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if (n == str_input):

            #old current_state == "Start"
            if (current_state == program_state[0]):
                #new current_state == "Var1"
                current_state = program_state[1]
                
                #Если была нажата клавиша дробного числа, то изменяем вывод
                if (flag_point == False):
                    program_display = ""
                else:
                    flag_point = False
                    program_display = "0."
                
                display.configure(text=program_display)
                
            #old current_state == "Oper"
            if (current_state == program_state[3]):
                #new current_state == "Var2"
                current_state = program_state[2]
                
                #Если была нажата клавиша дробного числа, то изменяем вывод
                if (flag_point == False):
                    program_display = ""
                else:
                    flag_point = False
                    program_display = "0."
                
                display.configure(text=program_display)
                
            #От переполнения экрана(не больше 14 символов)
            if (len(program_display) <= 13):
            
                #Перестраховочная проверка
                #Если на дисплее был ноль, то стираем его
                #или делаем целой частью дробного числа
                if (program_display == "0"):
                    #Если была нажата клавиша дробного числа, то изменяем вывод
                    if (flag_point == False):
                        program_display = ""
                    else:
                        flag_point = False
                        program_display = "0."
            
                #Если была нажата клавиша дробного числа, то все следующие цифры становятся дробной частью числа
                if (flag_point):
                    flag_point = False
                    
                    #Однако откуда мы можем знать, что до этого число уже не становилось дробным?
                    #Поэтому ставим точку если её уже нет в экранной строке
                    if not ("." in program_display):
                        str_tmp = program_display + "."
                        program_display = str_tmp
            
                str_tmp = program_display + str_input
                program_display = str_tmp
                
                display.configure(text=program_display)
                
    #Кнопки +, -, *, /
    #Сохраняем первый операнд и ждём второго
    #или же вычисляем до этого идущие операнды и работаем с результатом
    if ((str_input == "sum") or
        (str_input == "sub") or
        (str_input == "mul") or
        (str_input == "div")):
        
            #Отменяем флаг дробного числа, который должен был бы превратить число в дробное при вводе цифры
            flag_point = False
        
            #Если имели до этого ввод первого операнда, то скидываем его в переменную
            #Если до этого получили результат с помощью энтера, то также рассматриваем его как первый операнд
            #(current_state == "Var1") or (current_state == "Rez")
            if ((current_state == program_state[1]) or (current_state == program_state[4])):
                str_variable1 = program_display
                
            #Если имеем ввод второго операнда, пробуем вычислить вначале имеющиеся операнды
            if (current_state == program_state[2]):
                
                #Скидываем имеющееся на экране во вторую переменную
                str_variable2 = program_display
                
                #Функция сама обработает возможную пустоту значений в операндах
                str_rez = calc_fun(str_variable1, str_variable2, str_operation)
                
                #showinfo(title="Debug", message=str_rez)
                
                if (str_rez == "error"):
                    reset_fun()
                else:
                    str_variable1 = str_rez
                    str_variable2 = ""
                    program_display = str_rez
                    display.configure(text=program_display)
            
            #В любом случае запоминаем новую поступившую операцию
            #Если уже была выбрана операция current_state == "Oper", она просто заменится
            str_operation = str_input
            
            #Выставляем текущее как "Oper" 
            current_state = program_state[3]
            
    #Кнопка Enter
    #Выводим результат текущей операции
    if (str_input == "ent"):
        
        #Клавиша Enter доступна лишь в следующих случаях:
        #1) Уже был получен результат(st4) и следовательно можно устроить повтор
        #2) Вводится первый аргумент(st1) и уже есть операция и второй аргумент
        #3) Введена операция(st3) и у нас есть оба операнда
        #4) Вводится второй аргумент(st2) и уже имеем операцию и первый аргумент
        if ((current_state == program_state[4]) or
            ((current_state == program_state[1]) and (str_operation != "") and (str_variable2 != "")) or
            ((current_state == program_state[3]) and (str_variable1 != "") and (str_variable2 != "")) or
            ((current_state == program_state[2]) and (str_operation != "") and (str_variable1 != ""))):
            
            #Отменяем флаг дробного числа, который должен был бы превратить число в дробное при вводе цифры
            flag_point = False
        
            #Если был ввод второго операнда, то скидываем имеющееся на экране во вторую переменную
            if (current_state != program_state[4]):
                str_variable2 = program_display
            else:
                #И напротив, если имеем лишь нажатие клавиши энтер, то обновим первую переменную
                str_variable1 = program_display
        
            #Функция сама обработает возможную пустоту значений в операндах
            str_rez = calc_fun(str_variable1, str_variable2, str_operation)
            
            #showinfo(title="Debug", message=str_rez)
            
            if (str_rez == "error"):
                reset_fun()
            else:
                str_variable1 = str_rez
                program_display = str_rez
                display.configure(text=program_display)
                
                #current_state = "Rez"
                current_state = program_state[4]
        
    #Кнопка Delete
    #Удаляем по одному символу на экране справа
    if (str_input == "del"):
    
        #Отменяем флаг дробного числа, который должен был бы превратить число в дробное при вводе цифры
        #Также если обнаруживаем, что флаг был установлен, то не удаляем ничего другого
        if (flag_point):
        
            flag_point = False
            
        else:
        
            #Дополнительная проверка на присутствие знака "e"
            #В этом случае полностью очищаем экран
            if ("e" in program_display):
                program_display = "0"
                display.configure(text=program_display)
        
            #Дополнительная проверка, от пустоты на дисплее
            if (program_display == ""):
                program_display = "0"
                display.configure(text=program_display)
            
            #Убираем цифры только если что-то есть на дисплее
            #если имеем состояние введёной операции или результат, то обновляем также первую переменную
            #и работаем именно с дисплеем не обращая внимание на всё остальное
            if (program_display != ""):
                
                #showinfo(title="Debug", message="Delete")
                
                n_length = len(program_display)
                
                str_tmp = "0"
                
                #Ставим ноль если:
                #1)остался один символ, который соответсвенно удалится
                #2)либо мы имеем дело с минусом
                #В остальных же случаях убавляем по одному символу
                if ((n_length <= 1) or
                    ((n_length == 2) and (program_display[0] == "-"))):
                    str_tmp = "0"
                else:
                    str_tmp = program_display[:(n_length - 1)]
                    
                program_display = str_tmp
                display.configure(text=program_display)
                
                #Если был введён первый аргумент и мы находимся на стадии операции, то изменим также значение первой переменной
                #Точно также поступаем если была нажата клавиша энтер и на экране мы видим результат
                #(current_state == "Oper") or (current_state == "Rez")
                if ((current_state == program_state[3]) or (current_state == program_state[4])):
                    str_variable1 = program_display
                    
        
    #Кнопка Reset
    #Сброс состояния в ноль
    if (str_input == "rst"):
        reset_fun()
        
    #Кнопка Copy
    #Копируем содержимое экрана в буфер обмена
    if (str_input == "cpy"):
        pyperclip.copy(program_display)
    
    #Кнопка Point
    #Ставим флаг о том, что следующая введёная цифра пойдёт как дробная часть числа 
    if (str_input == "pnt"):
        flag_point = True
        
    #Кнопка Plus_or_Minus
    #Инвертируем число на экране
    if (str_input == "p_or_m"):
        f_num = float(program_display)
        
        f_num = f_num * (-1)
        #Преобразуем дробное число в строку
        #Дроби округляем до 8 символов 
        program_display = convert_float_to_str(f_num, 8)
        display.configure(text=program_display)
        
        #Если был введён первый аргумент и мы находимся на стадии операции, то изменим также значение первой переменной
        #Точно также поступаем если была нажата клавиша энтер и на экране мы видим результат
        #(current_state == "Oper") or (current_state == "Rez")
        if ((current_state == program_state[3]) or (current_state == program_state[4])):
            str_variable1 = program_display

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("MiniCalc")
root.geometry("282x400+400+200")

root.resizable(False, False)

#Текущая версия программы

version = customtkinter.CTkLabel(
    master = root,
    text = "version: " + str_version,
    text_font = ("Verdana", 6),
    fg_color = "#000000",
    bg_color = "#000000",
    text_color = "#FFFFFF")

version.place(x=0, y=0, width=90, height=20)

#Дисплей

display = customtkinter.CTkLabel(
    master = root,
    text = "0",
    text_font = ("Verdana", 14),
    anchor = customtkinter.E,
    fg_color = "#D2D2D2",
    text_color = "#B71C1C",
    corner_radius = 3)

display.place(x=20, y=25, width=302, height=40)

#Кнопки системных операций

wx_rst = customtkinter.CTkButton(
    master=root,
    text="Reset",
    text_font = ("Verdana", 11),
    corner_radius = 3,
    fg_color="maroon",
    hover_color="red",
    command = lambda: interface_fun("rst"))
    
wx_rst.place(x=20, y=75, width=90, height=40)

wx_del = customtkinter.CTkButton(
    master=root,
    text = "Delete",
    text_font = ("Verdana", 11),
    corner_radius = 3,
    fg_color="gray",
    hover_color="darkgray",
    command = lambda: interface_fun("del"))
    
wx_del.place(x=105, y=75, width=90, height=40)

wx_cpy = customtkinter.CTkButton(
    master=root,
    text = "Copy",
    text_font = ("Verdana", 11),
    corner_radius = 3,
    fg_color="gray",
    hover_color="darkgray",
    command = lambda: interface_fun("cpy"))

wx_cpy.place(x=190, y=75, width=90, height=40)

#Кнопки вычислений

wx_sum = customtkinter.CTkButton(master=root, text = "+", text_font = ("Verdana", 11), corner_radius = 3, command = lambda: interface_fun("sum"))
wx_sum.place(x=20, y=125, width=90, height=40)

wx_mul = customtkinter.CTkButton(master=root, text = "*", text_font = ("Verdana", 11), corner_radius = 3, command = lambda: interface_fun("mul"))
wx_mul.place(x=105, y=125, width=90, height=40)

wx_p_or_m = customtkinter.CTkButton(master=root, text = "+/-", text_font = ("Verdana", 11), corner_radius = 3, command = lambda: interface_fun("p_or_m"))
wx_p_or_m.place(x=190, y=125, width=90, height=40)

wx_sub = customtkinter.CTkButton(master=root, text = "-", text_font = ("Verdana", 11), corner_radius = 3, command = lambda: interface_fun("sub"))
wx_sub.place(x=20, y=165, width=90, height=40)

wx_div = customtkinter.CTkButton(master=root, text = "/", text_font = ("Verdana", 11), corner_radius = 3, command = lambda: interface_fun("div"))
wx_div.place(x=105, y=165, width=90, height=40)

wx_pnt = customtkinter.CTkButton(master=root, text = ".", text_font = ("Verdana", 11), corner_radius = 3, command = lambda: interface_fun("pnt"))
wx_pnt.place(x=190, y=165, width=90, height=40)

#Цифровая клавиатура

wx1 = customtkinter.CTkButton(master=root, text = "1", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("1"))
wx1.place(x=20, y=210, width=90, height=40)

wx2 = customtkinter.CTkButton(master=root, text = "2", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("2"))
wx2.place(x=105, y=210, width=90, height=40)

wx3 = customtkinter.CTkButton(master=root, text = "3", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("3"))
wx3.place(x=190, y=210, width=90, height=40)

wx4 = customtkinter.CTkButton(master=root, text = "4", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("4"))
wx4.place(x=20, y=250, width=90, height=40)

wx5 = customtkinter.CTkButton(master=root, text = "5", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("5"))
wx5.place(x=105, y=250, width=90, height=40)

wx6 = customtkinter.CTkButton(master=root, text = "6", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("6"))
wx6.place(x=190, y=250, width=90, height=40)

wx7 = customtkinter.CTkButton(master=root, text = "7", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("7"))
wx7.place(x=20, y=290, width=90, height=40)

wx8 = customtkinter.CTkButton(master=root, text = "8", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("8"))
wx8.place(x=105, y=290, width=90, height=40)

wx9 = customtkinter.CTkButton(master=root, text = "9", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("9"))
wx9.place(x=190, y=290, width=90, height=40)

wx0 = customtkinter.CTkButton(master=root, text = "0", text_font = ("Verdana", 13), corner_radius = 3, command = lambda: interface_fun("0"))
wx0.place(x=20, y=335, width=90, height=40)

#Кнопка энтер

wx_ent = customtkinter.CTkButton(
    master=root,
    text = "Enter",
    text_font = ("Verdana", 11),
    corner_radius = 3,
    fg_color="green",
    hover_color="darkgreen",
    command = lambda: interface_fun("ent"))
    
wx_ent.place(x=105, y=335, width=198, height=40)

#Статусная строка внизу окна

status = customtkinter.CTkLabel(
    master = root,
    text = "",
    anchor = customtkinter.W,
    text_font = ("Verdana", 8),
    fg_color = "#000000",
    bg_color = "#000000",
    width=350,
    height=25,
    text_color = "#FFFFFF")

status.place(x=0, y=380)

#События клавиатуры
root.bind("0", (lambda event: interface_fun("0")))
root.bind("1", (lambda event: interface_fun("1")))
root.bind("2", (lambda event: interface_fun("2")))
root.bind("3", (lambda event: interface_fun("3")))
root.bind("4", (lambda event: interface_fun("4")))
root.bind("5", (lambda event: interface_fun("5")))
root.bind("6", (lambda event: interface_fun("6")))
root.bind("7", (lambda event: interface_fun("7")))
root.bind("8", (lambda event: interface_fun("8")))
root.bind("9", (lambda event: interface_fun("9")))
root.bind("+", (lambda event: interface_fun("sum")))
root.bind("-", (lambda event: interface_fun("sub")))
root.bind("*", (lambda event: interface_fun("mul")))
root.bind("/", (lambda event: interface_fun("div")))
root.bind("<Escape>", (lambda event: interface_fun("rst")))
root.bind("<Delete>", (lambda event: interface_fun("del")))
root.bind("<BackSpace>", (lambda event: interface_fun("del")))
root.bind("<Return>", (lambda event: interface_fun("ent")))
root.bind("c", (lambda event: interface_fun("cpy")))
root.bind("$", (lambda event: interface_fun("p_or_m")))
root.bind(".", (lambda event: interface_fun("pnt")))
root.bind(",", (lambda event: interface_fun("pnt")))

#Мышь вошла в зону действия элемента, показываем подсказку
wx0.bind("<Enter>", (lambda event: statusbar_fun("0", True)))
wx1.bind("<Enter>", (lambda event: statusbar_fun("1", True)))
wx2.bind("<Enter>", (lambda event: statusbar_fun("2", True)))
wx3.bind("<Enter>", (lambda event: statusbar_fun("3", True)))
wx4.bind("<Enter>", (lambda event: statusbar_fun("4", True)))
wx5.bind("<Enter>", (lambda event: statusbar_fun("5", True)))
wx6.bind("<Enter>", (lambda event: statusbar_fun("6", True)))
wx7.bind("<Enter>", (lambda event: statusbar_fun("7", True)))
wx8.bind("<Enter>", (lambda event: statusbar_fun("8", True)))
wx9.bind("<Enter>", (lambda event: statusbar_fun("9", True)))
wx_sum.bind("<Enter>", (lambda event: statusbar_fun("sum", True)))
wx_sub.bind("<Enter>", (lambda event: statusbar_fun("sub", True)))
wx_mul.bind("<Enter>", (lambda event: statusbar_fun("mul", True)))
wx_div.bind("<Enter>", (lambda event: statusbar_fun("div", True)))
wx_rst.bind("<Enter>", (lambda event: statusbar_fun("rst", True)))
wx_del.bind("<Enter>", (lambda event: statusbar_fun("del", True)))
wx_ent.bind("<Enter>", (lambda event: statusbar_fun("ent", True)))
wx_cpy.bind("<Enter>", (lambda event: statusbar_fun("cpy", True)))
wx_p_or_m.bind("<Enter>", (lambda event: statusbar_fun("p_or_m", True)))
wx_pnt.bind("<Enter>", (lambda event: statusbar_fun("pnt", True)))
version.bind("<Enter>", (lambda event: statusbar_fun("ver", True)))
status.bind("<Enter>", (lambda event: statusbar_fun("stt", True)))

#Мышь ушла из зоны действия элемента, убираем подсказку
wx0.bind("<Leave>", (lambda event: statusbar_fun("0", False)))
wx1.bind("<Leave>", (lambda event: statusbar_fun("1", False)))
wx2.bind("<Leave>", (lambda event: statusbar_fun("2", False)))
wx3.bind("<Leave>", (lambda event: statusbar_fun("3", False)))
wx4.bind("<Leave>", (lambda event: statusbar_fun("4", False)))
wx5.bind("<Leave>", (lambda event: statusbar_fun("5", False)))
wx6.bind("<Leave>", (lambda event: statusbar_fun("6", False)))
wx7.bind("<Leave>", (lambda event: statusbar_fun("7", False)))
wx8.bind("<Leave>", (lambda event: statusbar_fun("8", False)))
wx9.bind("<Leave>", (lambda event: statusbar_fun("9", False)))
wx_sum.bind("<Leave>", (lambda event: statusbar_fun("sum", False)))
wx_sub.bind("<Leave>", (lambda event: statusbar_fun("sub", False)))
wx_mul.bind("<Leave>", (lambda event: statusbar_fun("mul", False)))
wx_div.bind("<Leave>", (lambda event: statusbar_fun("div", False)))
wx_rst.bind("<Leave>", (lambda event: statusbar_fun("rst", False)))
wx_del.bind("<Leave>", (lambda event: statusbar_fun("del", False)))
wx_ent.bind("<Leave>", (lambda event: statusbar_fun("ent", False)))
wx_cpy.bind("<Leave>", (lambda event: statusbar_fun("cpy", False)))
wx_p_or_m.bind("<Leave>", (lambda event: statusbar_fun("p_or_m", False)))
wx_pnt.bind("<Leave>", (lambda event: statusbar_fun("pnt", False)))
version.bind("<Leave>", (lambda event: statusbar_fun("ver", False)))
status.bind("<Leave>", (lambda event: statusbar_fun("stt", False)))

#Клавиша "s" закрывает/открывает статусбар
root.bind("s", hide_status_fun)

#Клавиши "i" открывают информацию о программе
root.bind("i", information_fun)

#Клавиша "q" для выхода из программы
root.bind("q", (lambda event: root.destroy()))


root.mainloop()