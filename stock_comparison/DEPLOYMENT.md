# Deployment Guide

## Quick Start

Follow these steps to deploy your stock chart to GitHub Pages with automatic daily updates:

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `stock-price-comparison` or `stock-chart-dashboard`
3. Make it **public** (required for free GitHub Pages)
4. Don't initialize with README, .gitignore, or license (we'll add our own)

### Step 2: Upload Files

**Option A: Using Git (Recommended)**

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Stock price comparison dashboard"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Option B: Using GitHub Web Interface**

1. Go to your repository on GitHub
2. Click "uploading an existing file"
3. Drag and drop all files from this directory:
   - `stock_comparison.py`
   - `index.html`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `.github/workflows/update_chart.yml` (create the folder structure first)

### Step 3: Enable GitHub Pages

1. Go to your repository **Settings**
2. Scroll down to **Pages** in the left sidebar
3. Under **Source**:
   - Select branch: `main` (or `master`)
   - Select folder: `/ (root)`
4. Click **Save**
5. Your site will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

### Step 4: Enable GitHub Actions

1. Go to the **Actions** tab in your repository
2. If prompted, click **"I understand my workflows, enable them"**
3. The workflow will automatically run:
   - Every day at 6:00 AM UTC (scheduled)
   - When you manually trigger it (workflow_dispatch)

### Step 5: Verify It Works

1. Wait a few minutes for the first workflow run to complete
2. Check the **Actions** tab to see if it succeeded (green checkmark)
3. Visit your GitHub Pages URL to see the chart
4. The chart should update automatically every day

## Troubleshooting

### Workflow Fails

**Issue**: GitHub Actions workflow fails with errors

**Solutions**:
- Check the Actions tab for error messages
- Ensure all files are in the correct locations
- Verify Python version in workflow file matches available versions
- Check that stock symbols are valid (GOOGL, AMZN)

### Chart Not Updating

**Issue**: Chart doesn't update daily

**Solutions**:
- Verify the workflow is enabled in Actions tab
- Check the cron schedule in `.github/workflows/update_chart.yml`
- Manually trigger the workflow to test
- Ensure the repository is public (required for free GitHub Pages)

### PNG Export Fails

**Issue**: Warning about PNG export in logs

**Solution**: This is normal in headless environments. The HTML chart will still work fine.

### GitHub Pages Not Loading

**Issue**: 404 error when accessing the site

**Solutions**:
- Ensure GitHub Pages is enabled in Settings
- Check that `index.html` is in the root directory
- Wait a few minutes after enabling Pages (deployment takes time)
- Clear browser cache

## Customization

### Change Update Time

Edit `.github/workflows/update_chart.yml`:

```yaml
- cron: '0 6 * * *'  # Change to your desired time
```

Time is in UTC. Examples:
- `0 0 * * *` = Midnight UTC
- `0 12 * * *` = Noon UTC  
- `0 18 * * 1-5` = 6 PM UTC on weekdays

### Change Stocks

Edit `stock_comparison.py`:

```python
googl = yf.download('GOOGL', ...)  # Change symbol
amzn = yf.download('AMZN', ...)   # Change symbol
```

### Change Time Period

Edit `stock_comparison.py`:

```python
start_date = "2021-01-08"  # Change date
```

## Manual Update

To manually trigger an update:

1. Go to **Actions** tab
2. Click **"Update Stock Chart Daily"**
3. Click **"Run workflow"** button
4. Select branch (usually `main`)
5. Click **"Run workflow"**

## Monitoring

- Check **Actions** tab to see workflow runs
- View logs to see if updates are successful
- Check commit history to see auto-commits from GitHub Actions

## Cost

- **Free**: GitHub Pages and GitHub Actions are free for public repositories
- **Limits**: 
  - GitHub Actions: 2,000 minutes/month for free accounts
  - Daily updates use ~2 minutes, so you have plenty of headroom

## Support

If you encounter issues:
1. Check the GitHub Actions logs
2. Verify all files are correctly placed
3. Ensure repository is public
4. Check that GitHub Pages is enabled

