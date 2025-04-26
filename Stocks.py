class Stock:
    def __init__(self, name, price, monthly_yield):
        self.name = name
        self.price = price
        self.monthly_yield = monthly_yield


class PortfolioOptimizer:
    def __init__(self, stocks, budget):
        self.stocks = stocks
        self.budget = budget
        self.best_total_yield = 0
        self.best_combo = None

    def optimize(self):
        max_quantities = [int(self.budget // stock.price) for stock in self.stocks]
        self._search_combinations([0] * len(self.stocks), 0, 0, 0, max_quantities)

    def _search_combinations(self, quantities, index, current_cost, current_yield, max_quantities):
        if current_cost > self.budget:
            return

        if index == len(self.stocks):
            if current_yield > self.best_total_yield:
                self.best_total_yield = current_yield
                self.best_combo = quantities.copy()
            return

        for qty in range(0, max_quantities[index] + 1):
            next_cost = current_cost + qty * self.stocks[index].price
            next_yield = current_yield + qty * self.stocks[index].monthly_yield
            quantities[index] = qty
            self._search_combinations(quantities, index + 1, next_cost, next_yield, max_quantities)

    def display_result(self):
        if self.best_combo:
            print("Best combination:")
            for stock, qty in zip(self.stocks, self.best_combo):
                print(f"  {stock.name}: {qty} units")
            print(f"Total monthly yield: {self.best_total_yield:.2f}")
        else:
            print("No valid combination found.")


if __name__ == "__main__":
    stocks = [
        Stock("A", 7.64, 0.09),
        Stock("B", 8.77, 0.08),
        Stock("C", 7.59, 0.08),
        Stock("D", 9.30, 0.09),
    ]

    budget = 33.00
    optimizer = PortfolioOptimizer(stocks, budget)
    optimizer.optimize()
    optimizer.display_result()
