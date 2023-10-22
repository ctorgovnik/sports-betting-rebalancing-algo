import numpy as np

class SimulateK:

    def  __init__(self, c, r, a):
      self.c = c
      self.r = r  # r = lambda
      self.a = a
      self.profits = {}

    def simulate(self, trials, beta, betb, pa = 0, pb = 0):
  
       
       for k in np.arange(2, 7, 0.1):
          profit_acc = np.array([])
          for i in range(trials):
            pa = np.random.uniform(0, 100)
            pb = 1 - pa
            qa = self.a*pa
            qb = self.a*pb
            la = beta / qa
            lb = betb / qb
            qa_adj = self.update_odds(pa, la, k)
            qb_adj = self.update_odds(pb, lb, k) 
            
            la_new = beta/qa_adj
            lb_new = betb/qb_adj
            
            if np.random.randn() > pa:
              profit = beta - lb_new
            else:
              profit = betb - la_new
            profit_acc = np.append(profit_acc, profit)

          
          self.profits.update({k : np.mean(profit_acc)})
              
             

    def update_odds(self, p, l, k):
        q = ((2 + self.r * self.c) / (2 + k - self.r * l)) * p
        return q
    
    def get_stats(self):
       rounded_profits = {round(k, 2): round(v, 2) for k, v in self.profits.items()}
       top_3_items = sorted(self.profits.items(), key=lambda x: x[1], reverse=True)[:3]

       top_3_k = [item[0] for item in top_3_items]

       return rounded_profits, top_3_k


        


    