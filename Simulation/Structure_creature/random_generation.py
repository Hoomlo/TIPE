import random as rd
from Structure_creature.points import Points
from Structure_creature.lien import Lien
from vecteurs import Vect
import UnirTrouver as unirtrouver

def genereate_random_list_of_point():
    
    nb_point = rd.randint(2, 10)
    list_of_point = [Vect(0,0) for i in range(nb_point)]
    
    for i in range(nb_point):
        x = rd.randint(0, 1000)
        y = rd.randint(0, 1000)

        list_of_point[i] = Points(Vect(x,y), Vect(0,0))
    return list_of_point

def generate_random_list_of_link(list_of_point):
    
    nb_point = len(list_of_point)
    nb_liens = nb_point - 1
    list_of_link = [Points(Vect(0,0), Vect(0,0)) for i in range(nb_liens)]
    structure = unirtrouver.init(nb_point)
    
    for i in range(nb_liens):
        
        b = False
        while not b:
            x = rd.randint(0, nb_point-1)
            y = rd.rendint(0, nb_point-1)

            b = unirtrouver.unir(structure, x, y)
        
        list_of_link[i] = Lien(list_of_point[x], list_of_point[y])
    
    return list_of_link

