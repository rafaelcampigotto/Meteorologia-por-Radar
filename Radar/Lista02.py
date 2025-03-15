#Lista 02 - Meteorologia por Radar
#Rafael Lima Campigotto / NUSP: 13641991

import math
import numpy as np

#Criando uma função

def coordenadas(lat_radar, lon_radar, lat_local, lon_local, Res):

    """
    Calcula a distância, o azimute e o número de gates de um ponto em relação a um radar

    Args:
        lat_radar (float): latitude do radar
        lon_radar (float): longitude do radar
        lat_local (float): latitude do ponto de interesse
        lon_local (float): longitude do ponto de interesse
        Res (int): resolução gate

    Returns:
        tuple: (Distancia, Azimute, NGate)
            -Distancia (float): Distância em quilômetros
            -Azimute (float): Ângulo azimutal em graus
            -NGates (int): Número de gates
    """

    #Calculando a variação em X e Y (em km)
    X= (lon_local-lon_radar)*111.195
    Y= (lat_local-lat_radar)*111.195

    #Calculando a distância (em km)
    Distancia= (X**2 + Y**2)**0.5

    #Calculando os ângulos
    ang=math.atan2(Y,X) #Ângulo em radianos, utilizando o ATAN2
    ang_cart=ang*180/np.pi #Ângulo cartesiano, em graus

    #Definição do quadrante e consequente definição do azimute
    if X>0 and Y>0:
        quadrante=1
    elif X>0 and Y<0:
        quadrante=2
    elif X<0 and Y<0:
        quadrante=3
    elif X<0 and Y>0:
        quadrante=4
    
    if quadrante !=4:
        Azimute=90-ang_cart
    else:
        Azimute=450-ang_cart

    #Cálculo do número de gates
    NGate= round(Distancia*1000/Res)
    
    return Distancia, Azimute, NGate

#Aplicando a função para os locais de interesse

#Minha casa (lat=-23.669289, lon=-46.664158)

#Minha casa e Butantã-USP
Dist, Az, Gate= coordenadas(-23.561722,-46.735111, -23.669289, -46.664158, 90)
print(f"Minha casa até o radar do Butantã-USP:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Minha casa e Radar Salesópolis
Dist, Az, Gate= coordenadas(-23.60, -45.9722, -23.669289, -46.664158, 125)
print(f"Minha casa até o Radar Salesópolis:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Minha casa e Radar Parque Cientec
Dist, Az, Gate= coordenadas(-23.6519, -46.6231, -23.669289, -46.664158, 75)
print(f"Minha casa até o Radar Parque Cientec:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Minha casa até o Radar São Roque
Dist, Az, Gate= coordenadas(-23.5166, -47.1166, -23.669289, -46.664158, 750)
print(f"Minha casa até o Radar São Roque:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Estação meteorológica do IAG (lat=-23.65, lon= -46.6167)

#Estação meteorológica do IAG até o Radar do Butantã
Dist, Az, Gate= coordenadas(-23.561722,-46.735111, -23.65, -46.6167, 90)
print(f"Estação IAG até o radar do Butantã-USP:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Estação meteorológica do IAG até o Radar do Salesópolis
Dist, Az, Gate= coordenadas(-23.60,-45.9722, -23.65, -46.6167, 125)
print(f"Estação IAG até o radar Salesópolis:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Estação meteorológica do IAG até o Radar do Parque Cientec
Dist, Az, Gate= coordenadas(-23.6519,-46.6231, -23.65, -46.6167, 75)
print(f"Estação IAG até o radar do Parque Cientec:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Estação meteorológica do IAG até o Radar São Roque
Dist, Az, Gate= coordenadas(-23.5166,-47.1166, -23.65, -46.6167, 750)
print(f"Estação IAG até o radar São Roque:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Prédio principal do IAG ( lat= -23.5596, lon= -46.73388)

#Prédio principal IAG até o radar do BUtantã
Dist, Az, Gate= coordenadas(-23.561722,-46.735111, -23.5596, -46.73388, 90)
print(f"Prédio Principal do IAG até o radar do Butantã-USP:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Prédio principal do IAG até o radar Salesópolis
Dist, Az, Gate= coordenadas(-23.60,-45.9722, -23.5596, -46.73388, 125)
print(f"Prédio Principal do IAG até o radar Salesópolis:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Prédio principal do IAG até o radar Parque Cientec
Dist, Az, Gate= coordenadas(-23.6519,-46.6231, -23.5596, -46.73388, 75)
print(f"Prédio Principal do IAG até o radar do Parque Cientec:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")

#Prédio principal do IAG até o radar São Roque
Dist, Az, Gate= coordenadas(-23.5166,-47.1166, -23.5596, -46.73388, 750)
print(f"Prédio Principal do IAG até o radar São Roque:\n Distância: {Dist}\n Azimute: {Az}\n Número de Gates: {Gate}\n")






    