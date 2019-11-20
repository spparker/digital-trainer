from models import Day, FitnessComponent, EnergySystem, Module

fit_com = ['Flexability', 'Balance', 'Stability', 'Aerobic', 'Anarobic',
           'Endurance', 'Power', 'Strength']

nrg_sys = ['Phosphagen', 'Glycogen', 'Oxigen']


days = 7
my_coms = [fit_com[7], fit_com[2], fit_com[3]]


for day in range(0,days):
    print("Day "+str(day))



