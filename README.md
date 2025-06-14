
Quant Strategy: Regime-Based Volatility Model (Live-Traded)

This project showcases a simplified version of a live-traded algorithmic strategy developed using time-series modeling and custom volatility overlays.

The strategy is based on:
- Regime identification using Hidden Markov Models (HMM)
- Volatility insight using custom GARCH adjustments (logic redacted)
- A multi-layered signal generation process combining statistical modeling and market heuristics

---

# Results (Live Performance)

- February 2025: 14.2% 
- March 2025: 11.1%  
- Max drawdown (backtest): 8%  
- Backtest Sharpe Ratio: ~3.3

> Executed using Zerodha API on a basket of NSE stocks. Logs available on request.

---

# About the Code

This repo includes:
- Basic regime classification via HMM (`hmm.py`)  
- A placeholder signal engine using MA-50/200 logic (`core_logic.py`)  
- Sample backtest-trade result (`result.txt`)

> Note: This is a simplified version of my proprietary strategy.  
> The core logic and execution components have been redacted for confidentiality.

---



