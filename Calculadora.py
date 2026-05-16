import tkinter as tk

# Função da calculadora
def calcular():
    try:
        numero1 = float(entry_num1.get())
        numero2 = float(entry_num2.get())
        operacao = entry_operacao.get()

        if operacao == "+":
            resultado = numero1 + numero2

        elif operacao == "-":
            resultado = numero1 - numero2

        elif operacao == "*":
            resultado = numero1 * numero2

        elif operacao == "/":
            if numero2 == 0:
                resultado_label.config(text="Não é possível dividir por zero!")
                return
            resultado = numero1 / numero2

        else:
            resultado_label.config(text="Operação inválida!")
            return

        resultado_label.config(text=f"Resultado: {resultado.:2f}")

    except ValueError:
        resultado_label.config(text="Digite números válidos!")

# Criando janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x250")

# Título
titulo = tk.Label(janela, text="Calculadora Python", font=("Arial", 16))
titulo.pack(pady=10)

# Primeiro número
label_num1 = tk.Label(janela, text="Primeiro número:")
label_num1.pack()

entry_num1 = tk.Entry(janela)
entry_num1.pack()

# Segundo número
label_num2 = tk.Label(janela, text="Segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(janela)
entry_num2.pack()

# Operação
label_operacao = tk.Label(janela, text="Operação (+ - * /):")
label_operacao.pack()

entry_operacao = tk.Entry(janela)
entry_operacao.pack()

# Botão calcular
botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=10)

# Resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack()

# Executar janela
janela.mainloop()









