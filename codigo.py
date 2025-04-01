import pandas as pd
import matplotlib.pyplot as plt
import graficos_random
from collections import defaultdict
from datetime import datetime, timezone, timedelta

# ---------- Variáveis Globais ---------- #
lista_produto = []
historico_atividades = []
nome_limite = 30
# ---------- Variáveis Globais ---------- #

# ---------- Função para Carregar Dados do xlsx ---------- #

def carregar_dados_xlsx():
    try:
        # Carregar o arquivo Excel para um DataFrame
        df = pd.read_excel('produtos.xlsx')

        # Converter colunas específicas para os tipos necessários
        df['codigo'] = df['codigo'].astype(int)
        df['quantidade'] = df['quantidade'].astype(int)

        # Converter o DataFrame em uma lista de dicionários
        lista_produto.extend(df.to_dict(orient='records'))

        print('Dados carregados!')
    except FileNotFoundError:
        print("Arquivo 'produtos.xlsx' não encontrado. Criando um novo arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
# ---------- FIM ---------- #
def carregar_atividades_xlsx():
    try:
        # Carregar o arquivo Excel para um DataFrame
        df = pd.read_excel('atividades.xlsx')
        historico_atividades.extend(df.to_dict(orient='records'))
        print('Atividades Carregadas!')
    except FileNotFoundError:
        print("Arquivo 'atividades.xlsx' não encontrado. Criando um novo arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
# ---------- FIM ---------- #

# ---------- Adicionar Atividades ---------- #
def adicionar_atividade(acao, produto): # Função para mostrar todas as atividades realizadas
    fuso_horario = timezone(timedelta(hours=-3))  # -3 horas para o fuso horário de São Paulo
    timestamp_atual = datetime.now(fuso_horario).strftime('%d-%m-%Y %H:%M:%S')

    atividade = {
        'acao': acao,
        'produto': produto,
        'timestamp': timestamp_atual
    }

    historico_atividades.append(atividade.copy())
# ---------- FIM ---------- #

# ---------- Funções de carregamento de arquivo ---------- #
carregar_dados_xlsx()
carregar_atividades_xlsx()
# ---------- FIM ---------- #

# ---------- Visualizar Histórico de atividades ---------- #
def visualizar_historico():
    print('=' * 120)
    print("{:<20} {:<20} {:<50}".format('Timestamp', 'Ação', 'Produto'))
    print('-' * 120)

    for atividade in historico_atividades:
        timestamp = atividade['timestamp']
        acao = atividade['acao']
        produto = atividade['produto']

        print("{:<20} {:<20} {:<50}".format(str(timestamp), str(acao), str(produto)))

    print('=' * 120)
# ---------- FIM ---------- #

# ---------- Salvar atividades no xlsx ---------- #
def salvar_atividades_xlsx():  # Função para salvar as atividades no arquivo xlsx
    fieldnames = ['acao', 'produto', 'timestamp']
    # Criar DataFrame a partir do histórico de atividades
    df = pd.DataFrame(historico_atividades, columns=fieldnames)
    # Salvar o DataFrame em um arquivo Excel
    df.to_excel('atividades.xlsx', index=False)
# ---------- FIM ---------- #

# ---------- Função para Salvar Dados em CSV ---------- #
def salvar_dados_xlsx():  # Função para salvar os produtos no arquivo xlsx
    fieldnames = ['codigo', 'nome', 'unidade', 'quantidade', 'categoria', 'valor','dataCadastro']
    # Criar DataFrame a partir da lista de produtos
    df = pd.DataFrame(lista_produto, columns=fieldnames)
    # Salvar o DataFrame em um arquivo Excel
    df.to_excel('produtos.xlsx', index=False)
# ---------- FIM ---------- #

# ---------- Função para Mostrar Tabela Produtos ---------- #
def mostrar_produtos():
    print("{:<12} {:<35} {:<17} {:<17} {:<17} {:<12} {:<12}".format('Código', 'Nome','Unidade',
                                                    'Quantidade','Categoria','Valor', 'Data Cadastro'))
    print("-" * 130)
    lista_produto_ordenada = sorted(lista_produto, key=lambda x: x['codigo'])
    for produto in lista_produto_ordenada:
        print("{:<12} {:<35} {:<17} {:<17} {:<17} R$ {:<12} {:<12}".format(
            produto['codigo'],
            produto['nome'],
            produto['unidade'],
            produto['quantidade'],
            produto['categoria'],
            produto['valor'],
            produto['dataCadastro']
        ))     
# ---------- FIM ---------- #

# ---------- Cadastrar Produto ---------- #
def cadastrar_produto_aleatorio():
    print('='*35, '  BEM-VINDO AO MENU CADASTRAR PRODUTO  ', '='*35)
    # Validação da entrada de dados e algumas exceções para números int e float
    
    while True:
        cadastro = input('Escolha a opção desejada:\n' +
                             '1 - Gerar Produtos Aleatórios:\n' +
                             '2 - Cadastrar Produto:\n' +
                             '3 - Retornar:\n' +
                             '-> ')
        if cadastro == '1':
            cadastro_aleatorio = input('Escolha a opção desejada:\n' +
                                    '1 - Cadastrar 3 produtos:\n' +
                                    '2 - Cadastrar 5 produtos:\n' +
                                    '3 - Retornar:\n' +
                                    '-> ')
            
            if cadastro_aleatorio == '1':
                produto_increment = []
                for _ in range(3):
                    produto_aleatorio = graficos_random.gerar_produto_aleatorio()
                    lista_produto.append(produto_aleatorio.copy())
                    adicionar_atividade('Cadastrar Produto', produto_aleatorio)
                    salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
                    salvar_dados_xlsx()  # função para salvar as alterações
                    produto_increment.append(produto_aleatorio)
                print("{:<12} {:<35} {:<17} {:<17} {:<17} {:<12} {:<12}".format('Código', 'Nome','Unidade',
                                                                'Quantidade','Categoria','Valor', 'Data Cadastro'))
                print("-" * 130)
                for produto in produto_increment:
                    print("{:<12} {:<35} {:<17} {:<17} {:<17} R$ {:<12} {:<12}".format(
                        produto['codigo'],
                        produto['nome'],
                        produto['unidade'],
                        produto['quantidade'],
                        produto['categoria'],
                        produto['valor'],
                        produto['dataCadastro']
                    ))     
                    
            elif cadastro_aleatorio == '2':
                produto_increment = []
                for _ in range(5):
                    produto_aleatorio = graficos_random.gerar_produto_aleatorio()
                    lista_produto.append(produto_aleatorio.copy())
                    adicionar_atividade('Cadastrar Produto', produto_aleatorio)
                    salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
                    salvar_dados_xlsx()
                    produto_increment.append(produto_aleatorio)
                    
                print("{:<12} {:<35} {:<17} {:<17} {:<17} {:<12} {:<12}".format('Código', 'Nome','Unidade',
                                                                'Quantidade','Categoria','Valor', 'Data Cadastro'))
                print("-" * 130)
                for produto in produto_increment:
                    print("{:<12} {:<35} {:<17} {:<17} {:<17} R$ {:<12} {:<12}".format(
                        produto['codigo'],
                        produto['nome'],
                        produto['unidade'],
                        produto['quantidade'],
                        produto['categoria'],
                        produto['valor'],
                        produto['dataCadastro']
                    ))
            else:
                print("Opção Invãlida. Digite novamente: ")    
# ----------             else:
                print("Opção inválida. Tente novamente")
        elif cadastro == '2':
            cadastrar()
        elif cadastro == '3':
            return
        else:
            print('Opção Inválida. Tente novamente:\n')
            continue
    
def cadastrar():
    while True:
        try:
            codigo = int(input('Digite o Código "ID" do produto: '))
            if any(produto['codigo'] == codigo for produto in lista_produto):
                print('Código já cadastrado. Por favor, insira um código diferente.\n')
            else:
                break
        except ValueError:
            print('Digite um número inteiro válido')

    while True:
        nome = input(f'NOME do produto (limite de {nome_limite} caracteres): ').lower()
        if nome and len(nome) <= nome_limite:
            break
        else:
          print(f"O nome deve ter no máximo {nome_limite} caracteres. Tente novamente.\n")

    while True:
        unidade = input('UNIDADE DE MEDIDA do produto (LT, CM, KG ou UN): ').strip().lower()
        if unidade in ['lt', 'cm', 'kg', 'un']:
            break
        else:
          print("Opção inválida. Por favor, escolha entre LT, CM, KG ou UN.\n")

    while True:
        try:
            quantidade = int(input('Digite a QUANTIDADE atual em unidade: '))
            break
        except ValueError:
          print('Por favor, digite um número inteiro válido.\n')

    while True:
        categoria = input('CATEGORIA do produto (insumo, limpeza, escritorio, eletronico): ').strip().lower()
        if categoria in ['insumo', 'limpeza', 'escritorio', 'eletronico']:
            break
        else:
          print("Opção inválida. Por favor, escolha entre insumo, limpeza, escritorio ou eletronico.\n")

    while True:
        try:
            valor = input('VALOR do produto R$: ')
            valor = float(valor.replace(",","."))
            break
        except ValueError:
            print("Digite um valor Válido")

    # Mostra a data que foi cadastrado o produto, no caso que será
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%Y-%m-%d")
    dataCadastro = data_formatada
    print("Data de Cadastro:", dataCadastro)

    dicionario_produto = {'codigo': codigo,
                          'nome': nome,
                          'unidade': unidade,
                          'quantidade': quantidade,
                          'categoria': categoria,
                          'valor': valor,
                          'dataCadastro': dataCadastro
                          }

    lista_produto.append(dicionario_produto.copy()) # Cria uma cópia da lista de produtos ao invés de modificala
    adicionar_atividade('Cadastrar Produto', dicionario_produto.copy())
    salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
    salvar_dados_xlsx()  # função para salvar as alterações
# ---------- FIM ---------- #

# ---------- Alterar Produto ---------- #
def alterar_produto(): # Função para alterar o produto cadastrado pelo código ou 'ID'
    print('='*35, '  BEM-VINDO AO MENU ALTERAR PRODUTO  ', '='*35)
    if not lista_produto:
        print('Nenhum produto cadastrado')
        return

    while True:
        alterar_menu = input('Escolha a opção desejada:\n' +
                             '1 - Alterar todos:\n' +
                             '2 - Alterar Código:\n' +
                             '3 - Alterar Nome:\n' +
                             '4 - Alterar Unidade:\n' +
                             '5 - Alterar Quantidade:\n' +
                             '6 - Alterar Valor:\n' +
                             '7 - Alterar Categoria:\n' + 
                             '8 - Sair\n'
                             '-> ')
        if alterar_menu == '1':
            alterar_todos()
        elif alterar_menu == '2':
            alterar_codigo()
        elif alterar_menu == '3':
            alterar_nome()
        elif alterar_menu == '4':
            alterar_unidade()
        elif alterar_menu == '5':
            alterar_quantidade() 
        elif alterar_menu == '6':
            alterar_valor() 
        elif alterar_menu == '7':
            alterar_categoria()
        elif alterar_menu == '8':
            return
        else:
            print('Opção Inválida. Tente novamente')
            continue
# ---------- FIM ---------- #

# ---------- Função alterar todos ---------- #
def alterar_todos(): # Função para alterar tudo de uma vez só
    
    mostrar_produtos()
    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto: # Busca na lista de produtos o cósigo digitado
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
                try:
                    novo_codigo = int(input('Novo Código do produto: '))
                    if any(produto['codigo'] == novo_codigo for produto in lista_produto):
                        print('Código já cadastrado. Por favor, insira um código diferente.\n')
                    else:
                        produto['codigo'] = novo_codigo
                        break
                except ValueError:
                    print('Por favor, digite um número inteiro válido:\n')

            while True:
                produto['nome'] = input('Novo Nome do produto: ').lower()
                if len(produto['nome']) <= nome_limite:
                  break
                else:
                  print(f'NOME do produto (limite de {nome_limite} caracteres): ')

            while True:
              produto['unidade'] = input('Nova UNIDADE DE MEDIDA do produto: ').strip().lower()
              if produto['unidade'] in ['lt', 'cm', 'kg', 'un']:
                break
              else:
                print('Opção Inválida. Por favor, escolha entre, LT, CM, KG OU UN.\n')

            while True:
                try:
                    produto['quantidade'] = int(input('Nova QUANTIDADE do produto: '))
                    break
                except ValueError:
                  print('Por favor, digite um número inteiro válido.\n')

            while True:
                produto['categoria'] = input('Nova CATEGORIA do produto: ').strip().lower()
                if produto['categoria'] in ['insumo', 'limpeza', 'escritorio', 'eletronico']:
                  break
                else:
                  print('Opção Inválida. Por favor, escolha entre insumo, limpeza, escritorio ou eletronico.\n')

            adicionar_atividade('Alterar Produto', produto)
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # Função para salvar as alterações

            print('Produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Função alterar codigo ---------- #
def alterar_codigo():
    
    mostrar_produtos()

    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto:
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
                try:
                    novo_codigo = int(input('Novo Código do produto: '))
                    if any(produto['codigo'] == novo_codigo for produto in lista_produto):
                        print('Código já cadastrado. Por favor, insira um código diferente.\n')
                    else:
                        produto['codigo'] = novo_codigo
                        break
                except ValueError:
                    print('Por favor, digite um número inteiro válido:\n')

            adicionar_atividade('Alterar Código Produto', produto['codigo'])
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # função para salvar as alterações

            print('Codigo do produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Função alterar nome ---------- #
def alterar_nome():

    mostrar_produtos()

    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto:
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
                produto['nome'] = input('Novo Nome do produto: ').strip()
                if len(produto['nome']) <= nome_limite:
                  break
                else:
                  print(f'NOME do produto (limite de {nome_limite} caracteres): ')

            adicionar_atividade('Alterar Nome Produto', produto['nome'])
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # função para salvar as alterações

            print('Nome do produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Função alterar unidade ---------- #
def alterar_unidade():

    mostrar_produtos()

    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto:
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
                print('UNIDADES: lt - cm - kg - un')
                produto['unidade'] = input('Nova UNIDADE DE MEDIDA do produto: ').strip().lower()
                if produto['unidade'] in ['lt', 'cm', 'kg', 'un']:
                  break
                else:
                  print('Opção Inválida. Por favor, escolha entre, LT, CM, KG OU UN.\n')

            adicionar_atividade('Alterar Unidade Produto', produto['unidade'])
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # função para salvar as alterações

            print('Unidade do produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Função alterar quantidade ---------- #
def alterar_quantidade():

    mostrar_produtos()

    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto:
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
              try:
                  produto['quantidade'] = int(input('Nova QUANTIDADE do produto: '))
                  break
              except ValueError:
                print('Por favor, digite um número inteiro válido.\n')

            adicionar_atividade('Alterar Quantidade Produto', produto['quantidade'])
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # função para salvar as alterações

            print('QUANTIDADE do produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Função alterar CATEGORIA ---------- #
def alterar_categoria():

    mostrar_produtos()

    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto:
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
                print('CATEGORIAS: insumo - limpeza - escritorio - eletronico')
                produto['categoria'] = input('Nova CATEGORIA do produto: ').strip().lower()
                if produto['categoria'] in ['insumo', 'limpeza', 'escritorio', 'eletronico']:
                    break
                else:
                    print('Opção Inválida. Por favor, escolha entre insumo, limpeza, escritorio ou eletronico.\n')

            adicionar_atividade('Alterar CATEGORIA Produto', produto['categoria'])
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # função para salvar as alterações

            print('CATEGORIA do produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Função alterar valor ---------- #
def alterar_valor():

    mostrar_produtos()

    while True:
        try:
            codigo_alterar = int(input('Digite o código do produto que deseja alterar: '))
            break
        except ValueError:
            print("Digite um número inteiro. Tente novamente: ")
    for produto in lista_produto:
        if produto['codigo'] == codigo_alterar:
            print('Produto encontrado. corrige os dados desejados:')
            while True:
              try:
                  produto['valor'] = float(input('Novo VALOR do produto R$: ').replace(",","."))
                  break
              except ValueError:
                print('Por favor, digite um número inteiro válido.\n')

            adicionar_atividade('Alterar Valor Produto', produto['valor'])
            salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
            salvar_dados_xlsx()  # função para salvar as alterações

            print('VALOR do produto alterado com sucesso!')
            return
    print('Produto não encontrado com o código fornecido\n')
# ---------- FIM ---------- #

# ---------- Alterar Produto ---------- #

# ---------- Remover Produto ---------- #
def remover_produto(): # Função para remover produto pelo código
    print('='*35, '  BEM-VINDO AO MENU REMOVER PRODUTO  ', '='*35)
    mostrar_produtos()

    remover = int(input('Digite com o CÓDIGO com produto que deseja remover: '))

      # Verifica se o código do produto a ser removido existe
    if any(produto['codigo'] == remover for produto in lista_produto):
          for produto in lista_produto:
              if produto['codigo'] == remover:
                  adicionar_atividade('Remover Produto', produto)
                  lista_produto.remove(produto)
                  salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
                  salvar_dados_xlsx()  # função para salvar as alterações
                  print('Produto Removido!!')
                  break
                  return
    else:
        print('Produto não encontrado com o código fornecido.\n')
        return
# ---------- FIM ---------- #

# ---------- Adicionar ---------- #
def adicionar_quantidade(): # Função para somente adicionar quantidade em quantidade
    print('='*35, '  BEM-VINDO AO MENU ADICIONAR QUANTIDADE  ', '='*35)

    if not lista_produto:
        print('Nenhum produto cadastrado')
        return

    mostrar_produtos()

    codigo_adicionar = int(input('Digite o código do produto que deseja adicionar quantidade: '))

    for i, produto in enumerate(lista_produto):
        if produto['codigo'] == codigo_adicionar:
            while True:
                try:
                    quantidade_adicionar = int(input('Digite a quantidade que deseja adicionar: '))
                    lista_produto[i]['quantidade'] += quantidade_adicionar
                    adicionar_atividade('Quantidade adicionada', quantidade_adicionar)
                    salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
                    salvar_dados_xlsx()  # função para salvar as alterações
                    print(f'Quantidade adicionada com sucesso! Nova quantidade: {lista_produto[i]["quantidade"]}')
                    break
                except ValueError:
                    print('Por favor, digite um número inteiro válido.')
            return

    print('Produto não encontrado com o código fornecido')
# ---------- FIM ---------- #

# ---------- Retirar ---------- #
def retirar_quantidade(): # Função para apenas retirar quantidade em retirar
    print('='*35, '  BEM-VINDO AO MENU RETIRAR QUANTIDADE  ', '='*35)

    if not lista_produto:
        print('Nenhum produto cadastrado')
        return

    mostrar_produtos()

    codigo_retirar = int(input('Digite o código do produto que deseja retirar quantidade: '))

    for i, produto in enumerate(lista_produto):
        if produto['codigo'] == codigo_retirar:
            while True:
                try:
                    quantidade_retirar = int(input('Digite a quantidade que deseja retirar: '))
                    if 0 < quantidade_retirar <= produto['quantidade']:
                        lista_produto[i]['quantidade'] -= quantidade_retirar
                        adicionar_atividade('Quantidade retirada', quantidade_retirar)
                        salvar_atividades_xlsx()  # Função para salvar todas as atividades no histórico no CSV
                        salvar_dados_xlsx()  # função para salvar as alterações
                        print(f'Quantidade retirada com sucesso! Nova quantidade: {lista_produto[i]["quantidade"]}')
                        break
                    else:
                        print(
                            'Quantidade inválida. Certifique-se de que a quantidade é maior que zero e menor ou igual à quantidade atual.')
                except ValueError:
                    print('Por favor, digite um número inteiro válido.')
            return

    print('Produto não encontrado com o código fornecido')
# ---------- FIM ---------- #

# ---------- Exibir Relatório ---------- #
def exibir_relatorio(): # Função para exibir o relatório de tudo, quanto por categoria para fazer uma divisão de departamentos ou também um relatório de tudo e com tudo
    print('='*35, '  BEM-VINDO AO MENU EXIBIR RELATÓRIO  ', '='*35)

    while True:
        opcao_relatorio = input('Escolha a opção desejada:\n' +
                                '1 - Exibir Produtos Cadastrados\n' +
                                '2 - Exibir Produtos por Categoria\n' +
                                '3 - Retornar\n' +
                                '-> ')

        if opcao_relatorio == '1':
            print(' ---------- Relatório Geral ---------- \n')
            if not lista_produto:
                print("Nenhum produto cadastrado.")
            else:
                mostrar_produtos()
                print("-" * 130)
                
        elif opcao_relatorio == '2':
            relatorio_por_categoria()      
        elif opcao_relatorio == '3':
            return
        else:
            print('Opção Inválida. Tente novamente\n' +
                  '=' * 50)
            continue

def relatorio_por_categoria():
    print(' ---------- Relatório Por Categoria ---------- \n')
    print('CATEGORIAS: insumo - limpeza - escritorio - eletronico')
    categoria_desejada = input('Digite a categoria do produto: ').lower()
    produtos_categoria = [produto for produto in lista_produto if produto['categoria'] == categoria_desejada]
    
    if not produtos_categoria:
        print("Nenhum produto cadastrado nessa categoria.")
        return []
    
    print(f"Produtos da categoria '{categoria_desejada}':")
    print("-" * 130)
    print("{:<12} {:<35} {:<17} {:<17} {:<17} {:<12} {:<12}".format(
        'Código', 'Nome', 'Unidade', 'Quantidade', 'Categoria', 'Valor', 'Data Cadastro'
    ))
    print("-" * 130)
    
    produtos_categoria_ordenada = sorted(produtos_categoria, key=lambda x: x['codigo'])
    for produto in produtos_categoria_ordenada:
        print("{:<12} {:<35} {:<17} {:<17} {:<17} R$ {:<12} {:<12}".format(
            produto['codigo'],
            produto['nome'],
            produto['unidade'],
            produto['quantidade'],
            produto['categoria'],
            produto['valor'],
            produto['dataCadastro']
        ))
    
    return produtos_categoria_ordenada

def exibir_graficos():
    print('='*35, '  BEM-VINDO AO MENU EXIBIR RELATÓRIO  ', '='*35)

    while True:
        opcao_graficos = input('Escolha a opção desejada:\n' +
                                '1 - Exibir Valor total por categoria\n' +
                                '2 - Exibir Valor total por Mes de Cadastro\n' +
                                '3 - Exibir relátorio de chegada\n' +
                                '4 - Exibir relátorio de retirada\n' +
                                '5 - Exibir Valor total em estoque\n' +
                                '6 - Retornar\n' +
                                '-> ')
        if opcao_graficos == '1':
            valor_por_categoria()
        elif opcao_graficos == '2':
            valor_por_dataCadastro()
        elif opcao_graficos == '3':
            relatorio_chegada()
        elif opcao_graficos == '4':
            relatorio_retirada()
        elif opcao_graficos == '5':
            valor_total_em_estoque()
        elif opcao_graficos == '6':
            return
        else:
            print("Opção Inválida. Tente novamente")

def valor_por_categoria():
    produtos_categoria = relatorio_por_categoria()
    valor_total = 0
    produtos_categoria_ordenada = sorted(produtos_categoria, key=lambda x: x['codigo'])
    for produto in produtos_categoria_ordenada:   
        valor_total += produto['valor'] * produto['quantidade']
    print("-" * 130)
    print('Total: ' + (' ' * 111) + 'R$ ' + '{:.2f}'.format(valor_total))
    print("-" * 130 + '\n')

    while True: 
        imprimir = input("Deseja imprimir um grafico ? (Y/N)\n").lower()
        if imprimir == 'y':
            if produtos_categoria:
                # Agrupar produtos pelo nome e somar os valores totais
                agrupados = defaultdict(float)
                for produto in produtos_categoria:
                    valor_total = produto['valor'] * produto['quantidade']
                    agrupados[produto['nome']] += valor_total

                # Separar os nomes e os valores totais para o gráfico
                nomes_produtos = list(agrupados.keys())
                valores_totais = list(agrupados.values())
                
                # Gera o gráfico de barras
                plt.figure(figsize=(17, 7.5))
                bars = plt.bar(nomes_produtos, valores_totais, color='skyblue', label='Valores', width=0.6)

                # Personalização do gráfico
                plt.title("Valores Totais por Produto (Agrupados)", fontsize=20, fontweight='bold', color='darkblue', pad=20)
                plt.xlabel("Produtos", fontsize=14, fontweight='bold', color='darkgreen')
                plt.ylabel("Valor Total (R$)", fontsize=14, fontweight='bold', color='darkgreen')
                plt.xticks(rotation=45, ha='right', fontsize=12, color='darkblue')
                plt.yticks(fontsize=12, color='darkblue')
                plt.grid(True, linestyle='dashed', alpha=0.5, color='gray')
                plt.legend(loc='upper left', fontsize=12)

                # Adiciona os valores no topo de cada barra
                for bar, valor_total in zip(bars, valores_totais):
                    plt.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height(),
                        f"R${valor_total:,.2f}",
                        ha='center',
                        va='bottom',
                        fontsize=12,
                        fontweight='bold',
                        color='black'
                    )

                # Ajusta o layout e exibe o gráfico
                plt.tight_layout()
                plt.show()
            else:
                print("Nenhum gráfico a ser exibido, pois não há produtos na categoria selecionada.")
        elif imprimir == 'n':
            print("Encerrando...")
        else:
            print("Opção Inválida. Tente novamente: ")

def valor_por_dataCadastro():
    ano = int(input("Digite o ano (ex: 2025): "))
    mes = int(input("Digite o mês (1-12): "))
    df = pd.read_excel("produtos.xlsx")
    df['dataCadastro'] = pd.to_datetime(df['dataCadastro'], dayfirst=True)
    produtos_filtrados = df[(df['dataCadastro'].dt.year == ano) & (df['dataCadastro'].dt.month == mes)]
    print("\nProdutos cadastrados em {}/{}:".format(mes, ano))
    print("-" * 130)
    if produtos_filtrados.empty:
        print("Nenhum produto encontrado.")
    else:
        print("{:<12} {:<35} {:<17} {:<17} {:<17} {:<12} {:<12}".format('Código', 'Nome','Unidade',
                                                    'Quantidade','Categoria','Valor', 'Data Cadastro'))
        print("-" * 130)
        for _, produto in produtos_filtrados.iterrows():
            print("{:<12} {:<35} {:<17} {:<17} {:<17} R$ {:<12} {:<12}".format(
                produto['codigo'],
                produto['nome'],
                produto['unidade'],
                produto['quantidade'],
                produto['categoria'],
                produto['valor'],
                produto['dataCadastro'].strftime('%d-%m-%Y')
            ))
        valor_total = 0
        for _, produto in produtos_filtrados.iterrows():   
            valor_total += produto['valor'] * produto['quantidade']   
        print("-" * 130)
        print('Total: ' + (' ' * 111) + 'R$ ' + '{:.2f}'.format(valor_total))
        print("-" * 130 + '\n')
            
    while True:
        imprimir = input("Deseja imprimir um grafico ? (Y/N)\n").lower()
        if imprimir == 'y':
            produtos_filtrados['valor_total'] = produtos_filtrados['valor'] * produtos_filtrados['quantidade']

            plt.figure(figsize=(17, 7.5))
            bars = plt.bar(
                produtos_filtrados['dataCadastro'].dt.strftime('%d/%m/%Y'), 
                produtos_filtrados['valor_total'], 
                color='skyblue', 
                label='Valores', 
                width=0.6
            )

            plt.title("Valores por Mês", fontsize=20, fontweight='bold', color='darkblue', pad=20)
            plt.xlabel("Data", fontsize=14, fontweight='bold', color='darkgreen')
            plt.ylabel("Soma dos Valores (R$)", fontsize=14, fontweight='bold', color='darkgreen')

            for bar in bars:
                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    f"R${bar.get_height():,.2f}",
                    ha='center',
                    va='bottom',
                    fontsize=12,
                    fontweight='bold',
                    color='black'
                )
            plt.xticks(rotation=45, ha='right', fontsize=12, color='darkblue')
            plt.yticks(fontsize=12, color='darkblue')
            plt.grid(True, linestyle='dashed', alpha=0.5, color='gray')
            plt.legend(loc='upper left', fontsize=12)
            plt.tight_layout()
            plt.show()
        elif imprimir == 'n':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Digite 'Y' para sim ou 'N' para não.")                
def relatorio_chegada():
    pass

def relatorio_retirada():
    pass

def valor_total_em_estoque():
    opcao_graficos = input('Escolha a opção desejada:\n' +
                        '1 - Exibir Todos os Produtos com valor\n' +
                        '2 - Exibir Gráfico Total\n' +
                        '3 - Retornar\n' +
                        '-> ')
    
    if opcao_graficos == '1':
        mostrar_produtos()
        valor_total = 0
        for produto in lista_produto:   
            valor_total += produto['valor'] * produto['quantidade']
        print("-" * 130)
        print('Total: ' + (' ' * 109) + 'R$ ' + '{:.2f}'.format(valor_total))
        print("-" * 130 + '\n')
        return valor_total
        
    elif opcao_graficos == '2':
        graficos_random.grafico()
    
    elif opcao_graficos == '3':
        return
    else:
        print("Opção Inválida. Tente novamente: ")
    # # ---------- FIM ---------- #
    
# ---------- Inicio Main ---------- #
while True: # Main principal com todas outras opção de função
    opcao_principal = input('CntEstoque - P.I.P.E.\n'
                            "================================"
                            "       MENU PRINCIPAL        "
                            "================================\n"
                            'Escolha a opção desejada:\n' +
                            "================================\n"
                            '1 - Cadastrar Produto\n' +
                            '2 - Alterar Produto\n' +
                            '3 - Remover Produto\n' +
                            '4 - Adicionar Quantidade\n' +
                            '5 - Retirar Quantidade\n' +
                            '6 - Exibir Relatório\n' +
                            '7 - Visualizar Histórico\n' +
                            '8 - Exibir Gráficos\n' +
                            '9 - Sair\n' +
                            "===============================\n"
                            '-> ')
    if opcao_principal == '1':
        cadastrar_produto_aleatorio()
    elif opcao_principal == '2':
        alterar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        adicionar_quantidade()
    elif opcao_principal == '5':
        retirar_quantidade()
    elif opcao_principal == '6':
        exibir_relatorio()
    elif opcao_principal == '7':
        visualizar_historico()
    elif opcao_principal == '8':
        exibir_graficos()
    elif opcao_principal == '9':
        break
    else:
        print('Opção Inválida. Tente novamente')
        continue
# ---------- Fim Main ---------- #