import arcade

def drawing(creature):
        
    # list of coordinates of each simulation point
        
    list_of_coords_points = [ (point.pos.x, point.pos.y) for point in creature.list_of_points ]
    point_diam = creature.list_of_points[0].diam
        
        
    # list of coordinates of each link in the simulation
        
    list_of_coords_liens = []   
    lien_thickness = creature.list_of_link[0].thickness
        
    for i in range(len(creature.list_of_link)):
            
        list_of_coords_liens.append((creature.list_of_link[i].A.pos.x, 
                                    creature.list_of_link[i].A.pos.y))
            
        list_of_coords_liens.append((creature.list_of_link[i].B.pos.x, 
                                    creature.list_of_link[i].B.pos.y))
        
        
    # drawing of all elements    
        
    arcade.draw_lines(list_of_coords_liens, arcade.color.BRONZE, lien_thickness)
    arcade.draw_points(list_of_coords_points, arcade.color.RED, point_diam)