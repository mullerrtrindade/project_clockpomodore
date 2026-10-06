# 🍅 Pomodoro Timer

Um aplicativo desktop de **Pomodoro** desenvolvido em Python para auxiliar na organização do tempo, produtividade e alternância entre períodos de foco e descanso.

O projeto foi desenvolvido como parte dos meus estudos em **Python e desenvolvimento de interfaces gráficas**, utilizando `ttkbootstrap` para a construção da interface.

---

## 📸 Sobre o projeto

O aplicativo utiliza a técnica Pomodoro, dividindo o trabalho em períodos de foco e descanso.

O funcionamento padrão é:

- 🎯 **25 minutos de foco**
- ☕ **5 minutos de descanso**
- 🧠 **15 minutos de descanso longo**
- 🔄 Descanso longo após **4 ciclos de foco**

---

## ✨ Funcionalidades

- ⏱️ Cronômetro regressivo
- ▶️ Iniciar Pomodoro
- ⏸️ Pausar cronômetro
- 🔄 Resetar sessão
- 🎯 Modo de foco
- ☕ Descanso curto
- 🧠 Descanso longo
- 🔢 Contador de ciclos concluídos
- 📊 Barra de progresso
- 🔔 Avisos ao término dos períodos
- 🎨 Mudança visual de acordo com o modo atual
- 🔒 Controle dos botões de acordo com o estado do cronômetro

---

## 🛠️ Tecnologias utilizadas

- Python
- Tkinter
- ttkbootstrap

---

## 📂 Estrutura

```text
project_clockpomodore/
│
├── main.py
├── README.md
└── .gitignore
```

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/mullerrtrindade/project_clockpomodore.git
```

### 2. Entre na pasta

```bash
cd project_clockpomodore
```

### 3. Instale o ttkbootstrap

```bash
pip install ttkbootstrap
```

### 4. Execute o programa

```bash
python main.py
```

---

## 🧠 Como funciona

O aplicativo possui três estados principais:

### Foco

O usuário possui **25 minutos** destinados à realização de uma atividade.

Ao finalizar o período, um ciclo é contabilizado.

### Descanso

Após um período de foco, o programa libera um descanso de **5 minutos**.

### Descanso longo

Após completar **4 ciclos de foco**, o usuário recebe um período de descanso de **15 minutos**.

Depois disso, o processo pode continuar normalmente.

---

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos como:

- Funções
- Variáveis globais
- Condicionais
- Operadores matemáticos
- Manipulação de estado
- Interfaces gráficas
- Eventos
- Callbacks
- `StringVar`
- `after()`
- `after_cancel()`
- Frames
- Labels
- Buttons
- Progressbar
- Messagebox
- Organização de código por responsabilidades

---

## 🎯 Objetivo

O principal objetivo deste projeto foi colocar em prática conhecimentos de Python através da construção de uma aplicação desktop funcional.

O projeto também faz parte da minha evolução no desenvolvimento de aplicações com interface gráfica e organização de código.

---

## 👨‍💻 Autor

**Müller Trindade**

GitHub: [@mullerrtrindade](https://github.com/mullerrtrindade)

---

## 📄 Licença

Projeto desenvolvido para fins de estudo e aprendizado.