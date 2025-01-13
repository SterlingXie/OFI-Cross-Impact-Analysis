import pandas as pd

file1 = "XNAS-20250109-DBURTAEFBS/xnas-itch-20241209-20241231.mbp-10.csv"
file2 = "XNAS-20250109-DBURTAEFBS/xnas-itch-20250101-20250108.mbp-10.csv"
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
combined_df = pd.concat([df1, df2], ignore_index=True)

aapl_data = combined_df[combined_df['symbol'] == 'AAPL']
aapl_data = aapl_data[aapl_data['action'].isin(['A', 'T'])]
columns_to_keep = ['ts_event'] + [
    f'{header}_{i:02}'
    for i in range(5) # 00 to 04
    for header in ['bid_px', 'ask_px', 'bid_sz', 'ask_sz']
]
aapl_simplified = aapl_data[columns_to_keep]
aapl_simplified.loc[:, 'ts_event'] = pd.to_datetime(aapl_simplified['ts_event'])
aapl_simplified.set_index("ts_event", inplace=True)
aapl_simplified = aapl_simplified.resample("T").mean().reset_index()

aapl_simplified.to_csv('aapl.csv', index=False)