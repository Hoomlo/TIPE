from vecteurs import Vect
import random as rd

def generate_random_vect():
    vx = rd.randint(-500, 500)
    vy = rd.randint(-500, 500)
    
    return Vect (vx, vy)

def generate_list_of_position_for_a_point(n : int):
    # une position pour un point est représenter par un vecteur vitesse
    
    list_of_pos_point = [Vect(0,0) for i in range(n)]
    for i in range(n):
        v = generate_random_vect()
        list_of_pos_point[i] = v
    return list_of_pos_point

def generate_list_of_position_for_a_creature(n: int, list_points: list):
    # renvoie une matrice de taille nbpoint * n tel que la colonne i représente la position i de la creature
    
    m = len(list_points)
    list_of_pos = [[] for i in range(m)]
    
    for i in range(m):
        
        list_of_pos_point = generate_list_of_position_for_a_point(n)
        list_of_pos[i] = list_of_pos_point
        