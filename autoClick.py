from tkinter import *
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


window = Tk()

window.title("AutoClicker - Daniel Corona")
window.geometry("400x400")


texto_orientacao = Label(window, text="Clique no botão para iniciar o AutoClicker")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

# botao = Button(window, text="Iniciar", command=)
# botao.grid(column=0,row=1)

texto_status = Label(window, text="Ativo")
texto_status.grid(column=0,row=2,padx=10, pady=10)
window.mainloop()





delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()



