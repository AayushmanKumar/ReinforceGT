## Overview

This notebook implements a game-theoretic approach to option pricing using Nash equilibrium concepts. It retrieves historical stock and option data for a given ticker (default: AAPL), constructs a binomial tree for option pricing, and uses convex optimization (via CVXPY) to solve for Nash equilibrium prices. The results are backtested against actual market prices for recent option expiries.

---

## Key Steps

### 1. Data Retrieval

- **Stock Data:**  
  Downloads historical closing prices for the specified ticker using `yfinance`.
- **Option Chain:**  
  Retrieves available option expiration dates and the corresponding call and put option data.

### 2. Parameter Setup

- **Volatility Calculation:**  
  Computes log returns and annualized volatility from historical prices.
- **Binomial Tree Parameters:**  
  Sets up the up/down factors, risk-free rate, and time steps for the binomial model.

### 3. Binomial Tree Construction

- **Asset Price Tree:**  
  Builds a binomial tree for the underlying asset price evolution.
- **Option Payoff:**  
  Calculates the terminal payoff for a call option at maturity for the last available strike price.

### 4. Backward Induction

- **Option Value Tree:**  
  Uses backward induction to compute the option value at each node in the tree.

### 5. Payoff Matrix Construction

- **Matrix Setup:**  
  Flattens the option value tree into a square payoff matrix, representing the game between the option holder and writer.

### 6. Nash Equilibrium via Convex Optimization

- **Variables:**  
  Defines probability vectors for both players and the value variable.
- **Constraints:**  
  Ensures valid probability distributions and Nash equilibrium conditions.
- **Optimization:**  
  Solves for the Nash equilibrium using `cvxpy`.

### 7. Backtesting

- **Recent Expiries:**  
  For the last 5 option expiries, repeats the pricing process and compares the Nash equilibrium price to the market price.
- **Results:**  
  Collects expiry, strike, market price, Nash price, absolute error, and relative error for each expiry.

---

## Output

- **Backtest Results:**  
  The notebook prints a DataFrame summarizing the comparison between Nash equilibrium prices and market prices for recent expiries.

---

## Notable Libraries Used

- `cvxpy` for convex optimization (Nash equilibrium computation)
- `yfinance` for financial data retrieval
- `pandas` and `numpy` for data manipulation and calculations

---

## File Location

- Nash_Bashers.ipynb

---

## Example Output

The final output is a table like:

| expiry      | strike | market_price | nash_price | error |
|-------------|--------|--------------|------------|-------|
| 2024-06-21  | 200    | 5.25         | 5.10       | -0.15 |
| ...         | ...    | ...          | ...        | ...   |

---

## Remarks

- The approach demonstrates the application of game theory to financial derivatives pricing.
- The Nash equilibrium price may differ from the market price, and the relative error is reported for each expiry.
- The notebook is modular and can be adapted for other tickers or option types with minor changes.