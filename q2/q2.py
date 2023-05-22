import numpy as np
from numpy import dot
from numpy.linalg import norm

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))  #norm->정규화 / dot->내적
def main():
  doc = np.array([])
  doc = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])

  query = np.array([1,1,0,0,1,0])

  for i in range(3):
    print('doc'+str(i+1)+': %.2f' % (cos_sim(doc[i, :], query)))

if __name__ == '__main__':
  main()

