def gerar_produto_aleatorio():
    import random
    from datetime import datetime, timedelta
        
    # Função para gerar uma data aleatória dentro de 1 ano
    hoje = datetime.now()
    inicio = datetime(2024, 1, 1)
    dias_diferenca = (hoje - inicio).days
    dias_aleatorios = random.randint(0, dias_diferenca)
    data = hoje - timedelta(days=dias_aleatorios)
    dataCadastro = data.strftime("%d-%m-%Y")
    
    nome = ''
    unidade = ''
    quantidade = 0
    valor = 0.0
    categoria = random.choice(['insumo', 'limpeza', 'escritorio', 'eletronico']).lower().strip()
    if categoria == 'insumo':
        codigo = random.randint(1, 500)
        nome = random.choice([
                            "Farinha de Trigo 500g",
                            "Açúcar Refinado 1kg",
                            "Óleo de Soja 900ml",
                            "Leite em Pó 400g",
                            "Arroz Integral 1kg",
                            "Milho em Grãos 500g",
                            "Cacau em Pó 250g",
                            "Sal Grosso 1kg",
                            "Fermento Biológico 10g",
                            "Manteiga sem Sal 200g",
                            "Amido de Milho 200g",
                            "Creme de Leite 300g",
                            "Polvilho Doce 500g",
                            "Ervas Finas 30g",
                            "Café Solúvel 100g",
                            "Farinha de Mandioca 1kg",
                            "Condimentos Mix 50g",
                            "Leite Condensado 395g",
                            "Gelatina Incolor 12g",
                            "Massa de Tomate 300g"
        ])
        if nome == 'Farinha de Trigo 500g':
            valor = 5.6
        elif nome == 'Açúcar Refinado 1kg':
            valor = 4.8
        elif nome == 'Óleo de Soja 900ml':
            valor = 8.98
        elif nome == 'Leite em Pó 400g':
            valor = 14.86
        elif nome == 'Arroz Integral 1kg':
            valor = 5.99
        elif nome == 'Milho em Grãos 500g':
            valor = 4.5
        elif nome == 'Cacau em Pó 250g':
            valor = 8.9
        elif nome == 'Sal Grosso 1kg':
            valor = 3.2
        elif nome == 'Fermento Biológico 10g':
            valor = 1.5
        elif nome == 'Manteiga sem Sal 200g':
            valor = 7.8
        elif nome == 'Amido de Milho 200g':
            valor = 5.0
        elif nome == 'Creme de Leite 300g':
            valor = 3.9
        elif nome == 'Polvilho Doce 500g':
            valor = 6.0
        elif nome == 'Ervas Finas 30g':
            valor = 4.0
        elif nome == 'Café Solúvel 100g':
            valor = 9.5
        elif nome == 'Farinha de Mandioca 1kg':
            valor = 4.2
        elif nome == 'Condimentos Mix 50g':
            valor = 3.8
        elif nome == 'Leite Condensado 395g':
            valor = 6.9
        elif nome == 'Gelatina Incolor 12g':
            valor = 2.5
        elif nome == 'Massa de Tomate 300g':
            valor = 4.6
        unidade = 'un'
        quantidade = random.randint(1, 50)
    elif categoria == 'limpeza':
        codigo = random.randint(1, 1000)
        nome = random.choice([
                            "Detergente Líquido 500ml",
                            "Sabão em Pó 1kg",
                            "Água Sanitária 2L",
                            "Desinfetante Floral 1L",
                            "Esponja de Limpeza 3 unidades",
                            "Lustra-Móveis 200ml",
                            "Limpa Vidros 500ml",
                            "Sabão Líquido 1,5L",
                            "Cera Líquida 750ml",
                            "Álcool em Gel 70% 500ml",
                            "Multiuso 500ml",
                            "Vassoura de Palha 1 unidade",
                            "Rodo de Alumínio 1 unidade",
                            "Balde de Plástico 10L",
                            "Luvas de Borracha 1 par",
                            "Pano de Chão 2 unidades",
                            "Papel Toalha 2 rolos",
                            "Saponáceo Cremoso 300ml",
                            "Cloro Gel 1L",
                            "Refil Mop 1 unidade"
        ])
        if nome == 'Detergente Líquido 500ml':
            valor = 3.5
        elif nome == 'Sabão em Pó 1kg':
            valor = 7.8
        elif nome == 'Água Sanitária 2L':
            valor = 5.2
        elif nome == 'Desinfetante Floral 1L':
            valor = 6.3
        elif nome == 'Esponja de Limpeza 3 unidades':
            valor = 4.5
        elif nome == 'Lustra-Móveis 200ml':
            valor = 8.7
        elif nome == 'Limpa Vidros 500ml':
            valor = 6.0
        elif nome == 'Sabão Líquido 1,5L':
            valor = 12.5
        elif nome == 'Cera Líquida 750ml':
            valor = 10.0
        elif nome == 'Álcool em Gel 70% 500ml':
            valor = 9.8
        elif nome == 'Multiuso 500ml':
            valor = 5.5
        elif nome == 'Vassoura de Palha 1 unidade':
            valor = 15.0
        elif nome == 'Rodo de Alumínio 1 unidade':
            valor = 18.5
        elif nome == 'Balde de Plástico 10L':
            valor = 10.0
        elif nome == 'Luvas de Borracha 1 par':
            valor = 6.0
        elif nome == 'Pano de Chão 2 unidades':
            valor = 7.2
        elif nome == 'Papel Toalha 2 rolos':
            valor = 4.9
        elif nome == 'Saponáceo Cremoso 300ml':
            valor = 5.3
        elif nome == 'Cloro Gel 1L':
            valor = 7.5
        elif nome == 'Refil Mop 1 unidade':
            valor = 12.0
        unidade = 'un'
        quantidade = random.randint(1, 30)
    elif categoria == 'escritorio':
        codigo = random.randint(1, 500)
        nome = random.choice([
                                "Caneta Esferográfica Azul",
                                "Lápis Preto",
                                "Apontador",
                                "Borrachas Brancas",
                                "Caderno Universitário 10 matérias",
                                "Papel Sulfite A4",
                                "Clips para Papel",
                                "Pasta Arquivadora",
                                "Tesoura",
                                "Marcador de Texto Amarelo",
                                "Carimbo para Data",
                                "Papel adesivo",
                                "Fita Crepe",
                                "Fita dupla face",
                                "Envelope A4",
                                "Caderno Espiral 200 folhas",
                                "Papel cartão",
                                "Post-it",
                                "Calculadora Científica",
                                "Grampeador"
        ])
        if nome == 'Caneta Esferográfica Azul':
            valor = 1.5
        elif nome == 'Lápis Preto':
            valor = 0.8
        elif nome == 'Apontador':
            valor = 1.2
        elif nome == 'Borrachas Brancas':
            valor = 1.0
        elif nome == 'Caderno Universitário 10 matérias':
            valor = 25.0
        elif nome == 'Papel Sulfite A4':
            valor = 15.0
        elif nome == 'Clips para Papel':
            valor = 3.5
        elif nome == 'Pasta Arquivadora':
            valor = 10.0
        elif nome == 'Tesoura':
            valor = 6.0
        elif nome == 'Marcador de Texto Amarelo':
            valor = 3.2
        elif nome == 'Carimbo para Data':
            valor = 20.0
        elif nome == 'Papel adesivo':
            valor = 5.5
        elif nome == 'Fita Crepe':
            valor = 4.0
        elif nome == 'Fita dupla face':
            valor = 7.0
        elif nome == 'Envelope A4':
            valor = 2.5
        elif nome == 'Caderno Espiral 200 folhas':
            valor = 12.0
        elif nome == 'Papel cartão':
            valor = 8.0
        elif nome == 'Post-it':
            valor = 6.5
        elif nome == 'Calculadora Científica':
            valor = 50.0
        elif nome == 'Grampeador':
            valor = 18.0
        unidade = 'un'
        quantidade = random.randint(1, 20) 
    elif categoria == 'eletronico':
        codigo = random.randint(1, 500)
        nome = random.choice([
                                "Smartphone",
                                "Notebook",
                                "Tablet",
                                "Fones de Ouvido Bluetooth",
                                "Carregador Portátil",
                                "Câmera Digital",
                                "Smartwatch",
                                "TV LED",
                                "Impressora",
                                "Computador Desktop",
                                "Microfone Condensador",
                                "Projetor Multimídia",
                                "Teclado Mecânico",
                                "Mouse Óptico",
                                "Roteador Wi-Fi",
                                "Caixa de Som Bluetooth",
                                "Cabo HDMI",
                                "Webcam",
                                "Leitor de Cartões",
                                "Scanner"
        ])
        if nome == 'Smartphone':
            valor = 1200.0
        elif nome == 'Notebook':
            valor = 2500.0
        elif nome == 'Tablet':
            valor = 900.0
        elif nome == 'Fones de Ouvido Bluetooth':
            valor = 150.0
        elif nome == 'Carregador Portátil':
            valor = 80.0
        elif nome == 'Câmera Digital':
            valor = 1800.0
        elif nome == 'Smartwatch':
            valor = 700.0
        elif nome == 'TV LED':
            valor = 2200.0
        elif nome == 'Impressora':
            valor = 400.0
        elif nome == 'Computador Desktop':
            valor = 3000.0
        elif nome == 'Microfone Condensador':
            valor = 250.0
        elif nome == 'Projetor Multimídia':
            valor = 1200.0
        elif nome == 'Teclado Mecânico':
            valor = 350.0
        elif nome == 'Mouse Óptico':
            valor = 80.0
        elif nome == 'Roteador Wi-Fi':
            valor = 200.0
        elif nome == 'Caixa de Som Bluetooth':
            valor = 180.0
        elif nome == 'Cabo HDMI':
            valor = 40.0
        elif nome == 'Webcam':
            valor = 120.0
        elif nome == 'Leitor de Cartões':
            valor = 60.0
        elif nome == 'Scanner':
            valor = 600.0
        unidade = 'un'
        quantidade = random.randint(1, 20)
        
    produto_gerado = {'codigo': codigo,
                          'nome': nome,
                          'unidade': unidade,
                          'quantidade': quantidade,
                          'categoria': categoria,
                          'valor': valor,
                          'dataCadastro': dataCadastro
    }
    return produto_gerado

def grafico():
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_excel("produtos.xlsx")
    df ['dataCadastro'] = pd.to_datetime(df['dataCadastro'], dayfirst=True)
    df['Data'] = df['dataCadastro'].dt.to_period("M")
    df['valor_total'] = df['valor'] * df['quantidade']
    resultado = df.groupby("Data")['valor_total'].sum().reset_index()
    plt.figure(figsize=(17,7.5))
    bars = plt.bar(resultado['Data'].astype(str), resultado['valor_total'], color='skyblue', label='Valores', width=0.6)
    
    plt.title("Valores por Mês", fontsize=20, fontweight='bold', color='darkblue', pad=20)
    plt.xlabel("Mês", fontsize=14, fontweight='bold', color='darkgreen')
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

    for bar in bars:
        bar.set_edgecolor('black')
    plt.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.show()
