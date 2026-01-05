# 🚀 Quick Start Guide

## Deploy in 5 Minutes!

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `stock-price-comparison` (or any name you like)
3. Make it **Public** ✅
4. **Don't** initialize with README, .gitignore, or license
5. Click "Create repository"

### Step 2: Upload Files

**Copy these commands and run them in your terminal:**

```bash
cd /Users/zng

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Stock price comparison dashboard"

# Add your GitHub repository (replace YOUR_USERNAME and YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under **Source**:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes, then visit: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

### Step 4: Enable GitHub Actions
1. Go to **Actions** tab
2. If you see a message, click **"I understand my workflows, enable them"**
3. Done! The workflow will run automatically every day at 6:00 AM UTC

### Step 5: Test It Works
1. Go to **Actions** tab
2. Click **"Update Stock Chart Daily"**
3. Click **"Run workflow"** button (top right)
4. Select branch: `main`
5. Click **"Run workflow"**
6. Wait 2-3 minutes for it to complete
7. Check your GitHub Pages site - the chart should be updated!

## ✅ That's It!

Your chart will now:
- ✅ Update automatically every day
- ✅ Be accessible at your GitHub Pages URL
- ✅ Show interactive hover tooltips
- ✅ Display return rates at the end of lines

## 📝 Important Notes

- **Repository must be PUBLIC** for free GitHub Pages
- First workflow run may take 3-5 minutes
- Chart updates happen automatically - no manual work needed!
- You can manually trigger updates anytime from Actions tab

## 🔧 Troubleshooting

**Can't see the chart?**
- Wait 2-3 minutes after enabling Pages
- Check that `index.html` is in the root directory
- Verify repository is public

**Workflow not running?**
- Check Actions tab for error messages
- Ensure all files are uploaded correctly
- Verify Python version in workflow (should be 3.11)

**Need help?**
- Check the full `DEPLOYMENT.md` guide
- Review GitHub Actions logs for errors

