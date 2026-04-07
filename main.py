from app.app import mostrar_stock, atualizar_stock
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
import os

def limpar_ecra():
    os.system('cls')



def main():
    menu = Panel(
        '[orange1][1] ->[/] Mostrar stock \n[orange1][2] ->[/] Atualizar Stock \nEscolha uma das opções para continuar ',
        title='[bold orange]🛒 Supermercado PT 🛒[/]',
        border_style='orange1',
        expand=False
    )


    while True:
        limpar_ecra()
        print(menu)
        opcao = Prompt.ask(' [orange1]--->[/orange1]')
        print(menu)
        if opcao == '1':
            limpar_ecra()
            mostrar_stock()
            input('\nPressione [ENTER] para voltar ao menu...')
        elif opcao == '2':
            limpar_ecra()
            stock_id = Prompt.ask('[yellow]ID:[/] ')
            novo_stock = Prompt.ask('[yellow]Novo stock:[/] ')
            atualizar_stock(stock_id,novo_stock)
            input('\nStock atualizado! Pressione [ENTER] para voltar ao menu...')




if __name__=='__main__':
    main()




