from datetime import datetime, timedelta
class Collaborator(object):
    def __init__(self, name, hour_per_week, rest_between_turn=60) -> None:
        self.name = name
        self.hour_per_week = hour_per_week
        self.hour_worked_week = 0
        self.work_today = True
        self.last_turn = datetime.now()
        self.rest_between_turn = timedelta(minutes = rest_between_turn) 

    def disponibility_to_work(self):
        if self.work_today:
            pass
            
        elif datetime.now() - self.last_turn > self.rest_between_turn:
            self.work_today=True
            
        else:
            left_time_rest = self.rest_between_turn - (datetime.now() - self.last_turn)
            print(f"Colaborador no puede entrar aun debe descansar: {left_time_rest}")
            self.work_today = False

        return self.work_today

    def work(self, hours=3):
        # Crear alerta que avise cuando se aproxima la hora extra
        if self.disponibility_to_work() == False:
            return False
        else:

            if hours<0:
                print("las horas no puedes ser negativas")
                return False
            elif hours<3:
                print("El trabajador no puede trabajar menos de 3 horas")
                return False
            elif hours>12:
                print("El colaborador no puede trabajar más de 12 horas")
                return False
            else:
                self.hour_worked_week += hours
                self.work_today = False
                return True

    def reset_week(self):
        print(f"El colaborador realizao {self.hour_worked_week} horas en la semana")
        self.hour_worked_week = 0

    def compesation_hour(self):
        extra_hour = max(self.hour_worked_week - self.hour_per_week, 0)
        if extra_hour > 0:
            print(f"Colaborador realizo: {extra_hour} hora extra")
            self.hour_per_week -= extra_hour

        else:
            print("sin horas extras")

        self.reset_week()

