# 🚀 Deploy Now - Final Steps

Your files are ready! Follow these steps to deploy:

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `stock-price-comparison` (or any name)
3. Make it **Public** ✅ (required for free GitHub Pages)
4. **Don't** check "Add a README file" or any other options
5. Click "Create repository"

## Step 2: Connect and Push

After creating the repository, GitHub will show you commands. Use these instead:

```bash
cd /Users/zng

# Add your GitHub repository (replace YOUR_USERNAME and YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**OR use the deploy script:**
```bash
cd /Users/zng
./deploy.sh YOUR_USERNAME YOUR_REPO_NAME
```

## Step 3: Enable GitHub Pages

1. Go to: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/settings/pages`
2. Under **Source**:
   - Branch: `main`
   - Folder: `/ (root)`
3. Click **Save**
4. Wait 1-2 minutes
5. Visit: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## Step 4: Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. Click **"I understand my workflows, enable them"**
3. Done! It will run automatically every day at 6:00 AM UTC

## Step 5: Test It

1. Go to **Actions** tab
2. Click **"Update Stock Chart Daily"**
3. Click **"Run workflow"** (top right)
4. Select branch: `main`
5. Click **"Run workflow"**
6. Wait 2-3 minutes
7. Check your site - chart should be updated!

## ✅ All Done!

Your chart will now update automatically every day. No manual work needed!

---

**Need help?** Check `QUICK_START.md` or `DEPLOYMENT.md` for more details.

