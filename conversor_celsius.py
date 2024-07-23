from tkinter import *
def fah():                                                                          #função para converter celsius a fahrenheit
    print('Fahrenheit')
    if (str(ent_n1.get()).isnumeric()):
        n1 = int(ent_n1.get())
        lb['text'] = n1 * 9/5 + 32
    else:
        lb['text'] = 'Valores inválidos'

def cel():                                                                          #função para converter fahrenheit a celsius
    print('Celsius')
    if (str(ent_n1.get()).isnumeric()):
        n1 = int(ent_n1.get())
        lb['text'] = (n1 - 32) * 5/9
    else:
        lb['text'] = 'Valores inválidos'

janela = Tk()
janela.title('Conversor de temperatura')
text_orient = Label(janela, text = 'Converta as temperaturas')
text_orient.grid(column = 0, row = 0)
ent_n1 = Entry(janela, width = 5)
ent_n1.grid(column = 0, row = 1)
bt_fah = Button(janela, text = 'Celsius para Fahrenheit', command = fah)
bt_fah.grid(column = 0, row = 4)
bt_cel = Button(janela, text = 'Fahrenheit para Celsius', command = cel)
bt_cel.grid(column = 0, row = 5)
lb = Label(janela, text = '0')
lb.grid(column = 0, row = 3)
janela.mainloop()