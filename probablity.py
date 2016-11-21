import chance, numpy as np
def matmul(exp):
  x = np.matrix('0 0 0 0 0; 0 0 0 0 0')
  for i in exp:
    x = np.dot(x,x)
