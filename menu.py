import flet as ft
import mysql.connector
from time import sleep

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
            content=ft.ElevatedButton(text="Página Inicial", width=300, on_click=menu_inicial)
        ))
        page.update()

    # Volta para o menu Inicial
    def menu_inicial(e):
        page.clean()
        page.update()
        page.add(capa, ct1, categorias, lista_pedidos)
        page.scroll = False
        page.update()

    # Redireciona para a tela de cadastro
    def tela_cadastrar(e):
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.scroll = True
        page.clean()
        page.update()
        page.add(ft.Container(content=ft.IconButton(ft.icons.ARROW_BACK, on_click=tela_login), alignment=ft.alignment.top_left))
        page.add(ft.Container(bgcolor=ft.colors.WHITE10, content=ft.Column(
            controls=[ft.Text("Cadastre-se", style=ft.TextStyle(color='black', weight='bold', size=30)), email, nome, bairro, rua, numero_casa, ref, senha, cad_button], 
            alignment='center', 
            horizontal_alignment='center'
        ), padding=5))
        page.update()

    # Cadastra o cliente no banco de dados
    def cadastrar_cliente(e):
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='menu_digital'
        )
        cursor = conexao.cursor()
        
        # Verificar se email já é cadastrado
        verificar_email = 'SELECT * FROM clientes WHERE email = %s'
        cursor.execute(verificar_email, (email.value,))
        resultado = cursor.fetchone()

        if resultado:
            # Email já cadastrado
            page.snack_bar = ft.SnackBar(ft.Text("E-mail já cadastrado"), open=True)
        else:
            # Inserir novo cliente
            comando = 'INSERT INTO clientes (email, nome, bairro, rua, numero, ponto_ref, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            valores = (email.value, nome.value, bairro.value, rua.value, numero_casa.value, ref.value, senha.value)
            cursor.execute(comando, valores)
            conexao.commit()

            page.snack_bar = ft.SnackBar(ft.Text("Cliente cadastrado com sucesso"), open=True)
        
        page.update()
        cursor.close()
        conexao.close()

    # Redireciona para a tela de login        
    def tela_login(e):
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.padding = 5
        page.clean()
        page.update()
        page.add(ft.Container(content=ft.IconButton(ft.icons.ARROW_BACK, on_click=menu_inicial), alignment=ft.alignment.top_left),
                ft.Container(border_radius=10, width=500, height=500 ,bgcolor=ft.colors.WHITE10,content=ft.Column(controls=[
                    ft.Text("Login", size=30, style=ft.TextStyle(color='black', weight='bold')),
                    email_login,
                    senha_login,
                    ft.Row(controls=[
                        ft.TextButton(text="Cadastre-se", style=ft.ButtonStyle(color='black'), on_click=tela_cadastrar),
                        ft.TextButton(text="Esqueci minha senha", style=ft.ButtonStyle(color='black'), on_click=tela_recu_senha)
                        ], vertical_alignment='center', alignment='center'),
                        ft.ElevatedButton(text="Entrar", width=300, on_click=login),
            ], alignment='center', horizontal_alignment='center'), padding=5)
        )
        page.update()
    
    # Variável global para armazenar dados do cliente logado
    global cliente_logado
    cliente_logado = None
    
    # LOGIN DO USUÁRIO
    def login(e):
        global cliente_logado
        
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='menu_digital'
        )
        cursor = conexao.cursor()

        # Verifica se o email e senha estão corretos
        verificar_email = 'SELECT * FROM clientes WHERE email = %s AND senha = %s'
        cursor.execute(verificar_email, (email_login.value, senha_login.value))
        resultado = cursor.fetchone()

        if resultado:
            # Email e senha corretos
            cliente_logado = {
                'email': resultado[1],
                'nome': resultado[2],
                'bairro': resultado[3],
                'rua': resultado[4],
                'numero': resultado[5],
                'ponto_ref': resultado[6]
            }

            page.snack_bar = ft.SnackBar(ft.Text("Login Bem-sucedido!"), open=True)
            page.update()

            # Saudação ao usuário
            page.clean()
            page.add(ft.Text(f"Olá, {resultado[2]}! Seja bem-vindo ao nosso menu digital.", size=40, style=ft.TextStyle(color='black', weight='bold')))
            page.update()
            sleep(5)
            menu_inicial(e)

        else:
            # Email ou senha incorretos
            page.snack_bar = ft.SnackBar(ft.Text("E-mail ou senha incorretos"), open=True)
        
        page.update()
        cursor.close()
        conexao.close()

    # TELA DE RECUPERAR SENHA
    def tela_recu_senha(e):
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.padding = 5
        page.clean()
        page.update()
        page.add(ft.Container(bgcolor=ft.colors.WHITE10, content=ft.Column(
            controls=[ft.Text("Recupere sua senha", size=30, style=ft.TextStyle(color='black', weight='bold')), 
                      recuperar_email, 
                      nova_senha,
                      ft.ElevatedButton(text="Salvar senha", width=300, on_click=recuperar_senha)
            ]
        )))

    # RECUPERAR SENHA DO CLIENTE
    def recuperar_senha(e):
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='menu_digital'
        )
        cursor = conexao.cursor()
        
        verificar_email = 'SELECT * FROM clientes WHERE email = %s'
        cursor.execute(verificar_email, (recuperar_email.value,))
        resultado = cursor.fetchone()

        if resultado:
            atualizar_senha = 'UPDATE clientes SET senha = %s WHERE email = %s'
            cursor.execute(atualizar_senha, (nova_senha.value, recuperar_email.value))
            conexao.commit()
        
            page.snack_bar = ft.SnackBar(ft.Text("Senha atualizada com sucesso"), open=True)
            page.update()
            tela_login(e)
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("E-mail não encontrado"), open=True)
        
        page.update()

    # Mostrar perfil do cliente logado
    def mostrar_perfil(e):
        if cliente_logado:
            page.clean()
            page.add(ft.Container(content=ft.IconButton(ft.icons.ARROW_BACK, on_click=menu_inicial), alignment=ft.alignment.top_left))
            page.add(ft.Container(bgcolor=ft.colors.WHITE10, content=ft.Column(
                controls=[
                    ft.Text(f"Perfil de {cliente_logado['nome']}", size=30, style=ft.TextStyle(color='black', weight='bold')),
                    ft.Text(f"E-mail: {cliente_logado['email']}", size=20, style=ft.TextStyle(color='black')),
                    ft.Text(f"Bairro: {cliente_logado['bairro']}", size=20, style=ft.TextStyle(color='black')),
                    ft.Text(f"Rua: {cliente_logado['rua']}", size=20, style=ft.TextStyle(color='black')),
                    ft.Text(f"Número: {cliente_logado['numero']}", size=20, style=ft.TextStyle(color='black')),
                    ft.Text(f"Ponto de Referência: {cliente_logado['ponto_ref']}", size=20, style=ft.TextStyle(color='black')),
                ], alignment='center', horizontal_alignment='center'
            ), padding=5))
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Nenhum cliente logado"), open=True)
            page.update()

    # Variáveis
    capa = ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQF2_H0tdFgRjIgWt0uDMevE8HyF4dZ4LBpA&s")
    login_button = ft.TextButton(text="Faça seu Login", on_click=tela_login)
    perfil = ft.TextButton(text="Ver Perfil", on_click=mostrar_perfil)

    email = ft.TextField(hint_text="E-mail", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    nome = ft.TextField(hint_text="Nome", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    bairro = ft.TextField(hint_text="Bairro", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    rua = ft.TextField(hint_text="Rua", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    numero_casa = ft.TextField(hint_text="Número da residência", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    ref = ft.TextField(hint_text="Ponto de referência", max_length=50, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    senha = ft.TextField(hint_text="Senha", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black', can_reveal_password=True, password=True)
    email_login = ft.TextField(hint_text="E-mail", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    senha_login = ft.TextField(hint_text="Senha", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black', can_reveal_password=True, password=True)
    cad_button = ft.ElevatedButton(text="Cadastrar", width=300, on_click=cadastrar_cliente)

    # Variáveis da tela de recuperar senha
    recuperar_email = ft.TextField(hint_text="E-mail", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black')
    nova_senha = ft.TextField(hint_text="Digite uma nova senha", max_length=30, width=300, hint_style=ft.TextStyle(color='black'), color='black', focused_border_color='black', cursor_color='black', can_reveal_password=True, password=True)
    
    # Container com informações do cliente
    ct1 = ft.Container(
        bgcolor=ft.colors.WHITE10,
        height=35,
        content=ft.Row(controls=[login_button, perfil], alignment=ft.MainAxisAlignment.CENTER),
        border_radius=5
    )

    # Categoria de vendas do estabelecimento
    categorias = ft.ListView(
        controls=[
            ft.FloatingActionButton(text="Pizzas", width=600, bgcolor=ft.colors.ORANGE_ACCENT),
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
        content=ft.ElevatedButton(text="Ver Pedidos", icon=ft.icons.STORAGE_SHARP, width=300, on_click=pedidos)
    )

    page.add(capa, ct1, categorias, lista_pedidos)

ft.app(main)
