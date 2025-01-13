# OFI-Cross-Impact-Analysis
This project analyzed the impact of order flow imbalance on price movements for Nasdaq stocks.

Steps to run this project:
1. Install the dependencies listed on the `requirements.txt` file.
2. Download data[1] from Databento in csv format (the current setup allows for two files to be concatenated).
3. Change depth level by changing the variable in each function header (i.e. levels=5) on the Jupyter notebook. 
4. Change lag by changing the lag variable when calling the contemporaneous_cross_impact function for each ticker.

[1] Recommended data:
Databento (Nasdaq TotalView–ITCH, MBP-10 schema).
Tickers: (AAPL, TSLA, COST, AMGN, AEP).
LOB Levels: 00 to 04
Time Period: 1 month

Post-customization, all graph generation, data analysis, and regression generation is handled by the notebook. Run all cells in order.