import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

agua = ctrl.Antecedent(np.arange(0,101,1), 'agua')
sol = ctrl.Antecedent(np.arange(0,121,1), 'sol')
tip = ctrl.Consequent(np.arange(0,101,1), 'tip')

agua['poco']= fuzz.trapmf(agua.universe, [0,0,10,30])
agua['ideal']= fuzz.trimf(agua.universe, [10,30,50])
agua['mucho']= fuzz.trapmf(agua.universe, [30,50,100,100])
agua.view()

sol['poco']= fuzz.trapmf(sol.universe, [0,0,20,45])
sol['ideal']= fuzz.trimf(sol.universe, [20,45,70])
sol['mucho']= fuzz.trapmf(sol.universe, [45,70,120,120])
sol.view()

tip['poco']= fuzz.trapmf(tip.universe, [0, 0, 25, 50])
tip['ideal']= fuzz.trimf(tip.universe, [25, 50, 75])
tip['mucho']= fuzz.trapmf(tip.universe, [50 , 75, 100, 100])
tip.view()

regla1 = ctrl.Rule(agua['poco'] | sol['poco'], tip['poco'])
regla2 = ctrl.Rule(agua['poco'] | sol['ideal'], tip['poco'])
regla3 = ctrl.Rule(agua['poco'] | sol['mucho'], tip['errado'])
regla4 = ctrl.Rule(agua['ideal'] | sol['poco'], tip['ideal'])
regla5 = ctrl.Rule(agua['ideal'] | sol['ideal'], tip['ideal'])
regla6 = ctrl.Rule(agua['ideal'] | sol['muito'], tip['poco'])
regla7 = ctrl.Rule(agua['mucho'] | sol['poco'], tip['errado'])
regla8 = ctrl.Rule(agua['mucho'] | sol['ideal'], tip['errado'])
regla9 = ctrl.Rule(agua['mucho'] | sol['mucho'], tip['errado'])

tipping_ctrl = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
#############################################################
tipping.input['agua'] = 100
tipping.input['sol'] = 110
##############################################################
tipping.compute()
##############################################################
tipping.output['tip']
tip.view(sim=tipping)
