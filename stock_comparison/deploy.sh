#!/bin/bash

# Quick deployment script for GitHub
# Usage: ./deploy.sh YOUR_USERNAME YOUR_REPO_NAME

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: ./deploy.sh YOUR_USERNAME YOUR_REPO_NAME"
    echo "Example: ./deploy.sh johndoe stock-price-comparison"
    exit 1
fi

USERNAME=$1
REPO_NAME=$2

echo "🚀 Starting deployment..."
echo "Repository: https://github.com/$USERNAME/$REPO_NAME"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
fi

# Add all files
echo "📝 Adding files..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Initial commit: Stock price comparison dashboard"
fi

# Set remote (will overwrite if exists)
echo "🔗 Setting up remote..."
git remote remove origin 2>/dev/null
git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Files uploaded successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Go to: https://github.com/$USERNAME/$REPO_NAME/settings/pages"
echo "2. Under 'Source', select:"
echo "   - Branch: main"
echo "   - Folder: / (root)"
echo "3. Click 'Save'"
echo "4. Wait 1-2 minutes, then visit:"
echo "   https://$USERNAME.github.io/$REPO_NAME/"
echo ""
echo "5. Enable GitHub Actions:"
echo "   - Go to Actions tab"
echo "   - Click 'I understand my workflows, enable them'"
echo ""
echo "🎉 Done! Your chart will update automatically every day!"

