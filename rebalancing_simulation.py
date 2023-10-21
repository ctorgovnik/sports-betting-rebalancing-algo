import numpy as np

class SimulateK:

    def  __init__(self, c, r, a):
      self.c = c
      self.r = r
      self.qa = 0
      self.qb = 0
      self.a = a
      self.profits = {}

    def simulate(self, trials, beta, betb, random_probabilities, pa = 0, pb =0):
  
       
       for k in range(2, 7):
          for i in range(trials):
             if (random_probabilities):
                pa = np.random.uniform(0, 100)
                pb = 1 - self.pa
             self.qa = self.a*self.pa
             self.qb = self.a*self.pb
             la = beta / self.qa
             lb = betb / self.qb
             self.qa = SimulateK.update(la)
             self.qb = SimulateK.update(lb)
             if np.random.randn > pa:
                profit = beta - lb
             else:
                profit = betb - la
              
  
             

             

    @staticmethod
    def update(l):
        pass


    