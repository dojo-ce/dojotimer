#-*- coding: utf-8 -*-
from Tkinter import *
import time

class Clock(object):

    def __init__(self, master, default_time=1):


        # Crio o frame principal.
        self.frame = Frame(master)
        self.frame.pack()
        

        # Pego a janela TopLevel
        self.top = self.frame.winfo_toplevel()

        # Modifico um pouco a janela
        self.top.title("Dojo Rio")
        self.top.attributes('-topmost', 1)
        self.top.resizable(0, 0)

        # Os outros widgets ficam num método separado
        self.create_widgets()

        # Defino alguns valores padrão.
        self.running = False
        self.default_time = default_time # Tempo padrão (em minutos)
        self.seconds = 60 * self.default_time
        self.labelstr.set('%02d:%02d' % ((self.seconds /60), (self.seconds % 60)))

    def create_widgets(self):

        # Crio o label. self.labelstr é o que vai ser usado como texto. Quando for atualizada com o
        # método .set('str') o label vai ser atualizado.
        self.labelstr = StringVar()
        self.label = Label(self.frame, textvariable=self.labelstr, fg='#198931', font=('Helvetica', '48'))
        self.label.pack()

        # Crio alguns botões
        self.start = Button(self.frame, text='Começar', command=self.start)
        self.start.pack(side=LEFT)

        self.stop = Button(self.frame, text='Parar', command=self.stop)
        self.stop.pack(side=LEFT)

        self.reset = Button(self.frame, text='Zerar', command=self.reset)
        self.reset.pack(side=LEFT)

        self.quit = Button(self.frame, text='Sair', command=self.frame.quit)
        self.quit.pack(side=LEFT)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def update(self):
        if self.running:

            if 0 < self.seconds <= 30:
                self.label['fg']='#efbf16'
            elif self.seconds <= 0:
                self.label['fg']='#d70505'
                self.running = False
            new_str = '%02d:%02d' % ((self.seconds / 60), (self.seconds % 60))
            self.labelstr.set(new_str)
            self.label.after(1000, self.update)
            self.seconds -= 1
    
    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 60 * self.default_time
        self.label['fg']='#198931'
        new_str = '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        self.labelstr.set(new_str)


if __name__ == '__main__':
    root = Tk()
    clock = Clock(root, 1)

    root.mainloop()
