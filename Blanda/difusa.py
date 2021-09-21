import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

dia = ctrl.Antecedent(np.arange(0, 8, 1),'dia')
mes = ctrl.Antecedent(np.arange(0, 12, 1),'mes')
hora = ctrl.Antecedent(np.arange(0,25,1)) ########?
carretera = ctrl.Antecedent(np.arange(0, 2, 1),'carretera') #### idk
lluvia = ctrl.Antecedent(np.arange(0, 2, 1),'lluvia')  #### same

dia['lunes'] = fuzz.trimf(dia.universe,[0,0,0.1])
dia['martes'] = fuzz.trimf(dia.universe,[0.9,1,1.1])
dia['miercoles'] = fuzz.trimf(dia.universe,[1.9,2,2.1])
dia['jueves'] = fuzz.trimf(dia.universe,[2.9,3,3.1])
dia['viernes'] = fuzz.trimf(dia.universe,[3.9,4,4.1])
dia['sabado'] = fuzz.trimf(dia.universe,[4.9,5,5.1])
dia['domingo'] = fuzz.trimf(dia.universe,[5.9,6,6.1])
dia.view()

mes['enero'] = fuzz.trimf(mes.universe,[0,0,0.1])
mes['febrero'] = fuzz.trimf(mes.universe,[0.9,1,1.1])
mes['marzo'] = fuzz.trimf(mes.universe,[1.9,2,2.1])
mes['abril'] = fuzz.trimf(mes.universe,[2.9,3,3.1])
mes['mayo'] = fuzz.trimf(mes.universe,[3.9,4,4.1])
mes['junio'] = fuzz.trimf(mes.universe,[4.9,5,5.1])
mes['julio'] = fuzz.trimf(mes.universe,[5.9,6,6.1])
mes['agosto'] = fuzz.trimf(mes.universe,[6.9,7,7.1])
mes['septiembre'] = fuzz.trimf(mes.universe,[7.9,8,8.1])
mes['octubre'] = fuzz.trimf(mes.universe,[8.9,9,9.1])
mes['noviembre'] = fuzz.trimf(mes.universe,[9.9,10,10.1])
mes['diciembre'] = fuzz.trimf(mes.universe,[10.9,11,11.1])
mes.view()

hora['madrugada'] = fuzz.trimf(hora.universe,[0,0,5.9])
hora['mañana'] = fuzz.trimf(hora.universe,[6,9,11.9])
hora['medio_dia'] = fuzz.trimf(hora.universe,[12,13,14])
hora['tarde'] = fuzz.trimf(hora.universe,[13,16,17.9])
hora['noche'] = fuzz.trimf(hora.universe,[18,21,23.9])
hora.view()

carretera['mala'] = fuzz.trimf(carretera.universe,[0,0, 0.4])
carretera['regular'] = fuzz.trimf(carretera.universe,[0,0.4,0.7])
carretera['buena'] = fuzz.trimf(carretera.universe,[0.6,0.8.,1])
carretera.view()

lluvia['llovizna'] = fuzz.trimf(lluvia.universe,[0,0,0.3])
lluvia['lluvia'] = fuzz.trimf(lluvia.universe,[0.3,0.5,0.7])
lluvia['tormenta'] = fuzz.trimf(lluvia.universe,[0.6,0.8,1])
lluvia.view()

rule1 = ctrl.Rule(,)
