def lampada ():
    return 'Luz acesa'
def ar_condicionado(temperatura):
    return f'Temperatura ajustada para {temperatura} graus'
def tocar_musica (musica):
    return f'Tocando a música {musica}'
comandos = {1:lampada,2:ar_condicionado,3:tocar_musica}
def processar(i,parametro=None):
    if parametro is not None:
        return comandos[i](parametro) 
    else: 
        return comandos [i]()
print(processar(1))
print(processar(2,20))
print(processar(3,'Despacito'))
