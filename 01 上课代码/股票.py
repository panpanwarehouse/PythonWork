open_prices = [115, 120, 124, 135, 130]
close_prices = [120, 124, 128, 144, 126]

# 计算每个交易日的涨跌情况和涨幅百分比
daily_changes = [(close - open) / open * 100 for open, close in zip(open_prices, close_prices)]

# 输出每个交易日的涨跌情况
for i, change in enumerate(daily_changes, start=1):
    status = "涨" if change > 0 else "跌"
    print(f"第 {i} 天：{status}，涨幅：{change:.2f}%")

# 输出最大涨幅的日期和对应的数据
max_increase_index = daily_changes.index(max(daily_changes))
max_increase_percentage = daily_changes[max_increase_index]

print(f"\n最大涨幅的日期是第 {max_increase_index + 1} 天")
print(f"涨幅百分比为：{max_increase_percentage:.2f}%")
print(f"开盘价：{open_prices[max_increase_index]}，收盘价：{close_prices[max_increase_index]}")