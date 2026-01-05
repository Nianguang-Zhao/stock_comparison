import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# 获取过去五年的数据
end_date = datetime.now()
start_date = "2021-01-08"


# Download stock data for Google (GOOGL) and Amazon (AMZN)
print("Downloading Google stock data...")
googl = yf.download('GOOGL', start=start_date, end=end_date, progress=False, auto_adjust=True)

print("Downloading Amazon stock data...")
amzn = yf.download('AMZN', start=start_date, end=end_date, progress=False, auto_adjust=True)

# 如果返回的是多级列，取第一列
if isinstance(googl.columns, pd.MultiIndex):
    googl_close = googl['Close'].iloc[:, 0] if len(googl['Close'].shape) > 1 else googl['Close']
else:
    googl_close = googl['Close']

if isinstance(amzn.columns, pd.MultiIndex):
    amzn_close = amzn['Close'].iloc[:, 0] if len(amzn['Close'].shape) > 1 else amzn['Close']
else:
    amzn_close = amzn['Close']

# 标准化股价：将起始价格设为100
normalize_base = 100
googl_start_price = float(googl_close.iloc[0])
amzn_start_price = float(amzn_close.iloc[0])

googl_normalized = (googl_close / googl_start_price) * normalize_base
amzn_normalized = (amzn_close / amzn_start_price) * normalize_base

# 计算每条数据点的回报率（用于悬停显示）
googl_returns = ((googl_normalized / normalize_base) - 1) * 100
amzn_returns = ((amzn_normalized / normalize_base) - 1) * 100

# 计算最终回报率（用于末端标注）
googl_return = float(googl_returns.iloc[-1])
amzn_return = float(amzn_returns.iloc[-1])

# 创建交互式图表
fig = go.Figure()

# 添加Google股价线，带悬停信息
fig.add_trace(go.Scatter(
    x=googl.index,
    y=googl_normalized,
    mode='lines',
    name='Google (GOOGL)',
    line=dict(color='#4285F4', width=2),
    hovertemplate='<b>Google (GOOGL)</b><br>' +
                  'Date: %{x|%Y-%m-%d}<br>' +
                  'Normalized Price: %{y:.2f}<br>' +
                  'Return Rate: %{customdata:.2f}%<extra></extra>',
    customdata=googl_returns
))

# 添加Amazon股价线，带悬停信息
fig.add_trace(go.Scatter(
    x=amzn.index,
    y=amzn_normalized,
    mode='lines',
    name='Amazon (AMZN)',
    line=dict(color='#FF9900', width=2),
    hovertemplate='<b>Amazon (AMZN)</b><br>' +
                  'Date: %{x|%Y-%m-%d}<br>' +
                  'Normalized Price: %{y:.2f}<br>' +
                  'Return Rate: %{customdata:.2f}%<extra></extra>',
    customdata=amzn_returns
))

# 添加基准线（100）
fig.add_hline(
    y=normalize_base,
    line_dash="dash",
    line_color="gray",
    opacity=0.5,
    annotation_text="Starting Baseline (100)",
    annotation_position="right"
)

# 在线的末端添加回报率标注
last_date_googl = googl.index[-1]
last_value_googl = float(googl_normalized.iloc[-1])
fig.add_annotation(
    x=last_date_googl,
    y=last_value_googl,
    text=f'{googl_return:+.1f}%',
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='#4285F4',
    ax=20,
    ay=0,
    bgcolor='white',
    bordercolor='#4285F4',
    borderwidth=2,
    font=dict(size=11, color='#4285F4', family='Arial Black')
)

last_date_amzn = amzn.index[-1]
last_value_amzn = float(amzn_normalized.iloc[-1])
fig.add_annotation(
    x=last_date_amzn,
    y=last_value_amzn,
    text=f'{amzn_return:+.1f}%',
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='#FF9900',
    ax=20,
    ay=0,
    bgcolor='white',
    bordercolor='#FF9900',
    borderwidth=2,
    font=dict(size=11, color='#FF9900', family='Arial Black')
)

# 设置图表布局
fig.update_layout(
    title=dict(
        text='Google vs Amazon Stock Price Comparison (Past 5 Years) - Normalized to Starting Point',
        font=dict(size=18, family='Arial', color='black'),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Date', font=dict(size=14)),
        tickfont=dict(size=12),
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=1
    ),
    yaxis=dict(
        title=dict(text='Normalized Price (Starting=100)', font=dict(size=14)),
        tickfont=dict(size=12),
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=1
    ),
    hovermode='x unified',
    legend=dict(
        x=0.02,
        y=0.98,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='gray',
        borderwidth=1
    ),
    width=1400,
    height=800,
    template='plotly_white'
)

# Save as HTML file (interactive)
output_file_html = 'stock_comparison.html'
fig.write_html(output_file_html)
print(f"\nInteractive chart saved as: {output_file_html}")

# 保存为PNG文件（静态）
output_file_png = 'stock_comparison.png'
try:
    fig.write_image(output_file_png, width=1400, height=800, scale=2)
    print(f"Static chart saved as: {output_file_png}")
except Exception as e:
    print(f"Warning: Could not save PNG (this is normal in headless environments): {e}")

# 显示图表（only if running interactively)
try:
    fig.show()
except Exception:
    pass  # Skip in headless environments

# Print statistics
print("\n=== Normalized Stock Statistics (Starting=100) ===")
print(f"\nGoogle (GOOGL):")
current_normalized_googl = float(googl_normalized.iloc[-1])
max_normalized_googl = float(googl_normalized.max())
min_normalized_googl = float(googl_normalized.min())
print(f"  Current normalized price: {current_normalized_googl:.2f}")
print(f"  5-year high: {max_normalized_googl:.2f}")
print(f"  5-year low: {min_normalized_googl:.2f}")
print(f"  5-year return: {(current_normalized_googl - normalize_base):.2f}%")

print(f"\nAmazon (AMZN):")
current_normalized_amzn = float(amzn_normalized.iloc[-1])
max_normalized_amzn = float(amzn_normalized.max())
min_normalized_amzn = float(amzn_normalized.min())
print(f"  Current normalized price: {current_normalized_amzn:.2f}")
print(f"  5-year high: {max_normalized_amzn:.2f}")
print(f"  5-year low: {min_normalized_amzn:.2f}")
print(f"  5-year return: {(current_normalized_amzn - normalize_base):.2f}%")

print(f"\n=== Original Stock Prices ===")
print(f"\nGoogle (GOOGL):")
print(f"  Starting price: ${googl_start_price:.2f}")
print(f"  Current price: ${float(googl_close.iloc[-1]):.2f}")
print(f"  5-year return: {((float(googl_close.iloc[-1]) / googl_start_price - 1) * 100):.2f}%")

print(f"\nAmazon (AMZN):")
print(f"  Starting price: ${amzn_start_price:.2f}")
print(f"  Current price: ${float(amzn_close.iloc[-1]):.2f}")
print(f"  5-year return: {((float(amzn_close.iloc[-1]) / amzn_start_price - 1) * 100):.2f}%")
