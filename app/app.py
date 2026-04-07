import sqlite3
from rich import print
from rich.panel import Panel
from rich.table import Table

def adicionar_produtos(nome, preco, stock, categoria):
    try:
        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, preco, stock, categoria) VALUES (?,?,?,?)
        ''',(nome, preco, stock, categoria))
        conn.commit()
        print(f'Produto: {nome} | Quantidade: {stock} | [yellow]Adicionado ao stock![/yellow]')
    except sqlite3.IntegrityError:
        print(f'[red]Erro:[/red] Já existe um produto chamado {nome}')
    finally:
        conn.close()


def atualizar_stock(id, novo_stock):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE produtos SET stock = ? WHERE id = ?', (novo_stock, id))
    conn.commit()
    caixa = Panel(f'ID:{id} [yellow]atualizado com sucesso![/yellow]', title='Atualização de stock')
    print(caixa)
    conn.close()
    



def mostrar_stock():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    dados = cursor.fetchall()

    tabela = Table(title='🛒 Stock Supermercado PT', header_style='bold green', border_style='blue')
    tabela.add_column('ID', justify='right', style='dim')
    tabela.add_column('Nome')
    tabela.add_column('Preço')
    tabela.add_column('stock')
    tabela.add_column('Categoria')
    tabela.add_column('Ultima atualização', style='italic blue')

    for linha in dados:
        tabela.add_row(
            str(linha[0]),
            linha[1],
            f'€{linha[2]:.2f}',
            str(linha[3]),
            linha[4],
            linha[5]
        )
    print(tabela)
    conn.close()
   
        
        
        
        

 