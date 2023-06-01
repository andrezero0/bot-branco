from telethon import TelegramClient, sync, events
from time import sleep
import requests

api_id = 3910389
api_hash = '86f861352f0ab76a251866059a6adbd6'

sessao_branco = '+5584988647903'

def obter_chats():
    client = TelegramClient(sessao_branco, api_id, api_hash)
    client.start()
    dialogs = client.get_dialogs()
    for dialogs in dialogs:
        if dialogs.id < 0:
            print('----------------------------------------')
            print(f'Grupo: {dialogs.title}')
            print(f'Id: {dialogs.id}')


    client.disconnect()

#obter_chats()
uid_branco = 0


def bot_branco():
    print('Procuarndo Mensagens Branco!')
    c_branco = TelegramClient(sessao_branco, api_id, api_hash)
    @c_branco.on(events.NewMessage(chats= [1001939756983]))
    async def enviar_msg(event):
        msg = str(event.raw_text)

        if 'POSSÍVEL BRANCO⚠️⚪️' in msg:
            msg = str(msg.replace('POSSÍVEL BRANCO', '''BOSS BRANCO
POSSÍVEL BRANCO'''))
            msg = str(msg.replace('BOSS', '[BOSS](http://t.me/boss_vips_bot)'))
            msg = str(msg.replace('⚠️⚪️', ' ⚪️🧨'))
            msg = str(msg.replace('á', 'a', 1))
            msg = str(msg.replace('⏱ Horarios das Probabilidade:', 'HORARIO DAS PROBABILIDADE: ⏱️'))
            msg = str(msg.replace('LISTA BRANCA:', '''LISTA DOS BRANCA:
'''))
            msg = str(msg.replace('🎰 Entre no jogo aqui', '''
[🎰 Blaze.com](blaze.com/r/azpoL)'''))


            global uid_branco
            uid_msg1 = await c_branco.send_message(-1001609756520, msg)
            uid_branco = uid_msg1.id
            msg = ''

        elif 'Não veio 👎' in msg:
            msg = str(msg.replace('''Não veio 👎
Vamos Buscar no Próximo Sinal 😉''', 'AGUARDA A PRÓXIMA ✖️✖️'))
            await c_branco.send_message(-1001609756520,  msg, reply_to= uid_branco)
            uid_branco = 0
            msg = ''
        
        elif 'WIN BRANCO -' in msg:
            await c_branco.send_message(-1001609756520,  msg, reply_to= uid_branco)
            msg = ''
        
        elif '👌 Resultado até agora' in msg:
            msg = str(msg.replace('👌 Resultado até agora', 'PARCIAL DO DIA'))
            await c_branco.send_message(-1001609756520,  msg, reply_to= uid_branco)
            msg = ''
    

            
    c_branco.start()
    c_branco.run_until_disconnected()




bot_branco()
