#Импортируем модуль os, для работы с директориями и путями  
import os
from os import path

dir = os.path.abspath(os.curdir)

SPLITTER = [[0, 19],[21, 40], [42, 48]]
LOG_PATH = path.join(dir, "dism.log")
HTML_PATH = path.join(dir, "index.html")
AFTER_HTML_PATH = path.join(dir, "after_index.html")
BEFORE_HTML_PATH = path.join(dir, "before_index.html")

#Превращаем необработанную строку в сроку Html,
def line2htmlRow(line):
    #Если строка меньше 57, то скорее всего там только сообщение
    if len(line) < 57 or line[0]=="[":
        pass
        return "<tr><td></td><td></td><td></td><td>"+line+"</td></tr>\n"
    #Иначе делим на столбцы, используя информацию из сплиттера
    else:    
        S = SPLITTER
        outline = "<tr>"
        for i in range(0,len(S)):
            outline += '<td class="c'+str(i)+'">' + line[S[i][0]:S[i][1]].strip() + "</td>"
        #Последний столбец не имеет фиксированной длины и идет до конца
        outline += "<td>" + line[S[len(S)-1][1]:].strip() + "</td></tr>\n"
        return outline
    return ""



#Делим лог на страницы
def createOrUpdateHtml():
    fill_table()
    content = ""
    with open(AFTER_HTML_PATH, "r", encoding="utf-8") as after_file:
        with open(BEFORE_HTML_PATH, "r", encoding="utf-8") as before_file:
            with open(HTML_PATH, "r", encoding="utf-8") as middle_file:
                content = after_file.read() + middle_file.read() + before_file.read()
    
    with open(HTML_PATH, "w", encoding="utf-8") as middle_file:
        middle_file.write(content)

    return HTML_PATH


def fill_table():
    with open(LOG_PATH) as file_handler:
        line = "test"
        startPoint = findStartPoint(file_handler)
        file_handler.seek(startPoint)
        with open(HTML_PATH, "w", encoding="utf-8") as new_file:
            while line != "": 
                line = getLine(file_handler)
                new_line = line2htmlRow(line)
                new_file.write(new_line)




#Получить строку из файла
def getLine(file_handler):
    ch = file_handler.read(1)
    line = ""
    while ch != "" and ch != "\n":
        line += ch
        ch = file_handler.read(1)
    return line


#Получить начало лога, некоторые логи читают с начала мусорные байты
def findStartPoint(file_handler):
    ch = file_handler.read(1)
    startByte = 0
    while not ch.isdigit():
        ch = file_handler.read(1)
        startByte += 1
    return startByte

createOrUpdateHtml()