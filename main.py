import os

ARQUIVO = "tarefas.txt"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    tarefas = []
    for linha in linhas:
        nome, status = linha.strip().split(" | ")
        tarefas.append({"nome": nome, "status": status})
    return tarefas


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for t in tarefas:
            f.write(f"{t['nome']} | {t['status']}\n")


def adicionar_tarefa(tarefas):
    nome = input("\nDigite o nome da tarefa: ")
    tarefas.append({"nome": nome, "status": "pendente"})
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    print("\n📋 Lista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. {t['nome']} - {t['status']}")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    indice = int(input("\nNúmero da tarefa a concluir: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefas[indice]["status"] = "concluída"
        print("Tarefa concluída!")
    else:
        print("Índice inválido.")


def remover_tarefa(tarefas):
    listar_tareras(tarefas)
    indice = int(input("\nNúmero da tarefa a remover: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida!")
    else:
        print("Índice inválido.")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n===== SISTEMA DE TAREFAS =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("Saindo... Tarefas salvas!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
