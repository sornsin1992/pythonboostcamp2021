from tkinter import * #ดึงความสามรถหลักมาทั้งหมด
from tkinter import ttk # ttk is theme of tk
from googletrans import Translator
#-----------Google translate function--------------
translator = Translator()

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #ขยายขนาดหน้าจอ
GUI.title('วุ้นแปลภาษา')
#--------------------------Config-----------
FONT = ('Andsana New',15)
#------------Label---------------------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()
#---------------------Entry(ช่องกรอก)--------
v_vocab = StringVar() # class or  ช่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)
#ipadx = กรอบภายใน pad = ระยะห่างระหว่างกรอบ
#---------------------Button--------
def Translate():
                vocab = v_vocab.get()    #.get คือให้แสดงผลออกมา ไม่สามารถดึงมาใช้โดยตรงได้
                meaning = translator.translate(vocab,dest='th')
                print( vocab + ' : '  + meaning.text)
                print(meaning.pronunciation)
                v_result.set(vocab + ' : ' + meaning.text) #setค่า
B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่ม
B1.pack(ipadx=20,ipady=10)

#------------Label2---------------------
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()
#------------result----------------------
v_result = StringVar() #กล่องเก็บคำแปล
R1 = ttk.Label(GUI,textvariable=v_result, font=FONT,foreground='green')
R1.pack()

#ipadx = ระยะภายใร, padx = ระยะภายนอก

GUI.mainloop()

#สั่งให้โปรแกรม Run ตลอดเวลาจนกว่าจtปิด
#ต้องอยู่บรรทัดสุดท้ายเท่านั้น
