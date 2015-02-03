import sys
import os
os.chdir('C:\libsvm\libsvm-3.20\python')
from svmutil import *
y, x = svm_read_problem('../3d_xlj.txt')
m = svm_train(y[:200], x[:200], '-c 4')
p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)
