import arcade
from Structure_creature.creature import Creature
import affichage_initialisation_update.setup
import affichage_initialisation_update.graphic_display
import affichage_initialisation_update.updating

WIN_WIDTH = 1250
WIN_HEIGHT = 720

WIN_TITLE = "simulation of evolution"



class Mygame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(WIN_WIDTH, WIN_HEIGHT, WIN_TITLE, resizable = True)
        
        self.set_location(75, 75)
        arcade.set_background_color(arcade.color.WHITE)
        
        self.creature = Creature()
        affichage_initialisation_update.setup.initialiser(self.creature)
         
        self.simulation_time = 0.0
        self.stepCount = 0
        self.delta_time_cst = 0.01
        self.delta_time_var  = 1
        self.delta_time_produit = self.delta_time_cst * self.delta_time_var  #delta time utile
        
        """v = [s.velocity for s in self.creature.list_of_points]
        print("\n init vel 2")
        print(v)"""
        
        # affichage du delta_time
        
        self.delta_time_text = arcade.Text(text= f"{self.delta_time_cst * self.delta_time_var}", 
                                           start_x= 1150, start_y= 50, 
                                           color= arcade.color.BLACK, font_size= 10)
        
        
        # gestion de la camera
        
        self.camera = arcade.Camera(WIN_WIDTH, WIN_HEIGHT)
        self.camera_left_bottom_angle = 0, 0
        
        self.Q_pressed = False
        self.D_pressed = False
        self.Z_pressed = False
        self.S_pressed = False
        self.right_pressed = False
        self.left_pressed = False
        
    
    def on_draw(self):
        arcade.start_render()
        
        self.camera.use()
        
        self.delta_time_text.draw()
        
        affichage_initialisation_update.graphic_display.drawing(self.creature)
        
        return super().on_draw()
    
    # utilisation des touches clavier pour bouger la caméra et pour modifier le delta_time
    
    def update_cam_pos(self):
        
        cam_x, cam_y = self.camera_left_bottom_angle
        
        if self.Q_pressed:
            self.camera_left_bottom_angle = (cam_x - 10, cam_y)
        if self.D_pressed:
            self.camera_left_bottom_angle = (cam_x + 10, cam_y)
        if self.Z_pressed:
            self.camera_left_bottom_angle = (cam_x, cam_y + 10)
        if self.S_pressed:
            self.camera_left_bottom_angle = (cam_x, cam_y - 10)
        
        self.camera.move_to(self.camera_left_bottom_angle)
        
    def update_delta_time(self):
        
        if self.right_pressed:
            self.delta_time_var += 0.1
        if self.left_pressed:
            self.delta_time_var -= 0.1
        
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.Q:
            self.Q_pressed = True
        elif key == arcade.key.D:
            self.D_pressed = True
        elif key == arcade.key.Z:
            self.Z_pressed = True
        elif key == arcade.key.S:
            self.S_pressed = True
        
        # gestion de delta time
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.Q:
            self.Q_pressed = False
        elif key == arcade.key.D:
            self.D_pressed = False
        elif key == arcade.key.Z:
            self.Z_pressed = False
        elif key == arcade.key.S:
            self.S_pressed = False
        
        # gestion delat time
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
    
    # fin de la gestion caméra et delta_time
    
    def on_update(self, delta_time: float):
        
        
        self.stepCount += 1
        
        # modification du delta de temps
        
        delta_time_prev = self.delta_time_produit
        self.delta_time_produit = self.delta_time_cst * self.delta_time_var
        
        # mis a jour de la durée
        
        self.simulation_time += self.delta_time_produit
        
        # fin modification delta de temps
        
        affichage_initialisation_update.updating.update(self.creature, self.stepCount, self.delta_time_produit, delta_time_prev)
        
        self.update_cam_pos()
        self.update_delta_time()
        
        self.delta_time_text.text = f"{(self.delta_time_cst * self.delta_time_var) : .2f}"
        
        return super().on_update(delta_time)



def main():
    window = Mygame()
    arcade.run()

if __name__ == "__main__":
    main()