#!/bin/bash

echo "🎭 SentimentScope - Setup Script"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Navigate to backend directory
cd backend

echo "📦 Setting up Python virtual environment..."
python3 -m venv venv

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📥 Installing Python dependencies (this may take a few minutes)..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📚 Downloading NLTK data..."
python3 << EOF
import nltk
nltk.download('brown')
nltk.download('punkt')
print("✅ NLTK data downloaded successfully!")
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the application:"
echo ""
echo "1. Start the backend:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python app.py"
echo ""
echo "2. In a new terminal, open the frontend:"
echo "   cd frontend"
echo "   open index.html"
echo ""
echo "Happy analyzing! 🎉"
