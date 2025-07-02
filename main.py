# Parte 1: Tuplas
# 1.1 Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), usando os valores 255 para vermelho, 102 para verde e 0 para azul.

cores = (255, 102, 0)

# 1.2 Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude e -34.8829 para longitude.

coordenadas = (-8.0578, -34.8829)

# 1.3 Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, contendo o ID 101, o username 'ana_silva' e a data de criação '2023-01-15'.

usuario = (101, 'ana_silva', '2023-01-15')

# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).

cores = (255, 102, 0)
r, g, b = cores
print(g)

# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas variáveis separadas chamadas latitude e longitude.

coordenadas = (-8.0578, -34.8829)
latitude, longitude = coordenadas

# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), que representa (id, nome, email), desempacote-a em variáveis e use a variável do nome para imprimir uma saudação.

usuario = (205, 'Carlos Pereira', 'carlos.p@email.com')
id, nome, email = usuario
print(f"Glória à Arstotzka, {nome}!")

# 1.7 Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), itere sobre ela e imprima cada papel.

administrador = ('moderador', 'editor', 'sysadmin')
for papel in administrador:
    print(papel)

# 1.8 Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.

usuario = (205, 'Carlos Pereira', 'carlos.p@email.com')
for dado in usuario:
    print(dado) 

# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.

cores = (255, 102, 0)
for componente in cores:
    print(componente)

# 1.10 Escreva uma função que verifique se um papel de usuário existe em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com os papéis 'editor' e 'usuario_comum'.

def verificador_papel_administrador(papel):
    resultado = False
    administrador = ('moderador', 'editor', 'sysadmin')
    for admin in administrador:
        if papel == admin:
            resultado = True
            return "Sim" if resultado else "Não"

print(f"O usuário é administrador? {verificador_papel_administrador('sysadmin')}")
print(f"O usuário é administrador? {verificador_papel_administrador('usuario_comum')}")

# 1.11 Dada a tupla de atribuições de equipe ('editor', 'leitor', 'editor', 'comentarista', 'editor'), conte e imprima o número de vezes que o papel 'editor' aparece.

atribuicoes_equipe = ('editor', 'leitor', 'editor', 'comentarista', 'editor')
contador_editor = atribuicoes_equipe.count('editor')
print(f"O editor aparece {contador_editor} vezes.")

# Parte 2: Dicionários
# 2.1 Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.

usuario_dicionario = {
    'username': 'bia_costa',
    'email': 'bia_costa@email.com',
    'data_adesao': '2024-05-21'
}

# 2.2 Crie um dicionário para um produto. Use as chaves 'id_produto', 'nome', 'preco' e 'estoque' com os respectivos valores 'XYZ-001', 'Fone de Ouvido Sem Fio', 299.90 e 150.

produto_dicionario = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': 299.90,
    'estoque': 150
}

# 2.3 Crie um dicionário vazio chamado preferencias_usuario.

preferencias_usuario = {}

# 2.4 Dado o dicionário de produto {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150}, acesse e imprima o preço original. Em seguida, atualize o preço para o valor promocional de 249.99.

produto_dicionario = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': 299.90,
    'estoque': 150
}
print(f"Preço original: {produto_dicionario['preco']}")
produto_dicionario['preco'] = 249.99
print(f"Preço promocional: {produto_dicionario['preco']}")

# 2.5 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}, adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.

perfil_usuario = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
perfil_usuario['telefone'] = '98765-4321'

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get() para tentar acessar o valor da chave 'ultimo_login'. Como a chave não existe, forneça o valor padrão 'Nunca logou'. Após a tentativa, bia fez o login, então atualize o dicionário para incluir a chave 'ultimo_login' com o valor '2024-05-22'.

perfil_usuario = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
perfil_usuario['ultimo_login'] = 'Nunca logou'
perfil_usuario.get('ultimo_login', 'Nunca logou')
perfil_usuario['ultimo_login'] = '2024-05-22'

# 2.7 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}, use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.

usuario_dicionario = {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}
del usuario_dicionario['telefone_fixo']

# 2.8 Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}, use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'. Armazene o valor retornado (o nome do produto) e imprima uma mensagem de confirmação.

catalogo_produtos_dicionario = {
    'XYZ-001': 'Fone de Ouvido Sem Fio',
    'ABC-002': 'Teclado Mecânico'
}
produto_removido = catalogo_produtos_dicionario.pop('XYZ-001', 'Produto não encontrado.')
print(f"Produto removido: {produto_removido}")

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' usando o método .pop(). Forneça o valor padrão 'Email não encontrado.' para evitar um erro.

perfil_usuario = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}
perfil_usuario.pop('email', 'Email não encontrado.')
print(perfil_usuario.get('email', 'Email não encontrado.'))

# 2.10 Dado o catálogo de produtos {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço'.

catalogo_produtos_dicionario = {
    'Fone de Ouvido': 249.99,
    'Teclado Mecânico': 450.00,
    'Mouse Gamer': 120.50
}
for produto in catalogo_produtos_dicionario:
    print(f"{produto}: R${catalogo_produtos_dicionario[produto]:.2f}")

# 2.11 Dado a lista de compras da feira {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço' e depois imprima o total.

lista_compras_feira = {
    'Tapioca': 18.99,
    'Queijo Manteiga': 45.00,
    'Ovos': 23.50
}
for item, preco in lista_compras_feira.items():
    print(f"{item}: R${preco:.2f}")
total = sum(lista_compras_feira.values())
print(f"Total: R${total:.2f}")

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'. O valor associado a essa chave deve ser outro dicionário contendo: 'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo' e 'cep': '01000-000'.

perfil_usuario = {
    'username': 'bia_costa'
}
perfil_usuario['endereco'] = {
    'rua': 'Rua das Flores, 123',
    'cidade': 'São Paulo',
    'cep': '01000-000'
}

# 2.13 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'profissao'. O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'.

perfil_usuario = {
    'username': 'bia_costa',
    'endereco': {
        'rua': 'Rua das Flores, 123',
        'cidade': 'São Paulo',
        'cep': '01000-000'
    }
}
perfil_usuario['profissao'] = {
    'cargo': 'Desenvolvedora',
    'empresa': 'Tech Solutions'
}

# 2.14 A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, acesse e imprima apenas o valor associado à chave 'cidade'.

perfil_usuario = {
    'username': 'bia_costa',
    'endereco': {
        'rua': 'Rua das Flores, 123',
        'cidade': 'São Paulo',
        'cep': '01000-000'
    },
    'profissao': {
        'cargo': 'Desenvolvedora',
        'empresa': 'Tech Solutions'
    }
}

cidade = perfil_usuario['endereco']['cidade']
print(f"Cidade: {cidade}")

# 2.15 Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' para 'Avenida Principal, 456'.

perfil_usuario = {
    'username': 'bia_costa',
    'endereco': {
        'rua': 'Rua das Flores, 123',
        'cidade': 'São Paulo',
        'cep': '01000-000'
    },
    'profissao': {
        'cargo': 'Desenvolvedora',
        'empresa': 'Tech Solutions'
    }
}

perfil_usuario['endereco']['rua'] = 'Avenida Principal, 456'

# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla (-8.0578, -34.8829) como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.

Locais = {
    (-8.0578, -34.8829): 'Recife',
    (-23.5505, -46.6333): 'São Paulo'
}

# 2.17 A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser a tupla (-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.

Locais = {
    (-8.0578, -34.8829): 'Recife',
    (-23.5505, -46.6333): 'São Paulo'
}
Locais[(-22.9068, -43.1729)] = 'Rio de Janeiro'

# 2.18 Escreva uma função que, dado um dicionário de locais, encontre o nome do local a partir de uma tupla de coordenadas. A função deve retornar uma mensagem padrão caso a coordenada não seja encontrada. Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).

def encontrar_Local_por_coordenadas(coordenadas):
    locais = {
        (-8.0578, -34.8829): 'Recife',
        (-23.5505, -46.6333): 'São Paulo',
        (-22.9068, -43.1729): 'Rio de Janeiro'
    }
    return locais.get(coordenadas, "Local não encontrado.")
print(encontrar_Local_por_coordenadas((-23.5505, -46.6333)))  # Deve retornar 'São Paulo'
print(encontrar_Local_por_coordenadas((0, 0)))  # Deve retornar 'Local não encontrado.'

# Parte 3: Vetores (Listas e NumPy)
# 3.1 Crie uma lista de hashtags (#) para redes sociais chamada tags_post com os valores ['#tecnologia', '#python', '#programacao']. Em seguida, adicione a tag '#dados' ao final da lista.

tags_post = ['#tecnologia', '#python', '#programacao']
tags_post.append('#dados')
print(tags_post)

# 3.2 Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados'], remova o elemento '#programacao'.

tags_post = ['#tecnologia', '#python', '#programacao', '#dados']
tags_post.remove('#programacao')
print(tags_post)

# 3.3 Dada a lista de tags ['#tecnologia', '#python', '#dados'], verifique se a string '#importante' existe na lista.

tags_post = ['#tecnologia', '#python', '#dados']
verificar_importante = '#importante' in tags_post
novo_booleano = "Sim" if verificar_importante else "Não"
print(f"A tag '#importante' está na lista? {novo_booleano}")

# 3.4 Importe a biblioteca numpy com o alias np. Crie um array NumPy a partir da lista de itens vendidos da semana, em que os itens são tuplas representando (produto, quantidade): [('camiseta', 10), ('calça', 5), ('sapato', 2)].

import numpy as np

itens_vendidos = np.array([('camiseta', 10), ('calça', 5), ('sapato', 2)])

# 3.5 Crie um array NumPy para armazenar as seguintes pontuações de um aluno: [0.85, 0.92, 0.78, 0.95, 0.88].

pontos_aluno = np.array([0.85, 0.92, 0.78, 0.95, 0.88])

# 3.6 Crie um array NumPy para armazenar as temperaturas em Celsius: [45.5, 46.0, 45.8, 47.1, 46.5].

temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])

# 3.7 Dado o array NumPy com tuplas de itens e preços precos = np.array([(Sapato, 100.0), (Calça, 250.0), (Camiseta, 80.0), (Tênis, 150.0)]), crie um novo array aplicando um desconto de 10% a todos os elementos (multiplicando por 0.9).

import numpy as np

# Separando os dados em duas listas
produtos = ['Sapato', 'Calça', 'Camiseta', 'Tênis']
precos = np.array([100.0, 250.0, 80.0, 150.0])  # Apenas os preços

# Aplicando desconto de 10%
precos_desconto = precos - (precos * 0.10)

# Exibindo os resultados
for produto, preco_com_desconto in zip(produtos, precos_desconto):
    print(f"{produto}: R$ {preco_com_desconto:.2f}")

# 3.8 Modifique o desconto aplicado acima para ser de 15% e imprima todos os valores originais e com desconto no formato, o <item> custava <preco_original>, agora custa <preco_com_desconto>.

produtos = ['Sapato', 'Calça', 'Camiseta', 'Tênis']
precos = np.array([100.0, 250.0, 80.0, 150.0])  # Apenas os preços
# Aplicando desconto de 15%
desconto = 0.15
precos_desconto = precos - (precos * desconto)

# Exibindo os resultados
for produto, preco_com_desconto in zip(produtos, precos_desconto):
    print(f"{produto} custava R${precos[produtos.index(produto)]:.2f}, agora custa R${preco_com_desconto:.2f}")

# 3.9 Dados o array de quantidades quantidades = np.array([1, 2, 3]) e o array de preços unitários precos_unitarios = np.array([15.0, 30.0, 22.5]), calcule o valor total por item multiplicando os dois arrays.

quantidades = np.array([1, 2, 3])
precos_unitarios = np.array([15.0, 30.0, 22.5])
valores_totais = quantidades * precos_unitarios
print("Valores totais por item:", valores_totais)

# 3.10 Dado o array de temperaturas em Celsius temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5]), converta todas as temperaturas para Fahrenheit usando a fórmula F = C * 1.8 + 32.

temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])
temperaturas_fahrenheit = temperaturas_celsius * 1.8 + 32
print(f"Temperaturas em Fahrenheit: {temperaturas_fahrenheit}")

# Parte 4: Matrizes (NumPy)
# 4.1 Crie e imprima uma matriz NumPy 3x4 (3 meses, 4 produtos) para representar as vendas com os dados: 
# [0, 1, 3]
# [9, 7, 4]
# [2, 6, 6]
# [3, 3, 3].

import numpy as np

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
print(f"Matriz de vendas:\n{vendas}")

# 4.2 Usando a matriz de vendas da questão anterior, imprima seu formato (atributo .shape) e sua transposta (atributo .T).

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
print(f"Formato da matriz de vendas: {vendas.shape}")
print(f"Matriz transposta:\n{vendas.T}")

# 4.3 Crie uma matriz NumPy 3x3 preenchida com zeros, com tipo de dado inteiro (dtype=int).

matriz_zeros = np.zeros((3, 3), dtype=int)
print(f"Matriz 3x3 preenchida com zeros:\n{matriz_zeros}")

# 4.4 Dada a matriz de vendas da questão 4.1, extraia e imprima a linha completa de dados para o segundo produto (linha de índice 1).

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
linha_produto_2 = vendas[1, :]
print(f"Linha do segundo produto: {linha_produto_2}")

# 4.5 Usando a mesma matriz de vendas, extraia e imprima a coluna completa de dados para o terceiro mês (coluna de índice 2).

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
coluna_mes_3 = vendas[:, 2]
print(f"Coluna do terceiro mês: {coluna_mes_3}")

# 4.6 Ainda com a matriz de vendas, acesse e imprima o valor específico do produto 3 (linha 2) no mês 2 (coluna 1).

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
valor_produto_3_mes_2 = vendas[2, 1]
print(f"Valor do produto 3 no mês 2: {valor_produto_3_mes_2}")

# 4.7 Dada a matriz de preços matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]]), crie uma nova matriz com todos os preços aumentados em 5%.

matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]])
matriz_precos_aumentada = matriz_precos * 1.05
print(f"Matriz de preços aumentada em 5%:\n{matriz_precos_aumentada}")

# 4.8 Dadas as matrizes de vendas com a quantidade de vendas de 4 produtos nos primeiros 3 meses do ano, vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]]) e vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]]), some-as para criar uma matriz vendas_globais.

vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]])
vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]])
vendas_globais = vendas_eua + vendas_europa
print(f"Matriz de vendas globais:\n{vendas_globais}")

# 4.9 Dada a matriz de vendas vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]]) (3 produtos x 2 meses) e o vetor de preços precos = np.array([4.99, 5.25, 2.19]), calcule a receita total por mês usando o produto escalar (np.dot).

vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]])
precos = np.array([4.99, 5.25, 2.19])
receita_total_mensal = np.dot(vendas_unidades.T, precos)
print(f"Receita total por mês: {receita_total_mensal}")

# 4.10 Usando a matriz de vendas da questão 4.1, calcule o total de unidades vendidas em cada mês (soma ao longo do eixo 0).

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
total_unidades_mensais = np.sum(vendas, axis=0)
print(f"Total de unidades vendidas por mês: {total_unidades_mensais}")

# 4.11 Usando a mesma matriz de vendas, calcule a média de vendas para cada produto (média ao longo do eixo 1).

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
media_vendas_produtos = np.mean(vendas, axis=1)
print(f"Média de vendas por produto: {media_vendas_produtos}")

# 4.12 A partir da matriz de vendas, encontre e imprima o valor máximo.

vendas = np.array([[0, 1, 3], [9, 7, 4], [2, 6, 6], [3, 3, 3]])
valor_maximo = np.max(vendas)
print(f"Valor máximo de vendas: {valor_maximo}")

# Parte 5: Desafios Finais
# Crie uma lista chamada usuarios contendo um dicionário para um usuário. Este dicionário deve ter: a chave 'id_usuario' com valor 101; a chave 'perfil' com um dicionário aninhado {'nome': 'Ana Silva', 'email': 'ana.s@email.com'}; a chave 'permissoes' com a tupla ('leitura', 'escrita'); e a chave 'mapa_calor_logins' com uma matriz NumPy de 7x24 preenchida com zeros. Implemente uma função registrar_login(usuario) que incremente o contador no mapa de calor do usuário correspondente ao dia e hora atuais.

import datetime as dt

def registrar_login(usuario):
    dia_atual = dt.datetime.now().weekday()
    hora_atual = dt.datetime.now().hour
    usuario['mapa_calor_logins'][dia_atual, hora_atual] += 1

usuarios = [
    {
        'id_usuario': 101,
        'perfil': {
            'nome': 'Ana Silva',
            'email': 'ana.s@email.com'
        },
        'permissoes': ('leitura', 'escrita'),
        'mapa_calor_logins': np.zeros((7, 24))
    }
]

# Escreva uma função analisar_inventario(catalogo) que processe um dicionário de produtos. A função deve retornar uma tupla contendo: 1. O valor total do inventário (soma de preco * estoque), 2. O nome do produto mais caro, e 3. Uma lista de produtos sem estoque. Teste a função com o catálogo: {'Laptop Gamer': {'preco': 7500.00, 'estoque': 10}, 'Mouse Vertical': {'preco': 350.00, 'estoque': 50}, 'Monitor 4K': {'preco': 4200.00, 'estoque': 15}, 'Webcam HD': {'preco': 250.00, 'estoque': 0}}.

def analisar_inventario(catalogo):
    valor_total = 0
    produto_mais_caro = ''
    preco_mais_caro = 0
    produtos_sem_estoque = []

    for produto, info in catalogo.items():
        valor_total += info['preco'] * info['estoque']
        if info['preco'] > preco_mais_caro:
            preco_mais_caro = info['preco']
            produto_mais_caro = produto
        if info['estoque'] == 0:
            produtos_sem_estoque.append(produto)

    return (valor_total, produto_mais_caro, produtos_sem_estoque)
catalogo = {
    'Laptop Gamer': {'preco': 7500.00, 'estoque': 10},
    'Mouse Vertical': {'preco': 350.00, 'estoque': 50},
    'Monitor 4K': {'preco': 4200.00, 'estoque': 15},
    'Webcam HD': {'preco': 250.00, 'estoque': 0}
}

resultado = analisar_inventario(catalogo)
print(f"Valor total do inventário: R${resultado[0]:.2f}")
print(f"Produto mais caro: {resultado[1]}")
print(f"Produtos sem estoque: {', '.join(resultado[2]) if resultado[2] else 'Nenhum'}")

# Projete uma classe SocialGraph para gerenciar amizades. O construtor deve inicializar um dicionário self.conexoes. Implemente os métodos adicionar_amizade(id1, id2) para criar uma amizade mútua e obter_amigos(id_usuario) para retornar a lista de amigos. Instancie a classe e adicione as seguintes amizades: (101, 205), (101, 308), (205, 400). Teste o método obter_amigos para os usuários 101, 205 e 999.

class SocialGraph:
    def __init__(self):
        self.conexoes = {}

    def adicionar_amizade(self, id1, id2):
        if id1 not in self.conexoes:
            self.conexoes[id1] = set()
        if id2 not in self.conexoes:
            self.conexoes[id2] = set()
        self.conexoes[id1].add(id2)
        self.conexoes[id2].add(id1)

    def obter_amigos(self, id_usuario):
        return list(self.conexoes.get(id_usuario, []))

social_graph = SocialGraph()
social_graph.adicionar_amizade(101, 205)
social_graph.adicionar_amizade(101, 308)
social_graph.adicionar_amizade(205, 400)

amigos_101 = social_graph.obter_amigos(101)
amigos_205 = social_graph.obter_amigos(205)
amigos_999 = social_graph.obter_amigos(999)
