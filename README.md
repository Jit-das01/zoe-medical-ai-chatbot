# 🤖 MediBot - AI Medical Assistant

An intelligent medical chatbot powered by GPT-3.5, designed to provide general health information, symptom guidance, and help users understand when to seek professional medical care.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![React](https://img.shields.io/badge/React-18-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange)

## ✨ Features

### 🧠 **Intelligent Conversation**
- Natural language understanding of symptoms
- Context-aware responses based on chat history
- Multi-turn dialogue support
- Empathetic and supportive tone

### ⚠️ **Emergency Detection**
- Automatic detection of urgent symptoms
- Red flag alerts for serious conditions
- Immediate guidance to seek emergency care
- Keywords: chest pain, difficulty breathing, severe bleeding, etc.

### 💬 **User-Friendly Interface**
- Clean, modern chat UI
- Real-time typing indicators
- Quick action prompts for common questions
- Chat history tracking
- Responsive design

### 🎯 **Medical Accuracy**
- GPT-3.5-turbo powered responses
- Evidence-based information
- Clear disclaimers
- Always recommends professional consultation

## 🏗️ Architecture

```
medibot/
├── backend/
│   ├── app.py              # FastAPI server
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
└── frontend/
    └── index.html         # React chat interface
```

### **Tech Stack:**

**Backend:**
- FastAPI (modern Python web framework)
- OpenAI API (GPT-3.5-turbo)
- Pydantic (data validation)
- Python 3.10+

**Frontend:**
- React 18 (via CDN)
- Vanilla CSS
- Fetch API

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Modern web browser

### **Step 1: Clone/Download**
```bash
# Download the project files to your Desktop
cd ~/Desktop
mkdir medibot
cd medibot
```

### **Step 2: Set Up Backend**

```bash
cd backend

# Install dependencies
pip3 install -r requirements.txt

# Create .env file with your OpenAI API key
cat > .env << 'EOF'
OPENAI_API_KEY=your-api-key-here
EOF

# Edit .env and add your actual API key
nano .env  # or use any text editor
```

**Get OpenAI API Key:**
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with sk-...)
5. Paste it in .env file

### **Step 3: Run Backend**

```bash
python3 app.py
```

You should see:
```
🤖 MediBot API starting...
📍 API will be available at: http://localhost:8000
📚 Docs available at: http://localhost:8000/docs
```

### **Step 4: Open Frontend**

In a new terminal:
```bash
cd ../frontend
open index.html
```

Or just double-click `index.html`!

---

## 💡 How to Use

### **Starting a Conversation**

1. **Try Quick Actions** - Click on pre-written prompts
2. **Ask About Symptoms** - "I have a headache for 3 days"
3. **General Health Questions** - "What are symptoms of flu?"
4. **Emergency Help** - "I have chest pain" (triggers red alert)

### **Example Conversations:**

**Normal Query:**
```
You: I have a mild headache and feel tired
Bot: I understand you're experiencing a headache and fatigue. Let me help...
     
     Common causes:
     • Dehydration
     • Lack of sleep
     • Stress
     • Eye strain
     
     Recommendations:
     • Drink plenty of water
     • Rest in a dark, quiet room
     • Take over-the-counter pain relief if needed
     
     When to see a doctor:
     • If headache persists >3 days
     • If pain becomes severe
     • If accompanied by fever, vision changes, or stiff neck
     
     ⚠️ Disclaimer: This is general information...
```

**Emergency Query:**
```
You: I have severe chest pain
Bot: [Response about seeking immediate care]

🚨 EMERGENCY DETECTED
• Call emergency services (911/108) immediately
• Do not drive yourself to the hospital
• Stay calm and wait for help
```

---

## 📊 API Endpoints

### **Health Check**
```bash
GET /api/health
```

### **Chat**
```bash
POST /api/chat
Content-Type: application/json

{
  "message": "I have a headache",
  "session_id": "session_123" # optional
}
```

Response:
```json
{
  "response": "Bot's response...",
  "session_id": "session_123",
  "is_emergency": false,
  "suggested_actions": [...],
  "timestamp": "2026-03-22T14:30:00"
}
```

### **Get Chat History**
```bash
GET /api/history/{session_id}
```

### **Clear History**
```bash
DELETE /api/history/{session_id}
```

### **List Sessions**
```bash
GET /api/sessions
```

---

## 🎓 What I Learned

Building this project taught me:
- **OpenAI API Integration** - Using GPT-3.5 for conversational AI
- **FastAPI Development** - Building modern Python APIs
- **Medical AI Ethics** - Responsible AI design, disclaimers, emergency detection
- **Chat Systems** - Session management, history tracking
- **Full-Stack Integration** - React + Python backend
- **Error Handling** - Graceful failure management
- **User Experience** - Designing empathetic, helpful interfaces

---

## 🔮 Future Enhancements

### **Phase 2: RAG Integration**
- [ ] Add vector database (ChromaDB/Pinecone)
- [ ] Index medical textbooks and documentation
- [ ] Context-aware responses from knowledge base
- [ ] Citation of medical sources

### **Phase 3: Advanced Features**
- [ ] Symptom checker with decision trees
- [ ] Drug interaction checker
- [ ] Multilingual support (Hindi, Spanish, etc.)
- [ ] Voice input/output
- [ ] PDF report generation
- [ ] Chat export functionality

### **Phase 4: Production**
- [ ] User authentication
- [ ] Database for persistent chat history (PostgreSQL)
- [ ] Rate limiting
- [ ] Caching for common queries
- [ ] Deploy to cloud (Railway/Render)
- [ ] HIPAA compliance considerations

---

## 🚨 Important Disclaimers

### **Medical Disclaimer**
MediBot is designed for educational and informational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment.

- Always seek the advice of a qualified healthcare provider
- Never disregard professional medical advice
- Do not delay seeking medical care based on chatbot information
- In case of emergency, call 911 (US) or 108 (India)

### **Limitations**
- Cannot diagnose medical conditions
- Cannot prescribe medications
- Not suitable for emergency situations
- Information may not be complete or current
- Should not be used for critical health decisions

---

## 🐛 Troubleshooting

### **"Connection refused" error**
- Make sure backend is running on port 8000
- Check: `curl http://localhost:8000/api/health`

### **"Invalid API key" error**
- Verify your OpenAI API key in .env file
- Make sure it starts with `sk-`
- Check you have credits in your OpenAI account

### **Backend won't start**
- Install all dependencies: `pip3 install -r requirements.txt`
- Check Python version: `python3 --version` (needs 3.10+)

### **Slow responses**
- Normal! GPT-3.5 takes 2-5 seconds to respond
- Consider upgrading to GPT-4 for better quality (slower and more expensive)

---

## 💰 Cost Estimation

### **OpenAI API Costs:**
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- Average conversation (20 messages): ~$0.01-0.02
- 1000 conversations: ~$10-20

### **Free Tier:**
- OpenAI gives $5 free credits for new accounts
- Good for ~250-500 test conversations

---

## 📄 License

MIT License - Free to use and modify!

---

## 👨‍💻 Author

**Jit Das** - 3rd Year CS Student

- GitHub: [@Jit-das01](https://github.com/Jit-das01)
- LinkedIn: [Your LinkedIn]
- Projects:
  - GitHub Analytics Dashboard
  - SentimentScope (NLP)
  - MediBot (Medical AI) ← You are here!

---

## 🙏 Acknowledgments

- OpenAI for GPT-3.5 API
- FastAPI team for amazing framework
- React team
- Medical community for open health information

---

⭐ **If you find this project useful, please give it a star on GitHub!** ⭐

**Built with ❤️ using Python, React, and OpenAI GPT-3.5**

---

## 📸 Screenshots

### Main Chat Interface
![Chat Interface](screenshots/chat.png)

### Emergency Detection
![Emergency Alert](screenshots/emergency.png)

### Quick Actions
![Quick Actions](screenshots/quick-actions.png)
