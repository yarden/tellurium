"""
    tellurium 1.3.1

    auto-generated code
    sedmlDoc: L1V1  
    workingDir: /home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sedx/_te_BM12
    inputType: COMBINE_FILE
"""
from __future__ import print_function, division
import tellurium as te
from tellurium.sedml.mathml import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import libsedml
import pandas
import os.path

workingDir = '/home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sedx/_te_BM12'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
# Model <model1>
model1 = te.loadSBMLModel(os.path.join(workingDir, 'model1.xml'))

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
# Task <task1>
# Task: <task1>
task1 = [None]
model1.setIntegrator('cvode')
model1.timeCourseSelections = ['[Z]', '[X]', '[Y]', 'time']
task1[0] = model1.simulate(start=0.0, end=100.0, steps=1000)

# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
# DataGenerator <time>
__var__var_time_0 = np.transpose(np.array([sim['time'] for sim in task1]))
if len(__var__var_time_0.shape) == 1:
     __var__var_time_0.shape += (1,)
time = __var__var_time_0

# DataGenerator <X>
__var__X_X_0 = np.transpose(np.array([sim['[X]'] for sim in task1]))
if len(__var__X_X_0.shape) == 1:
     __var__X_X_0.shape += (1,)
X = __var__X_X_0

# DataGenerator <Y>
__var__Y_Y_0 = np.transpose(np.array([sim['[Y]'] for sim in task1]))
if len(__var__Y_Y_0.shape) == 1:
     __var__Y_Y_0.shape += (1,)
Y = __var__Y_Y_0

# DataGenerator <Z>
__var__Z_Z_0 = np.transpose(np.array([sim['[Z]'] for sim in task1]))
if len(__var__Z_Z_0.shape) == 1:
     __var__Z_Z_0.shape += (1,)
Z = __var__Z_Z_0

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
# Output <plot1>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], X[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8, label='X')
    else:
        plt.plot(time[:,k], X[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8)
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], Y[:,k], '-o', color='b', linewidth=1.5, markersize=3.0, alpha=0.8, label='Y')
    else:
        plt.plot(time[:,k], Y[:,k], '-o', color='b', linewidth=1.5, markersize=3.0, alpha=0.8)
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], Z[:,k], '-o', color='g', linewidth=1.5, markersize=3.0, alpha=0.8, label='Z')
    else:
        plt.plot(time[:,k], Z[:,k], '-o', color='g', linewidth=1.5, markersize=3.0, alpha=0.8)
plt.title('BM 12', fontweight='bold')
plt.xlabel('time', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.savefig(os.path.join(workingDir, 'plot1.png'), dpi=100)
plt.show()

