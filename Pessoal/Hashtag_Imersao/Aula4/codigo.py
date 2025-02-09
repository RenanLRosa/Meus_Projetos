
#importar flet
import flet as ft

#Criar uma função principal para rodar o app

def main(pagina):

    #titulo
    titulo = ft.Text('LittleZap')
    pagina.add(titulo)

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    chat = ft.Column()

    def enviar_mensagem(evento):
        nome_usuario = campo_nome.value
        mensagem = (f'{nome_usuario}: {campo_enviar_mensagem.value}')
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ''
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    def entrar_no_chat(evento):
        popup.open = False #Fecha poput
        pagina.remove(titulo) #Remove o titulo
        pagina.remove(botao) #Remove o botão
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = campo_nome.value
        mensagem = (f'{nome_usuario} entrou no chat.')
        pagina.pubsub.send_all(mensagem)
        pagina.update()
    #Criar popup
    titulo_popup = ft.Text('Bem-vindo ao LittleChat')
    campo_nome = ft.TextField(label='Digite seu nome')
    botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=entrar_no_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=campo_nome, actions=[botao_popup])

    #botão inicial
    def abrir_popup(evento):
        pagina.overlay.append(popup)
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    pagina.add(botao)
    
#Executar essa função no flet
app = ft.app(main, view=ft.WEB_BROWSER)