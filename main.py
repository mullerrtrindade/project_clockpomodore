import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


# =========================================================
# CONFIGURAÇÕES
# =========================================================

TEMPO_FOCO = 25 * 60
TEMPO_DESCANSO = 5 * 60
TEMPO_DESCANSO_LONGO = 15 * 60

CICLOS_ATE_DESCANSO_LONGO = 4


# =========================================================
# ESTADO DO PROGRAMA
# =========================================================

tempo_restante = TEMPO_FOCO

rodando = False
after_id = None

modo_atual = "Foco"
ciclos_concluidos = 0


# =========================================================
# FUNÇÕES DO CRONÔMETRO
# =========================================================

def formatar_tempo(tempo):
    minutos = tempo // 60
    segundos = tempo % 60

    return f"{minutos:02}:{segundos:02}"


def iniciar_pomodoro():
    global rodando, after_id

    if not rodando:
        rodando = True

        atualizar_botoes()

        after_id = janela.after(
            1000,
            atualizar_relogio
        )


def pausar_pomodoro():
    global rodando, after_id

    rodando = False

    if after_id is not None:
        janela.after_cancel(after_id)
        after_id = None

    atualizar_botoes()


def atualizar_relogio():
    global tempo_restante
    global rodando
    global after_id

    if rodando and tempo_restante > 0:

        tempo_restante -= 1

        relogio_var.set(
            formatar_tempo(tempo_restante)
        )

        atualizar_progresso()

        after_id = janela.after(
            1000,
            atualizar_relogio
        )

    elif tempo_restante == 0:

        rodando = False
        after_id = None

        atualizar_botoes()

        finalizar_periodo()


# =========================================================
# FUNÇÕES DOS CICLOS
# =========================================================

def finalizar_periodo():
    global modo_atual
    global ciclos_concluidos

    if modo_atual == "Foco":

        ciclos_concluidos += 1

        if ciclos_concluidos % CICLOS_ATE_DESCANSO_LONGO == 0:

            messagebox.showinfo(
                "Pomodoro",
                "Foco concluído!\nHora de fazer um descanso longo."
            )

            iniciar_descanso_longo()

        else:

            messagebox.showinfo(
                "Pomodoro",
                "Foco concluído!\nHora de descansar."
            )

            iniciar_descanso()

    else:

        messagebox.showinfo(
            "Pomodoro",
            "Descanso concluído!\nHora de voltar ao foco."
        )

        iniciar_foco()


def iniciar_foco():
    global tempo_restante
    global modo_atual

    modo_atual = "Foco"
    tempo_restante = TEMPO_FOCO

    atualizar_interface()


def iniciar_descanso():
    global tempo_restante
    global modo_atual

    modo_atual = "Descanso"
    tempo_restante = TEMPO_DESCANSO

    atualizar_interface()


def iniciar_descanso_longo():
    global tempo_restante
    global modo_atual

    modo_atual = "Descanso longo"
    tempo_restante = TEMPO_DESCANSO_LONGO

    atualizar_interface()


# =========================================================
# FUNÇÕES DA INTERFACE
# =========================================================

def atualizar_interface():

    relogio_var.set(
        formatar_tempo(tempo_restante)
    )

    modo_var.set(
        modo_atual
    )

    ciclos_var.set(
        f"Ciclos concluídos: {ciclos_concluidos}"
    )

    barra_progresso["value"] = 0

    atualizar_estilo_modo()


def atualizar_estilo_modo():

    if modo_atual == "Foco":
        modo_label.configure(
            bootstyle=SUCCESS
        )

        barra_progresso.configure(
            bootstyle=SUCCESS
        )

    elif modo_atual == "Descanso":
        modo_label.configure(
            bootstyle=INFO
        )

        barra_progresso.configure(
            bootstyle=INFO
        )

    else:
        modo_label.configure(
            bootstyle=WARNING
        )

        barra_progresso.configure(
            bootstyle=WARNING
        )


def atualizar_botoes():

    if rodando:

        botao_iniciar.configure(
            state="disabled"
        )

        botao_pausar.configure(
            state="normal"
        )

    else:

        botao_iniciar.configure(
            state="normal"
        )

        botao_pausar.configure(
            state="disabled"
        )


def atualizar_progresso():

    if modo_atual == "Foco":

        tempo_total = TEMPO_FOCO

    elif modo_atual == "Descanso":

        tempo_total = TEMPO_DESCANSO

    else:

        tempo_total = TEMPO_DESCANSO_LONGO

    progresso = (
        (tempo_total - tempo_restante)
        / tempo_total
    ) * 100

    barra_progresso["value"] = progresso


def reset():
    global tempo_restante
    global rodando
    global after_id
    global modo_atual
    global ciclos_concluidos

    rodando = False

    if after_id is not None:
        janela.after_cancel(after_id)
        after_id = None

    tempo_restante = TEMPO_FOCO
    modo_atual = "Foco"
    ciclos_concluidos = 0

    atualizar_interface()
    atualizar_botoes()


def fechar_programa():
    global after_id

    if after_id is not None:
        janela.after_cancel(after_id)

    janela.destroy()


# =========================================================
# JANELA PRINCIPAL
# =========================================================

janela = ttk.Window(
    themename="darkly"
)

janela.title("Pomodoro")
janela.geometry("450x400")

janela.resizable(
    False,
    False
)

janela.protocol(
    "WM_DELETE_WINDOW",
    fechar_programa
)


# =========================================================
# VARIÁVEIS DA INTERFACE
# =========================================================

modo_var = ttk.StringVar(
    value=modo_atual
)

relogio_var = ttk.StringVar(
    value=formatar_tempo(tempo_restante)
)

ciclos_var = ttk.StringVar(
    value=f"Ciclos concluídos: {ciclos_concluidos}"
)


# =========================================================
# TÍTULO
# =========================================================

titulo_label = ttk.Label(
    janela,
    text="POMODORO",
    font=("Arial", 12, "bold")
)

titulo_label.pack(
    pady=(20, 5)
)


# =========================================================
# MODO ATUAL
# =========================================================

modo_label = ttk.Label(
    janela,
    textvariable=modo_var,
    font=("Arial", 18, "bold"),
    bootstyle=SUCCESS
)

modo_label.pack(
    pady=5
)


# =========================================================
# RELÓGIO
# =========================================================

relogio_label = ttk.Label(
    janela,
    textvariable=relogio_var,
    font=("Arial", 48, "bold")
)

relogio_label.pack(
    pady=15
)


# =========================================================
# BARRA DE PROGRESSO
# =========================================================

barra_progresso = ttk.Progressbar(
    janela,
    length=320,
    mode="determinate",
    maximum=100,
    value=0,
    bootstyle=SUCCESS
)

barra_progresso.pack(
    pady=10
)


# =========================================================
# CONTADOR DE CICLOS
# =========================================================

ciclos_label = ttk.Label(
    janela,
    textvariable=ciclos_var,
    font=("Arial", 11)
)

ciclos_label.pack(
    pady=10
)


# =========================================================
# BOTÕES
# =========================================================

frame_botoes = ttk.Frame(
    janela
)

frame_botoes.pack(
    pady=20
)


botao_iniciar = ttk.Button(
    frame_botoes,
    text="Iniciar",
    bootstyle=SUCCESS,
    command=iniciar_pomodoro,
    width=10
)

botao_iniciar.pack(
    side=LEFT,
    padx=5
)


botao_pausar = ttk.Button(
    frame_botoes,
    text="Pausar",
    bootstyle=WARNING,
    command=pausar_pomodoro,
    state="disabled",
    width=10
)

botao_pausar.pack(
    side=LEFT,
    padx=5
)


botao_reset = ttk.Button(
    frame_botoes,
    text="Resetar",
    bootstyle=DANGER,
    command=reset,
    width=10
)

botao_reset.pack(
    side=LEFT,
    padx=5
)


# =========================================================
# LOOP PRINCIPAL
# =========================================================

janela.mainloop()