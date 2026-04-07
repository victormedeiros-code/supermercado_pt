from database.database import criar_banco
from app.app import adicionar_produtos

criar_banco()

novos_produtos = [
    ('Açucar branco 250g', 1.25, 10, 'Alimentos básicos'),
    ('Sal refinado 500g', 1.50, 10, 'Alimentos básicos'),
    ('Feijão em lata 500g', 3.00, 10, 'Alimentos básicos'),
    ('Arroz tipo-1 1kg', 3.50, 10, 'Alimentos básicos'),
    ('Detergente manual de loiça', 1.50, 15, 'Produtos de limpeza')
]

for p in novos_produtos:
    adicionar_produtos(*p)