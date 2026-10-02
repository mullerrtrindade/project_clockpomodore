import ttkbootstrap as ttk
from ttkbootstrap.constants import *

tempo_restante = 25 * 60
rodando = False

def iniciar_pomodoro():
    global rodando

    if not rodando:
        rodando = True
        atualizar_relogio()


def formatar_tempo(tempo):
    minutos = tempo // 60
    segundos = tempo % 60

    return f"{minutos:02}:{segundos:02}"


def atualizar_relogio():
    global tempo_restante

    if rodando and tempo_restante > 0:
        tempo_restante -= 1

        relogio_var.set(formatar_tempo(tempo_restante))

        janela.after(1000, atualizar_relogio)


janela = ttk.Window()
janela.title("Pomodoro")
janela.geometry("400x300")


relogio_var = ttk.StringVar(
    value=formatar_tempo(tempo_restante)
)


relogio_label = ttk.Label(
    janela,
    textvariable=relogio_var,
    font=("Arial", 48)
)

relogio_label.pack(pady=30)


janela.after(1000, atualizar_relogio)

janela.mainloop()

botao_iniciar = ttk.Button(
    janela,
    text="Iniciar",
    bootstyle=SUCCESS,
    command=iniciar_pomodoro
)
botao_iniciar.pack(pady=10)

