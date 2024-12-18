#Perguntar da onde pra onde (mm, cm e m) e aí fazer as devidas conversões
#Pedir qual unidade, pedir valor, pedir outra unidade, pedir valor, converter
UN1 = input('Qual a unidade de medida do primeiro valor(Use m, cm ou mm)? ')
V = float(input('Qual o valor inicial?' ))
UN2 = input('Qual a unidade de medida para a conversão(Use m, cm ou mm)? ')
mpcm = V*100
mpmm = V*1000
cmpm = V/100
cmpmm = V*10
mmpcm = V/10
mmpm = V/1000
if(UN1+'p'+UN2 == 'mpcm'):
    print('O resultado é {} cm'.format(mpcm))
if(UN1+'p'+UN2 == 'mpmm'):
    print('O resultado é {} mm'.format(mpmm))
if(UN1+'p'+UN2 == 'cmpmm'):
    print('O resultado é {} mm'.format(cmpmm))
if(UN1+'p'+UN2 == 'cmpm'):
    print('O resultado é {} m'.format(cmpm))
if(UN1+'p'+UN2 == 'mmpcm'):
    print('O resultado é {} cm'.format(mmpcm))
if(UN1+'p'+UN2 == 'mmpm'):
    print('O resultado é {} m'.format(mmpm))