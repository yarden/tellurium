"""
    tellurium 1.3.1

    auto-generated code (2016-02-29T17:11:17)
    sedmlDoc: L1V1  
    workingDir: /home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sedx/_te_BorisEJBsteady
    inputType: COMBINE_FILE
"""
from __future__ import print_function, division
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import libsedml
import pandas
import os.path

workingDir = '/home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sedx/_te_BorisEJBsteady'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
#  - model1 

# Model <model1>
model1 = te.loadSBMLModel(os.path.join(workingDir, 'model1.xml'))

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
#  - task1 

# Task <task1>
task1 = [None]
model1.setIntegrator('cvode')
Config = model1
model1.conservedMoietyAnalysis = True
model1.steadyStateSelections = ['[MKKK]', '[MKKK_P]', '[MAPK]', '[MAPK_PP]', '[MKK_P]', '[MAPK_P]', 'time', '[MKK]']
model1.steadyState()
task1[0] = dict(zip(model1.steadyStateSelections, model1.getSteadyStateValues()))
model1.conservedMoietyAnalysis = False

# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
#  - time1 (time)
#  - MAPK1 (MAPK)
#  - MAPK_P1 (MAPK_P)
#  - MAPK_PP1 (MAPK_PP)
#  - MKK1 (MKK)
#  - MKK_P1 (MKK_P)
#  - MKKK1 (MKKK)
#  - MKKK_P1 (MKKK_P)

# DataGenerator <time1>
time1 = [sim['time'] for sim in task1]

# DataGenerator <MAPK1>
MAPK1 = [sim['[MAPK]'] for sim in task1]

# DataGenerator <MAPK_P1>
MAPK_P1 = [sim['[MAPK_P]'] for sim in task1]

# DataGenerator <MAPK_PP1>
MAPK_PP1 = [sim['[MAPK_PP]'] for sim in task1]

# DataGenerator <MKK1>
MKK1 = [sim['[MKK]'] for sim in task1]

# DataGenerator <MKK_P1>
MKK_P1 = [sim['[MKK_P]'] for sim in task1]

# DataGenerator <MKKK1>
MKKK1 = [sim['[MKKK]'] for sim in task1]

# DataGenerator <MKKK_P1>
MKKK_P1 = [sim['[MKKK_P]'] for sim in task1]

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
#  - report1 (Steady State Values)
#  - plot1 (MAPK feedback (Kholodenko, 2000))

# Output <report1>
df = pandas.DataFrame(np.column_stack([MAPK1[0], MAPK_P1[0], MAPK_PP1[0], MKK1[0], MKKK1[0], MKK_P1[0], MKKK_P1[0]]), 
    columns=['MAPK1', 'MAPK_P1', 'MAPK_PP1', 'MKK1', 'MKKK1', 'MKK_P1', 'MKKK_P1'])
print(df.head(10))

# Output <plot1>
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MAPK1[k], color='b', linewidth=1.5, label='[MAPK]')
    else:
        plt.plot(time1[k], MAPK1[k], color='b', linewidth=1.5)
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MAPK_P1[k], color='g', linewidth=1.5, label='[MAPK_P]')
    else:
        plt.plot(time1[k], MAPK_P1[k], color='g', linewidth=1.5)
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MAPK_PP1[k], color='r', linewidth=1.5, label='[MAPK_PP]')
    else:
        plt.plot(time1[k], MAPK_PP1[k], color='r', linewidth=1.5)
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MKK1[k], color='c', linewidth=1.5, label='[MKK]')
    else:
        plt.plot(time1[k], MKK1[k], color='c', linewidth=1.5)
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MKKK1[k], color='m', linewidth=1.5, label='[MKKK]')
    else:
        plt.plot(time1[k], MKKK1[k], color='m', linewidth=1.5)
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MKK_P1[k], color='y', linewidth=1.5, label='[MKK_P]')
    else:
        plt.plot(time1[k], MKK_P1[k], color='y', linewidth=1.5)
for k in range(len(time1)):
    if k == 0:
        plt.plot(time1[k], MKKK_P1[k], color='k', linewidth=1.5, label='[MKKK_P]')
    else:
        plt.plot(time1[k], MKKK_P1[k], color='k', linewidth=1.5)
plt.title('plot1')
plt.legend()
plt.show()
