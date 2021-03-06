"""
Using outputStartTime to set of output.
Two parallel repeated tasks.
"""
from __future__ import print_function
import tellurium as te
import os

antimonyStr = '''
model case_12()
  J0: S1 -> S2; k1*S1-k2*S2
  S1 = 10.0; S2 = 0.0;
  k1 = 0.2; k2=0.01
end
'''

phrasedmlStr = '''
  mod1 = model "case_12"
  sim1 = simulate uniform(0, 2, 10, 49)
  sim2 = simulate uniform(0, 15, 49)
  task1 = run sim1 on mod1
  task2 = run sim2 on mod1
  repeat1 = repeat task1 for S1 in uniform(0, 10, 4), S2 = S1+20, reset=true
  repeat2 = repeat task2 for S1 in uniform(0, 10, 4), S2 = S1+20, reset=true
  plot "Offset simulation" repeat2.time vs repeat2.S1, repeat2.S2, repeat1.time vs repeat1.S1, repeat1.S2
  report repeat2.time vs repeat2.S1, repeat2.S2, repeat1.time vs repeat1.S1, repeat1.S2
'''

# phrasedml experiment
exp = te.experiment(antimonyStr, phrasedmlStr)

# write python code
realPath = os.path.realpath(__file__)
workingDir = os.path.dirname(realPath)
with open(realPath + 'code.py', 'w') as f:
    f.write(exp._toPython(phrasedmlStr, workingDir=workingDir))

# execute python
exp.execute(phrasedmlStr, workingDir=workingDir)

# remove sedx (not hashable due to timestamp)
os.remove(os.path.join(workingDir, 'case_12.sedx'))
