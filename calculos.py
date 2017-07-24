def distanciaMedia (lista_valores):
    soma = sum(list(lista_valores))
    dist_media = soma/len(lista_valores)
    return dist_media

def distanciaResultante(AP, ML):
    distancia_result = []

    for i in range(len(AP)):
        DR = sqrt((AP[i]**2)+(ML[i]**2))
        distancia_result.append(DR)
    return distancia_result

def distanciaResultanteParcial(APouML):
    distancia_resultparcial = []

    for i in range(len(APouML)):
        distancia_resultparcial
        DR = sqrt(APouML[i]**2)
        distancia_resultparcial.append(DR)
    return distancia_resultparcial

def dist_RMS (dist_resultante):
    d_R_quadrada =[]
    for _ in range(len(dist_resultante)):
        dist_result_quadrada = (dist_resultante[_]**2)
        d_R_quadrada.append(dist_result_quadrada)
    soma = sum(list(d_R_quadrada))
    disRMS =sqrt(soma/len(dist_resultante))
    return disRMS

def geraAP_ML(valx, valy):
    soma_AP0 = soma_ML0 = 0.0
    valores_AP = []
    valores_ML = []

    for ele in range(len(valy)):
        soma_AP0 = soma_AP0 + valx[ele]
        soma_ML0 = soma_ML0 + valy[ele]

    AP_barra = soma_AP0 / len(valx)
    ML_barra = soma_ML0 / len(valy)

    for i in range(len(valy)):
        ap = valx[i] - AP_barra
        ml = valy[i] - ML_barra
        valores_AP.append(ap)
        valores_ML.append(ml)
    return valores_AP, valores_ML

from random import*
def geraNumeroAleatorio(x_Inicial, x_Final, y_Inicial, y_Final, N):
    valores_x =[]
    valores_y =[]
    for i in range(N):
        x = uniform(x_Inicial, x_Final)
        y = uniform(y_Inicial, y_Final)
        valores_x.append(x)
        valores_y.append(y)
    return valores_x, valores_y

def mVelo(totex, tempo):
    velocidademedia = totex/tempo
    return velocidademedia

from math import sqrt
def totex(AP, ML):
    dist = []
    for i in range(len(AP)-1):
        distancia = sqrt((AP[i+1] - AP[i])**2 + (ML[i+1] - ML[i])**2)
        dist.append(distancia)
    Totex = sum(list(dist))
    return Totex

def totexParcial(APouML):
    dist = []
    for i in range(len(APouML)-1):
        distancia = sqrt((APouML[i+1] - APouML[i])**2)
        dist.append(distancia)
    Totexparcial = sum(list(dist))
    return Totexparcial

def valorAbsoluto(minimo, maximo):
    if abs(minimo) > abs(maximo):
        return abs(minimo)
    else:
        return abs(maximo)
