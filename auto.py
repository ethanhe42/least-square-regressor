import sys
import subprocess
data=[
        ['training_data_prob4_1.txt','testing_data_prob4_1.txt'],
        ['training_data_prob4_2.txt','testing_data_prob4_2.txt'],
        ['training_data_prob4_3.txt','testing_data_prob4_3.txt'],
        ]
name='output.txt'
with open(name,'w') as f:
    for i in range(len(data)):
        instruction=['python','linreg.py',data[i][0],data[i][1]]
        f.write('%'+' '.join(instruction)+'\n')
        f.write(subprocess.check_output(instruction))
        f.write('\n')
