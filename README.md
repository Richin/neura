# 🕵️‍♂️ DeepTruth – AI That Digs Deep for the Truth!

An AI-powered fact-checking and content verification system that helps users identify misinformation and assess content credibility in real-time.

## 🌟 Key Features

- **Real-Time Fact-Checking** – Instantly analyzes and verifies content
- **Website Credibility Scoring** – Assigns trust scores based on historical accuracy
- **Misinformation Detection** – Flags misleading or manipulated news
- **Deep Context Analysis** – Examines bias, tone, and source reliability
- **Explainable AI** – Clearly explains why a website or content is trustworthy (or not)

## 🚀 How It Works

1. **Enter a Website URL or Paste Content** – DeepTruth scans the content in real-time
2. **AI-Powered Analysis** – Evaluates sources, context, bias, and credibility
3. **Get Instant Results** – Displays a Trust Score and a detailed breakdown
4. **Stay Safe Online!** – Make informed decisions before trusting or sharing news

## 🌐 Integration Options

### Browser Extension
Our lightweight extension works with Chrome, Firefox, and Edge, offering:
- One-click analysis of articles, blogs, and news sites
- Direct in-browser fact-checking without leaving the page
- Color-coded trust scores highlighting potential misinformation

## 👥 Who Can Use DeepTruth?

### 📰 Journalists & Fact-Checkers
- Verify sources before publishing news
- Detect bias and misinformation in articles
- Ensure accuracy in investigative reporting

### 🏢 Businesses & Organizations
- Protect brand reputation by avoiding false claims
- Monitor online mentions and PR statements
- Ensure corporate communication is backed by credible sources

### 🏫 Educators & Students
- Fact-check research papers and academic sources
- Teach media literacy and critical thinking
- Detect AI-generated or misleading content in essays

### 📢 Social Media Users & Content Creators
- Verify news before sharing on social media
- Detect clickbait, deepfakes, and manipulated content
- Protect your audience from spreading misinformation

### 🏛 Government & Policy Makers
- Monitor and counter disinformation campaigns
- Ensure public communications are based on factual data
- Strengthen national security against cyber misinformation

### 🔎 Cybersecurity & Researchers
- Identify suspicious or fraudulent websites
- Detect AI-generated or manipulated news content
- Protect against misinformation-driven cyber threats

## 🔗 Getting Started

DeepTruth helps **anyone** navigate the internet **safely and responsibly**. Whether you're a journalist, student, researcher, or just someone who wants the **truth**, this tool is for you.



## 🛠️ Installation & Setup

### Prerequisites
1. **Python 3.8+**
   ```bash
   # Check your Python version
   python --version
   ```

2. **Ollama with DeepSeek Model**
   ```bash
   # Install Ollama (if not already installed)
   curl -fsSL https://ollama.com/install.sh | sh
   
   # Pull the DeepSeek model
   ollama pull deepseek
   ```

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/richin/neura.git
   cd neura/neura-chat
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```
   The application will open in your default web browser at `http://localhost:8501`

### Troubleshooting
- If you encounter any issues with Ollama, ensure the service is running:
  ```bash
  ollama serve
  ```
- For dependency issues, try creating a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

#StayInformed #DeepTruth #FactChecking #AIForGood 🚀