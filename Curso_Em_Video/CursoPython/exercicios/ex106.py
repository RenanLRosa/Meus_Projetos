while True:
    comando = input('Digite uma comando(FIM para encerrar): ')
    if comando.upper() == 'FIM':
        break
    help(comando)

