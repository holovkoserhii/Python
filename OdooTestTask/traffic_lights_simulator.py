# Завдання 5
# Змоделювати роботу світлофорів на перехресті, є світлофор для автомобілів, є для пішоходів,
# існують режими роботи (нічний, звичайний). Потрібно щоб була можливість додавати видаляти світлофори,
# перемикати в ручному режимі. Без ручного режиму усі світлофори мають працювати синхронно один з одним.
# Модель максимально наближена до реального життя.
# Має бути передбачена можливість отримувати інформацію про поточний стан кожного світлофора
# (стан, режим, скільки часу до наступного стану) для виведення на екран, надсиланню по мережі,
# інші розширення.

import datetime

class Traffic_Light:
    def __init__(self, title, axis, pedestrian = False):
        self.title = title
        self.axis = axis # All traffic-lights are installed along one axis (0) or perpendicular axis (1). Usually, 
#         Traffic lights, no matter pedestrian or for vehicles, give the way along one axis and restrict along the other.
        self.pedestrian = pedestrian # Pedestrian (True) or for vehicles (False)
        self.active = False # Turned on or off presently
        print("New Traffic light created. Name = " + self.title)

    def __del__(self):
        print ('Traffic light deleted')
        
    def activate(self, night_schedule = False):
        self.active = True
        self.night_schedule = night_schedule # Regular schedule (False) or Night schedule (True)
        self.mode_auto = True # Each traffic light is activated in auto mode. Change to manual if needed
        print ('Traffic light activated')
        return self
        
    def deactivate(self):
        self.active = False
        del self.night_schedule
        del self.mode_auto
        print ('Traffic light deactivated')
        return self
        
    def set_manual_mode(self):
        if self.mode_auto:
            self.mode_auto = False
            print ('Traffic light switched to manual mode')
            return self
    
    def get_status(self):
        
        present = datetime.datetime.now().time().second
        
        if present < 27:
#             axis0_pedestrian_false = "green"
#             axis0_pedestrian_true = "green"
#             axis1_pedestrian_false = "red"
#             axis1_pedestrian_true = "red"
            if self.axis == 0 and self.pedestrian == False:
                self.color = "Green"
            if self.axis == 0 and self.pedestrian == True:
                self.color = "Green"
            if self.axis == 1 and self.pedestrian == False:
                self.color = "Red"
            if self.axis == 1 and self.pedestrian == True:
                self.color = "Red"
            self.time_from_the_start = present
            self.time_till_the_end = 27 - present
        
        if (present >= 27) and (present < 30):
#             axis0_pedestrian_false = "yellow"
#             axis0_pedestrian_true = "red"
#             axis1_pedestrian_false = "red + yellow"
#             axis1_pedestrian_true = "red"
            if self.axis == 0 and self.pedestrian == False:
                self.color = "Yellow"
            if self.axis == 0 and self.pedestrian == True:
                self.color = "Red"
            if self.axis == 1 and self.pedestrian == False:
                self.color = "Red + Yellow"
            if self.axis == 1 and self.pedestrian == True:
                self.color = "Red"
            self.time_from_the_start = present - 27
            self.time_till_the_end = 30 - present
        
        if present >= 30 and present < 57:
#             axis0_pedestrian_false = "red"
#             axis0_pedestrian_true = "red"
#             axis1_pedestrian_false = "green"
#             axis1_pedestrian_true = "green"
            if self.axis == 0 and self.pedestrian == False:
                self.color = "Red"
            if self.axis == 0 and self.pedestrian == True:
                self.color = "Red"
            if self.axis == 1 and self.pedestrian == False:
                self.color = "Green"
            if self.axis == 1 and self.pedestrian == True:
                self.color = "Green"
            self.time_from_the_start = present - 30
            self.time_till_the_end = 57 - present
        
        if present >= 57:
#             axis0_pedestrian_false = "red + yellow"
#             axis0_pedestrian_true = "red"
#             axis1_pedestrian_false = "yellow"
#             axis1_pedestrian_true = "red"
            if self.axis == 0 and self.pedestrian == False:
                self.color = "Red + Yellow"
            if self.axis == 0 and self.pedestrian == True:
                self.color = "Red"
            if self.axis == 1 and self.pedestrian == False:
                self.color = "Yellow"
            if self.axis == 1 and self.pedestrian == True:
                self.color = "Red"
            self.time_from_the_start = present - 57
            self.time_till_the_end = 60 - present
           
        print("Active: " + str(self.active))
        print("Mode_auto: " + str(self.mode_auto))
        print("Color: " + str(self.color))
        print("Time from the start: " + str(self.time_from_the_start))
        print("Time till the end: " + str(self.time_till_the_end))
        
        return self


tl1v = Traffic_Light("axis 0 for pedestrians", 1, pedestrian = True)
tl1v.activate()
print(tl1v.axis)
print(tl1v.pedestrian)
tl1v.get_status()