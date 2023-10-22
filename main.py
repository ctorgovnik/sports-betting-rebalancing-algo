
from rebalancing_simulation import SimulateK

def main():
    simulate_k = SimulateK(50, 0.1, 1.15)
    simulate_k.simulate(50, 20000, 10000)
    print(simulate_k.profits)

    rounded_profits, top_3 = simulate_k.get_stats()

    print(rounded_profits)
    print(top_3)
    
    simulate_k.simulate(50, 100000, 20000)
    rounded_profits, top_3 = simulate_k.get_stats()
    print(top_3)


    simulate_k.simulate(50, 60000, 10000)
    print(top_3)

if __name__ == "__main__":
    main()


