import ttkbootstrap as ttk
from ttkbootstrap.constants import *


tempo_restante = 25 * 60
rodando = False


def iniciar_pomodoro():
    global rodando

    if not rodando:
        rodando = True
        atualizar_relogio()


def pausar_pomodoro():
    global rodando

    rodando = False


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


def reset():
    global tempo_restante, rodando

    tempo_restante = 25 * 60
    rodando = False

    relogio_var.set(formatar_tempo(tempo_restante))


# Janela principal
janela = ttk.Window()
janela.title("Pomodoro")
janela.geometry("400x300")


# Variável que controla o texto do relógio
relogio_var = ttk.StringVar(
    value=formatar_tempo(tempo_restante)
)


# Relógio
relogio_label = ttk.Label(
    janela,
    textvariable=relogio_var,
    font=("Arial", 48)
)

relogio_label.pack(pady=30)


# Frame para organizar os botões
frame_botoes = ttk.Frame(janela)
frame_botoes.pack(pady=10)


# Botão iniciar
botao_iniciar = ttk.Button(
    frame_botoes,
    text="Iniciar",
    bootstyle=SUCCESS,
    command=iniciar_pomodoro
)

botao_iniciar.pack(side=LEFT, padx=5)


# Botão pausar
botao_pausar = ttk.Button(
    frame_botoes,
    text="Pausar",
    bootstyle=WARNING,
    command=pausar_pomodoro
)

botao_pausar.pack(side=LEFT, padx=5)


# Botão resetar
botao_reset = ttk.Button(
    frame_botoes,
    text="Resetar",
    bootstyle=DANGER,
    command=reset
)

botao_reset.pack(side=LEFT, padx=5)


# Mantém a janela aberta
janela.mainloop()