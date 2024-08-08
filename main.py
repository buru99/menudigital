import flet as ft
import urllib.parse

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.padding = 10
    page.theme_mode = ft.ThemeMode.LIGHT

    # Lista de pedidos do cliente
    pedidos_cliente = []

    # Atualiza a lista de pedidos e calcula o total
    def atualizar_pedidos():
        page.clean()
        page.add(ft.Text("Seus Pedidos", style=ft.TextStyle(weight='bold', size=25)))

        total = 0
        for pedido in pedidos_cliente:
            total += pedido['quantidade'] * pedido['preco']
            page.add(ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                ft.Column(controls=[ft.Text(f"{pedido['nome']} - R${pedido['preco']} x {pedido['quantidade']}")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.IconButton(icon=ft.icons.REMOVE, on_click=lambda e, p=pedido: atualizar_quantidade(p, -1)),
                ft.IconButton(icon=ft.icons.ADD, on_click=lambda e, p=pedido: atualizar_quantidade(p, 1))
            ])))
        
        page.add(ft.Text(f"Total: R${total:.2f}", style=ft.TextStyle(weight='bold', size=20)))
        page.add(ft.Text("Taxa de entrega R$5,00"))
        page.add(ft.BottomAppBar(
            bgcolor=ft.colors.TRANSPARENT,
            height=60,
            width=300,
            content=ft.Row(controls=[
                ft.TextButton(text="Finalizar Pedido", width=150, on_click=finalizar_pedido),
                ft.TextButton(text="Página Inicial", width=150, on_click=menu_inicial)
            ])
        ))
        page.update()

    # Atualiza a quantidade de itens no pedido
    def atualizar_quantidade(pedido, quantidade):
        pedido['quantidade'] += quantidade
        if pedido['quantidade'] <= 0:
            pedidos_cliente.remove(pedido)
        atualizar_pedidos()

    # Adiciona um item ao pedido
    def adicionar_pedido(nome, preco):
        for pedido in pedidos_cliente:
            if pedido['nome'] == nome:
                pedido['quantidade'] += 1
                break
        else:
            pedidos_cliente.append({'nome': nome, 'preco': preco, 'quantidade': 1})
        atualizar_pedidos()

    # Coleta dados do cliente e envia o pedido por WhatsApp
    def finalizar_pedido(e):
        def enviar_whatsapp(e):
            nome = input_nome.value
            bairro = input_bairro.value
            rua = input_rua.value
            num = input_numero.value
            ref = input_ref.value
            telefone = input_telefone.value
            troco = input_troco.value

            resumo_pedido = "Resumo do Pedido:\n"
            total = 0
            for pedido in pedidos_cliente:
                resumo_pedido += f"{pedido['nome']} - {pedido['quantidade']}x R${pedido['preco']} = R${pedido['quantidade'] * pedido['preco']:.2f}\n"
                total += pedido['quantidade'] * pedido['preco']
            resumo_pedido += f"\n*Total: R${total + 5:.2f}*"
            linhas = '-'*60
            mensagem = f"*Olá, aqui está o resumo do seu pedido*\n\n*Nome:* {nome}\n\n*Endereço:*\nRua {rua} Bairro {bairro}, Número {num}\n*Ponto de Referência:* {ref}\n\n*Telefone:* {telefone}\n\n{linhas}\n\n{resumo_pedido}\nTroco Para: {troco}"
            mensagem_encoded = urllib.parse.quote(mensagem)
            numero_whatsapp = "5588997349933"  # Substitua pelo número de WhatsApp desejado
            url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem_encoded}"
            
            page.clean()
            page.add(ft.Text("Pedido enviado com sucesso!", style=ft.TextStyle(weight='bold', size=25)))
            page.add(ft.TextButton(text="Abrir WhatsApp", url=url_whatsapp))
            page.add(ft.BottomAppBar(
                bgcolor=ft.colors.TRANSPARENT,
                height=60,
                width=300,
                content=ft.TextButton(text="Página Inicial", width=300, on_click=menu_inicial)
            ))
            page.update()

        page.clean()
        page.add(ft.Text("Finalize seu pedido", style=ft.TextStyle(weight='bold', size=25)))
        input_nome = ft.TextField(label="Nome", width=300)
        input_bairro = ft.TextField(label="Bairro", width=300)
        input_rua = ft.TextField(label="Rua", width=300)
        input_numero = ft.TextField(label="Número", width=300)
        input_ref = ft.TextField(label="Ponto de Referência", width=300)
        input_telefone = ft.TextField(label="Telefone", width=300)
        input_troco = ft.TextField(width=300,label="Precisa de troco? Se sim digite o valor")
        page.add(input_nome,input_bairro, input_rua, input_numero, input_ref, input_telefone, input_troco)
        page.add(ft.ElevatedButton(text="Enviar Pedido", on_click=enviar_whatsapp))
        page.add(ft.BottomAppBar(
            bgcolor=ft.colors.TRANSPARENT,
            height=60,
            width=300,
            content=ft.TextButton(text="Página Inicial", width=300, on_click=menu_inicial)
        ))
        page.update()

    # Ver lista de pedidos
    def pedidos(e):
        atualizar_pedidos()

    # Volta para o menu Inicial
    def menu_inicial(e):
        page.clean()
        page.add(capa, categorias, lista_pedidos)
        page.scroll = False
        page.update()

    # AQUI ABRE A LISTA DE CADA CATEGORIA DE PEDIDOS
    def Pizzas(e):
        page.clean()
        page.update()
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.padding = 10

        page.add(ft.Text("Confira nosso menu de pizzas", style=ft.TextStyle(weight='bold', size=25)))
        
        # LISTA DE SABORES
        pizzas = [
            {"nome": "Calabresa 8 fatias", "preco": 25.00, "imagem": "https://prezunic.vtexassets.com/arquivos/ids/179719-800-auto?v=638368810383670000&width=800&height=auto&aspect=true"},
            {"nome": "Mussarela 8 fatias", "preco": 25.00, "imagem": "https://bretas.vtexassets.com/arquivos/ids/187352/6571c1dd558925a4e8898c47.jpg?v=638375508167430000"},
            {"nome": "Portuguesa 8 fatias", "preco": 25.00, "imagem": "https://mercantilatacado.vtexassets.com/arquivos/ids/184481-800-auto?v=638350433052930000&width=800&height=auto&aspect=true"},
            {"nome": "Bacon 8 fatias", "preco": 25.00, "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR96_z2MgVvX_3LvbUiMy0Zoj30uMDc6A1Vw&s"},
            {"nome": "Frango Catupiry 8 fatias", "preco": 25.00, "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTft26lzsaiqBJqchXWifPQt6xCYCcvcNYEqrAimd-GgodQBjATSul2xKJERUizum3i-_I&usqp=CAU"},
            {"nome": "4 Queijos 8 fatias", "preco": 25.00, "imagem": "https://mercantilatacado.vtexassets.com/arquivos/ids/184328-800-auto?v=638350432632370000&width=800&height=auto&aspect=true"}
        ]

        # Cria a ListView rolável para as pizzas
        pizza_list = ft.ListView(expand=1, spacing=20, padding=10, auto_scroll=True)

        for pizza in pizzas:
            pizza_list.controls.append(
                ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                    ft.Column(controls=[ft.Text(f"{pizza['nome']}\nR${pizza['preco']:.2f}")], alignment=ft.MainAxisAlignment.START, expand=True),
                    ft.Row(controls=[ft.Image(src=pizza["imagem"], fit=ft.ImageFit.COVER)]),
                    ft.IconButton(icon=ft.icons.ADD, on_click=lambda e, p=pizza: adicionar_pedido(p['nome'], p['preco']))
                ]))
            )

        page.add(pizza_list)

        page.add(ft.BottomAppBar(
            bgcolor=ft.colors.TRANSPARENT,
            height=60,
            width=300,
            content=ft.TextButton(text="Página Inicial", width=300, on_click=menu_inicial)
        ))
        
        page.update()

    # Placeholder functions for other categories
    def placeholder(e):
        page.clean()
        page.add(ft.Text("Em breve!"))
        page.update()

    # CAPA DA PÁGINA
    capa = ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQF2_H0tdFgRjIgWt0uDMevE8HyF4dZ4LBpA&s")

    # LISTA DE CATEGORIAS DE PEDIDOS
    categorias = ft.ListView(
        controls=[
            ft.FloatingActionButton(text="Pizzas", width=600, bgcolor=ft.colors.ORANGE_ACCENT, on_click=Pizzas),
            ft.FloatingActionButton(text="Hamburguers", width=600, bgcolor=ft.colors.ORANGE_ACCENT, on_click=Pizzas),
            ft.FloatingActionButton(text="Combos", width=600, bgcolor=ft.colors.ORANGE_ACCENT, on_click=placeholder),
            ft.FloatingActionButton(text="Carnes", width=600, bgcolor=ft.colors.ORANGE_ACCENT, on_click=placeholder),
            ft.FloatingActionButton(text="Bebidas", width=600, bgcolor=ft.colors.ORANGE_ACCENT, on_click=placeholder),
        ],
        expand=1, spacing=20, padding=20, auto_scroll=True
    )

    # Lista de pedidos do cliente
    lista_pedidos = ft.BottomAppBar(
        bgcolor=ft.colors.TRANSPARENT,
        height=60,
        width=300,
        content=ft.TextButton(text="Ver Pedidos", icon=ft.icons.SHOPPING_CART, on_click=pedidos)
    )

    page.add(capa, categorias, lista_pedidos)
    page.update()

ft.app(main)
