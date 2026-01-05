# Stock Price Comparison Dashboard

Interactive stock price comparison chart for Google (GOOGL) and Amazon (AMZN) over the past 5 years.

## Features

- 📊 Interactive Plotly chart with hover tooltips
- 📈 Normalized prices (starting at 100) for easy comparison
- 🔄 Auto-updates daily via GitHub Actions
- 📱 Responsive design
- 🌐 Deployed on GitHub Pages

## Live Demo

Visit the [GitHub Pages site](https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/) to view the live chart.

## How It Works

1. **Daily Updates**: GitHub Actions runs the script every day at 6:00 AM UTC
2. **Data Source**: Uses `yfinance` to fetch stock data from Yahoo Finance
3. **Chart Generation**: Creates an interactive HTML chart using Plotly
4. **Auto-Deploy**: Commits and pushes the updated chart to the repository

## Setup Instructions

### 1. Create a GitHub Repository

1. Create a new repository on GitHub
2. Clone it locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

### 2. Copy Files

Copy all files from this directory to your repository:
- `stock_comparison.py`
- `index.html`
- `.github/workflows/update_chart.yml`
- `requirements.txt` (if you have one)

### 3. Enable GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select the branch (usually `main` or `master`)
4. Select the folder (usually `/ (root)`)
5. Click "Save"

### 4. Enable GitHub Actions

1. Go to "Actions" tab in your repository
2. Click "I understand my workflows, enable them"
3. The workflow will run automatically on schedule

### 5. Manual Trigger (Optional)

You can manually trigger the workflow:
1. Go to "Actions" tab
2. Select "Update Stock Chart Daily"
3. Click "Run workflow"

## Customization

### Change Update Schedule

Edit `.github/workflows/update_chart.yml` and modify the cron schedule:
```yaml
- cron: '0 6 * * *'  # 6:00 AM UTC daily
```

Cron format: `minute hour day month weekday`
- `0 6 * * *` = 6:00 AM UTC every day
- `0 0 * * *` = Midnight UTC every day
- `0 12 * * 1-5` = Noon UTC on weekdays only

### Change Stocks

Edit `stock_comparison.py` and modify the stock symbols:
```python
googl = yf.download('GOOGL', ...)  # Change 'GOOGL' to another symbol
amzn = yf.download('AMZN', ...)   # Change 'AMZN' to another symbol
```

### Change Time Period

Edit `stock_comparison.py`:
```python
start_date = "2021-01-08"  # Change to your desired start date
```

## Requirements

- Python 3.11+
- yfinance
- plotly
- pandas
- numpy
- kaleido (for PNG export)

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python stock_comparison.py
   ```

3. Open `stock_comparison.html` in your browser

## License

MIT License - feel free to use this for your own projects!

