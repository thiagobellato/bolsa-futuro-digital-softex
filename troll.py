import pyautogui
import time


def main():
    """
    Executa a automação de alerta de desligamento (de brincadeira).
    """

    # --- Etapa 1: Caixa de Alerta de Desligamento ---
    # Exibe a caixa de alerta inicial
    pyautogui.alert(
        text='Foram encontrados 23.698 arquivos com vírus, o PC será desligado em 15 segundos! \nClique em OK e digite "cancelar" para abortar.',
        title="Aviso de Desligamento",
    )

    # --- Etapa 2: Atraso para o usuário se preparar ---
    time.sleep(10)

    # --- Etapa 3: Input para Cancelar ---
    # Pede para o usuário digitar 'cancelar'
    resposta = pyautogui.prompt(
        text='Digite "cancelar" para abortar o desligamento.',
        title="Cancelar Desligamento",
    )

    # --- Etapa 4: Lógica de "Desligamento" ou Cancelamento ---
    if resposta and resposta.lower() == "cancelar":
        pyautogui.alert(text="Desligamento cancelado.", title="Cancelado")
    else:
        # Se o usuário não digitou 'cancelar' ou fechou a caixa, o script prossegue
        pyautogui.alert(
            text="Que pena! Eu ia desligar de verdade, mas é só uma brincadeira! :)",
            title="É uma brincadeira!",
        )


if __name__ == "__main__":
    main()
