import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.padding = 10
    page.theme_mode = ft.ThemeMode.LIGHT

    # Ver lista de pedidos
    def pedidos(e):
        page.clean()
        page.update()
        page.add(ft.BottomAppBar(
            bgcolor=ft.colors.TRANSPARENT,
            height=60,
            width=300,
            content=ft.TextButton(text="Página Inicial", width=300, on_click=menu_inicial)
        ))
        page.update()

     # Volta para o menu Inicial
    def menu_inicial(e):
        page.clean()
        page.update()
        page.add(capa, categorias, lista_pedidos)
        page.scroll = False
        page.update()

    #AQUI ABRE A LISTA DE CADA CATEGORIA DE PEDIDOS
    def Pizzas(e):
        page.clean()
        page.update()
        page.horizontal_alignment='center'
        page.vertical_alignment='center'
        page.padding=10

        page.add(ft.Text("Confira nosso menu de pizzas", style=ft.TextStyle(weight='bold', size=25)))
        
        #LISTA DE SABORES
        page.add(ft.ListView(controls=[
            ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START,controls=[
                ft.Column(controls=[ft.Text("Calabresa 8 fatias\nR$25,00")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.Row(controls=[ft.Image(src="https://prezunic.vtexassets.com/arquivos/ids/179719-800-auto?v=638368810383670000&width=800&height=auto&aspect=true", fit=ft.ImageFit.COVER)]),
                ft.IconButton(icon=ft.icons.ADD)
                ])),

            ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START,controls=[
                ft.Column(controls=[ft.Text("Mussarela 8 fatias\nR$25,00")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.Row(controls=[ft.Image(src="https://bretas.vtexassets.com/arquivos/ids/187352/6571c1dd558925a4e8898c47.jpg?v=638375508167430000", fit=ft.ImageFit.COVER)]),
                ft.IconButton(icon=ft.icons.ADD)
                ])),
            
            ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START,controls=[
                ft.Column(controls=[ft.Text("Portuguesa 8 fatias\nR$25,00")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.Row(controls=[ft.Image(src="https://mercantilatacado.vtexassets.com/arquivos/ids/184481-800-auto?v=638350433052930000&width=800&height=auto&aspect=true", fit=ft.ImageFit.COVER)]),
                ft.IconButton(icon=ft.icons.ADD)
                ])),
            
            ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START,controls=[
                ft.Column(controls=[ft.Text("Bacon 8 fatias\nR$25,00")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.Row(controls=[ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR96_z2MgVvX_3LvbUiMy0Zoj30uMDc6A1Vw&s", fit=ft.ImageFit.COVER)]),
                ft.IconButton(icon=ft.icons.ADD)
                ])),
            
            ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START,controls=[
                ft.Column(controls=[ft.Text("Frango Catupiry 8 fatias\nR$25,00")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.Row(controls=[ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTft26lzsaiqBJqchXWifPQt6xCYCcvcNYEqrAimd-GgodQBjATSul2xKJERUizum3i-_I&usqp=CAU", fit=ft.ImageFit.COVER)]),
                ft.IconButton(icon=ft.icons.ADD)
                ])),
            
            ft.Container(width=300, height=100, content=ft.Row(alignment=ft.MainAxisAlignment.START,controls=[
                ft.Column(controls=[ft.Text("4 Queijos 8 fatias\nR$25,00")], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.Row(controls=[ft.Image(src="https://mercantilatacado.vtexassets.com/arquivos/ids/184328-800-auto?v=638350432632370000&width=800&height=auto&aspect=true", fit=ft.ImageFit.COVER)]),
                ft.IconButton(icon=ft.icons.ADD)
                ])),
            
            
        
        ], expand=1, spacing=20,  auto_scroll=True))

        

        page.add(ft.BottomAppBar(
            bgcolor=ft.colors.TRANSPARENT,
            height=60,
            width=300,
            content=ft.TextButton(text="Página Inicial", width=300, on_click=menu_inicial)
        ))
        
        page.update()


    #CAPA DA PÁGINA
    capa = ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQF2_H0tdFgRjIgWt0uDMevE8HyF4dZ4LBpA&s")

    #LISTA DE CATEGORIAS DE PEDIDOS
    categorias = ft.ListView(
        controls=[
            ft.FloatingActionButton(text="Pizzas", width=600, bgcolor=ft.colors.ORANGE_ACCENT, on_click=Pizzas),
            ft.FloatingActionButton(text="Hamburguers", width=600, bgcolor=ft.colors.ORANGE_ACCENT),
            ft.FloatingActionButton(text="Combos", width=600, bgcolor=ft.colors.ORANGE_ACCENT),
            ft.FloatingActionButton(text="Carnes", width=600, bgcolor=ft.colors.ORANGE_ACCENT),
            ft.FloatingActionButton(text="Bebidas", width=600, bgcolor=ft.colors.ORANGE_ACCENT), 
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
ft.app(main)

