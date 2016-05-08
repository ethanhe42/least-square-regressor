import numpy as np
import sys
import numpy.linalg as alg
raw_train=sys.argv[1]
raw_test=sys.argv[2]

def readData(raw_train,tr=True):
    #ret data, n, dim
    with open(raw_train) as f:
        nTrain,dim=[int(i) for i in f.readline().split()]
        train=np.loadtxt(f.readlines())
        if tr:
            label=train.T[-1]
            data=np.concatenate((train.T[:-1],[np.ones(nTrain)])).T
            return data,label
        else:
            if dim==1:
                train=train.T[:,None]
            data=np.concatenate((train.T,[np.ones(nTrain)])).T
            return data
        #print train.dtype
        return 
train,label=readData(raw_train)
test=readData(raw_test,False)

#print train
#print label
#print test

w=alg.inv(train.T.dot(train)).dot(train.T).dot(label.T)
print 'w:',' '.join(str(i) for i in w)
y=test.dot(w.T)
for i in range(len(y)):
    print ' '.join(str(p) for p in test[i][:-1]),'--',y[i]

