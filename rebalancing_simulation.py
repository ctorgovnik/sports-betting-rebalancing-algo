import numpy as np

class SimulateK:

    def  __init__(self, c, r, a):
      self.c = c
      self.r = r  # r = lambda
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
            qa_adj = SimulateK.update(pa, la, k)
            qb_adj = SimulateK.update(pb, lb, k) 
            
            la_new = 0 
            lb_new = 0
            
            if np.random.randn > pa:
              profit = beta - lb_new
            else:
              profit = betb - la_new
            profit_acc.add(profit)
          
          self.profits.update({k : np.mean(profit_acc)})
              
  
             

             

    def update(self, p, l, k):
        q = ((2 + self.r * self.c) / (2 + k - self.r * l)) * p
        return q
        


    