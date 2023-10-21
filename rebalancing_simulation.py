import numpy as np

class SimulateK:

    def  __init__(self, c, r, a):
      self.c = c
      self.r = r
      # self.qa = 0
      # self.qb = 0
      self.a = a
      self.profits = {}

    def simulate(self, trials, beta, betb, pa = 0, pb = 0):
  
       
       for k in range(2, 7):
          profit_acc = np.arry()
          for i in range(trials):
            pa = np.random.uniform(0, 100)
            pb = 1 - self.pa
            qa = self.a*pa
            qb = self.a*pb
            la = beta / qa
            lb = betb / qb
            qa = SimulateK.update(la)
            qb = SimulateK.update(lb)
            if np.random.randn > pa:
              profit = beta - lb
            else:
              profit = betb - la
            profit_acc.add(profit)
          
          self.profits.update({k : np.mean(profit_acc)})
              
  
             

             

    @staticmethod
    def update(l):
        pass


    