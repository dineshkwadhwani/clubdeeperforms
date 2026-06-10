#!/bin/bash
# Club Deeper – Forms Creator Setup Script (Mac)
# Run this once before running create_forms.py

echo "============================================"
echo "  Club Deeper – Setup"
echo "============================================"

# Check Python
echo ""
echo "Checking Python version..."
python3 --version

# Install pip if not available
echo ""
echo "Ensuring pip is available..."
python3 -m ensurepip --upgrade 2>/dev/null || true
python3 -m pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing required libraries..."
python3 -m pip install -r requirements.txt

echo ""
echo "============================================"
echo "  Setup complete!"
echo "  Make sure credentials.json is in this"
echo "  folder, then run:"
echo ""
echo "  python3 create_forms.py"
echo "============================================"
