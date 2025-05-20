from Structure_creature.points import Points
from Structure_creature.lien import Lien
from vecteurs import Vect


class Creature:
    
    def __init__(self) -> None:
        
        self.list_of_points = []
        self.list_of_link = []
        
    def update_list_of_points (self, list_of_points):
        
        self.list_of_points = [point for point in list_of_points]
    
    def update_list_of_link (self):
        n = len(self.list_of_points)
        
        for i in range(n - 1):
            self.list_of_link.append(Lien(self.list_of_points[i], self.list_of_points[i+1]))
            

    """ implementation de la première loi de newton """
    
    def cherche_indice_in_list_point(self, point):
        n = len(self.list_of_points)
        
        for i in range(n):
            if self.list_of_points[i] == point:
                return i
    
    
    def newton_sum_of_velocity_nul_on_link (self):
        
        sauv_velocity = [point.velocity for point in self.list_of_points] # sauvegarde des vitesse de chaque point
        
        n_list_point = len(self.list_of_points)
        
        # on parcours la liste des points pour crée la liste des liens tel que point appartient au lien
        for i in range(n_list_point - 1): 
            
            point = self.list_of_points[i]
            tab_lien_tq_point_C_lien = []
            
            for lien in self.list_of_link:
                
                if point == lien.A or point == lien.B:
                    tab_lien_tq_point_C_lien.append(lien)
            
            # disjonction de cas selon le nombre de lien aux quels appartient le point
            n_list_lien_de_point = len(tab_lien_tq_point_C_lien)
            
            if n_list_lien_de_point == 0: # si le lien n'appartient a aucun lien il n'y a rien a faire
                pass
            
            elif n_list_lien_de_point == 1: # si le lien appartient a un seul lien on soustrait la vitesse de l'autre point a sa vitesse
                
                if tab_lien_tq_point_C_lien[0].A == point:
                    other_point = tab_lien_tq_point_C_lien[0].B
                else:
                    other_point = tab_lien_tq_point_C_lien[0].A
                
                new_v = sauv_velocity[i] - sauv_velocity[self.cherche_indice_in_list_point(other_point)]
                point.velocity = Vect.convert_into_int(new_v)
            
            else: 
                """ si le lien appartient a plus d'un lien on soustrais
                n-1 (le nombre de lien aux quel appartient le point) fois la somme des vitesses des autres points
                à n fois la vitesse de point"""
                
                list_other_points = []
                
                
                for lien in tab_lien_tq_point_C_lien:
                    
                    if point != lien.A:
                        list_other_points.append(lien.A)
                    else:
                        list_other_points.append(lien.B)   
                
                sum_of_velocity = Vect(0,0)
                
                
                for other_point in list_other_points:

                    sum_of_velocity += sauv_velocity[self.cherche_indice_in_list_point(other_point)]
                
                
                new_v = ((n_list_lien_de_point - 1)*n_list_lien_de_point)/2 * sauv_velocity[i] - (n_list_lien_de_point - 1) * sum_of_velocity
                point.velocity = Vect.convert_into_int(new_v)
               
        """v = [s.velocity for s in self.list_of_points]
        print("\n init vel ")
        print(v)"""
                
                
                
                
                    
