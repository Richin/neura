import streamlit as st
import requests
import trafilatura
import whois
import tldextract
import json
import time
from urllib.parse import urlparse

# Hide Streamlit menu & footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True
)

# 🔹 Ollama API (Running DeepSeek Locally)
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-r1:1.5b"

# ✅ Function: Scrape Website Content
def scrape_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        extracted_content = trafilatura.extract(response.text)
        return extracted_content or "No readable content found."
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {str(e)}"

# ✅ Function: Check Domain Reputation (WHOIS Lookup)
def check_domain_reputation(url):
    try:
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"
        domain_info = whois.whois(domain)
        
        creation_date = domain_info.creation_date if domain_info.creation_date else "Unknown"
        registrar = domain_info.registrar if domain_info.registrar else "Unknown"
        
        return f"🔹 **Domain Age**: {creation_date}\n🔹 **Registrar**: {registrar}"
    except Exception:
        return "⚠️ Unable to retrieve domain information."

# ✅ Function: Check Google Safe Browsing (Blacklist Status)
def check_blacklist(url):
    safe_browsing_url = f"https://transparencyreport.google.com/safe-browsing/search?url={url}"
    return f"[🔍 Check Google Safe Browsing]({safe_browsing_url})"

# ✅ Function: AI Analysis for Fake News Detection
def analyze_content(content, url=None):
    prompt = f"""
    Analyze the following news article for misinformation, bias, and credibility.
    - Assign a **trust score (0-100)** where 100 is highly trustworthy.
    - Highlight **potential fake news, bias, or manipulation**.
    - Identify **key sources, tones, and any misleading elements**.
    - If URL is provided, compare with historical reliability data.

    {"URL: " + url if url else ""}
    {content[:8000]}
    """
    
    try:
        response = requests.post(OLLAMA_API, json={"model": MODEL_NAME, "prompt": prompt, "stream": False})
        response_data = response.json()
        return response_data.get("response", "⚠️ No analysis generated.")
    except requests.exceptions.RequestException as e:
        return f"❌ AI Analysis Error: {str(e)}"

# ✅ Function: Website Credibility Scoring
def get_website_trust_score(content):
    prompt = f"Evaluate the credibility of the website content below and assign a trust score (0-100). Explain the rating.\n\n{content[:8000]}"
    
    try:
        response = requests.post(OLLAMA_API, json={"model": MODEL_NAME, "prompt": prompt, "stream": False})
        response_data = response.json()
        return response_data.get("response", "⚠️ No score generated.")
    except requests.exceptions.RequestException as e:
        return f"❌ Trust Score Error: {str(e)}"

# ✅ Streamlit UI
st.title("🕵️‍♂️ DeepTruth – AI that digs deep for the truth.")
st.markdown("### 🔍 AI That Scans, Scores & Verifies Websites or Content Instantly")

# Option Selection: URL vs. Text Input
option = st.radio("Choose input method:", ["🌍 Website URL", "📝 Paste Content"])

if option == "🌍 Website URL":
    url = st.text_input("🔗 Enter Website URL")
    
    if st.button("Check Website"):
        if not url or not urlparse(url).scheme:
            st.error("⚠️ Please enter a valid URL (include http:// or https://)")
            st.stop()

        st.info("🔄 Scraping website content...")
        content = scrape_website(url)
        
        if "Error" in content:
            st.error(content)
            st.stop()

        st.success("✅ Website content extracted! Analyzing trustworthiness...")

        # Check reputation
        reputation = check_domain_reputation(url)
        blacklist_status = check_blacklist(url)

        # AI Analysis
        trust_analysis = analyze_content(content, url)
        trust_score = get_website_trust_score(content)

        # Display Results
        st.subheader("📌 Website Trustworthiness Report")
        st.markdown(f"""
        **🔗 URL:** {url}  
        {reputation}  
        {blacklist_status}  
        """)

        st.subheader("🧐 AI Analysis")
        st.markdown(f"""
        <div style="padding: 15px; background-color: #e8f0ff; border-radius: 10px; font-size: 16px;">
            {trust_analysis}
        </div>
        """, unsafe_allow_html=True)

        st.subheader("📊 Credibility Score")
        st.markdown(f"""
        <div style="padding: 15px; background-color: #d4edda; border-radius: 10px; font-size: 18px; font-weight: bold;">
            {trust_score}
        </div>
        """, unsafe_allow_html=True)

elif option == "📝 Paste Content":
    text_content = st.text_area("📜 Paste the content here:")
    
    if st.button("Analyze Content"):
        if not text_content.strip():
            st.error("⚠️ Please enter content to analyze.")
            st.stop()

        st.success("✅ Analyzing content for misinformation...")
        trust_analysis = analyze_content(text_content)
        trust_score = get_website_trust_score(text_content)

        st.subheader("🧐 AI Content Analysis")
        st.markdown(f"""
        <div style="padding: 15px; background-color: #e8f0ff; border-radius: 10px; font-size: 16px;">
            {trust_analysis}
        </div>
        """, unsafe_allow_html=True)

        st.subheader("📊 Credibility Score")
        st.markdown(f"""
        <div style="padding: 15px; background-color: #d4edda; border-radius: 10px; font-size: 18px; font-weight: bold;">
            {trust_score}
        </div>
        """, unsafe_allow_html=True)
