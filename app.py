import streamlit as st
import joblib
import pandas as pd
import numpy as np
import re
import requests
import base64
from io import BytesIO
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Valid8", page_icon="✔", layout="wide")

# -------------------- HIGH LEVEL UI (FIXED) --------------------
def inject_god_level_ui():
    st.markdown("""
    <style>

    /* ================================
       HIGH LEVEL AI SAAS UI ENGINE
       Designed By TAHA ALI – 2026 Edition
    ================================= */

    :root {
        --primary: #7f00ff;
        --secondary: #e100ff;
        --accent: #00f5ff;
        --neon: #ff00c8;
        --dark: #050510;
        --glass: rgba(255,255,255,0.06);
    }

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif !important;
        color: white !important;
        scroll-behavior: smooth;
    }

    /* Remove all extra lines / borders */
    hr, .stTabs [data-baseweb="tab-list"]::after, .stTabs [data-baseweb="tab-list"]::before {
        display: none !important;
    }

    /* Fix the glass card left clipping */
    .stMarkdown, .element-container {
        overflow: visible !important;
    }
    .glass-card-3d, .glass-card {
        margin-left: 0 !important;
        padding-left: 2rem !important;
        box-sizing: border-box !important;
        width: 100% !important;
    }

    div[data-testid="stAppViewContainer"] {
        background: linear-gradient(120deg,#0f0c29,#302b63,#24243e) !important;
        overflow-x: hidden;
    }

    /* Animated Cosmic Background */
    div[data-testid="stAppViewContainer"]::before {
        content:"";
        position:fixed;
        width:200%;
        height:200%;
        top:-50%;
        left:-50%;
        background:
        radial-gradient(circle at 30% 30%, rgba(127,0,255,0.4), transparent 40%),
        radial-gradient(circle at 70% 70%, rgba(0,245,255,0.4), transparent 40%);
        animation: cosmicRotate 40s linear infinite;
        z-index:-1;
    }

    @keyframes cosmicRotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* ULTRA 3D HEADER */
    .main-header {
        font-size: 4.5rem;
        font-weight: 900;
        text-align:center;
        background: linear-gradient(90deg,#fff,#a18cd1,#fbc2eb,#8fd3f4,#fff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: floatUltra 6s ease-in-out infinite, glowPulse 3s infinite;
        text-shadow:0 0 40px rgba(255,0,255,0.4);
    }

    @keyframes floatUltra {
        0% { transform: translateY(0px);}
        50% { transform: translateY(-15px);}
        100% { transform: translateY(0px);}
    }

    @keyframes glowPulse {
        0%,100% { filter: drop-shadow(0 0 20px var(--primary));}
        50% { filter: drop-shadow(0 0 40px var(--secondary));}
    }

    /* NEON GLASS CARDS */
    .glass-card-3d, .glass-card {
        background: var(--glass);
        backdrop-filter: blur(25px);
        border-radius: 40px;
        padding: 2rem !important;
        border:1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 40px rgba(127,0,255,0.3), 0 0 80px rgba(0,245,255,0.2);
        transition: all 0.6s cubic-bezier(.23,1,.32,1);
    }

    .glass-card-3d:hover, .glass-card:hover {
        transform: translateY(-15px) scale(1.03);
        box-shadow: 0 0 60px rgba(225,0,255,0.6), 0 0 120px rgba(0,245,255,0.5);
    }

    /* LIQUID BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg,var(--primary),var(--secondary));
        border:none;
        border-radius:60px;
        padding:1rem 2.5rem;
        font-weight:800;
        letter-spacing:1px;
        transition: all 0.4s ease;
        position:relative;
        overflow:hidden;
    }

    .stButton > button::before {
        content:"";
        position:absolute;
        width:200%;
        height:200%;
        top:-50%;
        left:-50%;
        background:linear-gradient(120deg,transparent,rgba(255,255,255,0.4),transparent);
        transform:rotate(25deg);
        animation: liquidMove 3s infinite linear;
    }

    @keyframes liquidMove {
        0% { transform:translateX(-100%) rotate(25deg);}
        100% { transform:translateX(100%) rotate(25deg);}
    }

    .stButton > button:hover {
        transform:scale(1.1);
        box-shadow:0 0 40px var(--neon);
    }

    /* PREMIUM TABS (No horizontal line) */
    div[data-testid="stTabs"] {
        margin-bottom: 0 !important;
    }
    div[data-testid="stTabs"] button {
        border-radius:50px !important;
        padding:0.7rem 2rem !important;
        font-weight:700 !important;
        background:rgba(255,255,255,0.05) !important;
        transition:all 0.4s ease !important;
        border: none !important;
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        background:linear-gradient(135deg,var(--primary),var(--secondary)) !important;
        box-shadow:0 0 30px var(--secondary);
        transform:scale(1.08);
    }

    /* PREDICTION EFFECT */
    .pred-valid {
        background:linear-gradient(135deg,#00ff99,#00cc66);
        padding:2rem;
        border-radius:40px;
        font-size:2.5rem;
        font-weight:900;
        text-align:center;
        animation: successPulse 2s infinite;
    }

    .pred-invalid {
        background:linear-gradient(135deg,#ff004c,#b3002d);
        padding:2rem;
        border-radius:40px;
        font-size:2.5rem;
        font-weight:900;
        text-align:center;
        animation: errorPulse 2s infinite;
    }

    @keyframes successPulse {
        0%,100% { box-shadow:0 0 20px #00ff99;}
        50% { box-shadow:0 0 60px #00ff99;}
    }

    @keyframes errorPulse {
        0%,100% { box-shadow:0 0 20px #ff004c;}
        50% { box-shadow:0 0 60px #ff004c;}
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar {
        width:10px;
    }
    ::-webkit-scrollbar-thumb {
        background:linear-gradient(var(--primary),var(--secondary));
        border-radius:5px;
    }

    /* Remove image preview border and extra spacing */
    .stImage {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

inject_god_level_ui()

# -------------------- FEATURE FUNCTIONS (Same as your training) --------------------
company_keywords = [
    r'sdn bhd', r'sdn.bhd', r'limited', r'ltd', r'enterprise',
    r'corporation', r'corp', r'trading', r'co\.', r'company'
]

def detect_company_fuzzy(text):
    text_lower = text.lower()
    for kw in company_keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
            return 1
    if re.search(r'\bson\b', text_lower) or re.search(r'\bs d n\b', text_lower):
        return 1
    return 0

def detect_date_fuzzy(text):
    patterns = [
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',
        r'\d{8}',
        r'\d{2}[-/]\d{2}[-/]\d{4}',
        r'\d{4}[-/]\d{1,2}[-/]\d{1,2}'
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return 1
    return 0

def detect_total_fuzzy(text):
    patterns = [
        r'(?:total|amount|grand total|balance|sum)[:\s]*[\d,]+\.\d{2}',
        r'(?:rm|myr|\$|rp)\s*[\d,]+\.\d{2}',
        r'\b\d+\.\d{2}\b'
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return 1
    return 0

def ocr_quality_score(text):
    if len(text) == 0: return 0
    readable = sum(c.isalnum() or c.isspace() for c in text)
    return readable / len(text)

def digit_ratio(text):
    if len(text) == 0: return 0
    return sum(c.isdigit() for c in text) / len(text)

def count_dates(text):
    return len(re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text))

def count_currency(text):
    return text.lower().count("rm") + text.lower().count("gst")

def line_count(text):
    return len(text.split("\n"))

def numeric_token_count(text):
    return len(re.findall(r"\d+\.?\d*", text))

def structure_score(text):
    score = 0
    t = text.lower()
    if "invoice" in t: score += 1
    if "total" in t: score += 1
    if "gst" in t: score += 1
    if len(text.split("\n")) > 8: score += 1
    return score

# -------------------- LOAD YOUR XGBOOST MODEL --------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("invoice_model.pkl")
    word_vec = joblib.load("word_vectorizer.pkl")
    char_vec = joblib.load("char_vectorizer.pkl")
    features = joblib.load("feature_columns.pkl")
    return model, word_vec, char_vec, features

model, word_vec, char_vec, feature_cols = load_artifacts()

def predict_invoice(text):
    has_company = detect_company_fuzzy(text)
    has_date = detect_date_fuzzy(text)
    has_total = detect_total_fuzzy(text)
    ocr_q = ocr_quality_score(text)
    dig_r = digit_ratio(text)
    txt_len = len(text)
    dt_c = count_dates(text)
    curr_c = count_currency(text)
    ln_c = line_count(text)
    num_c = numeric_token_count(text)
    struct_s = structure_score(text)

    extra_array = np.array([[ocr_q, dig_r, txt_len, dt_c, curr_c, ln_c, num_c, struct_s]])
    from scipy.sparse import hstack, csr_matrix
    extra_sparse = csr_matrix(extra_array)
    X_word = word_vec.transform([text])
    X_char = char_vec.transform([text])
    X_final = hstack([X_word, X_char, extra_sparse])

    prob = model.predict_proba(X_final)[0][1]
    pred = model.predict(X_final)[0]

    # Override for missing company
    if not has_company:
        pred = 0
        prob = 0.0
    elif has_company and has_date and has_total:
        pred = 1
        prob = max(prob, 0.85)
    return pred, prob

# -------------------- GROQ TEXT EXTRACTION --------------------
GROQ_API_KEY = st.secrets["GROQ_API_KEY"] 
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def extract_text_with_groq(image_base64):
    prompt = "Extract all visible text from this invoice. Preserve line breaks as much as possible. Do not add any extra text."
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.3-70b-versatile",
        # "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}]}],
        "max_tokens": 2048,
        "temperature": 0.0
    }
    try:
        response = requests.post(GROQ_URL, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"ERROR: {response.status_code} - {response.text}"
    except Exception as e:
        return f"ERROR: {str(e)}"

# -------------------- UI (Only two tabs, no image preview) --------------------
st.markdown("<h1 class='main-header'>✔ Valid8</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #aaa;'>Instant Invoice Verification with AI</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🤖 Upload & AI Extract", "📝 Manual Text Entry"])

# ---------- TAB 1: GROQ + XGBoost (No image preview) ----------
with tab1:
    # st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    if GROQ_API_KEY == "YOUR_GROQ_API_KEY_HERE":
        st.warning("⚠️ Please set your free GROQ API key in the code (console.groq.com).")
        st.info("Until then, use the **Manual Text Entry** tab.")
    else:
        uploaded = st.file_uploader("Upload invoice image", type=['jpg','png','jpeg'])
        if uploaded:
            # Show just file name, no image preview
            st.success(f"📎 Selected: {uploaded.name}")
            if st.button("🚀 Extract & Classify", type="primary"):
                with st.spinner("Step 1: GROQ extracting text from image..."):
                    buffered = BytesIO()
                    image = Image.open(uploaded)
                    image.save(buffered, format="JPEG", quality=80)
                    img_b64 = base64.b64encode(buffered.getvalue()).decode()
                    extracted = extract_text_with_groq(img_b64)
                    if extracted.startswith("ERROR"):
                        st.error(f"GROQ failed: {extracted}")
                        st.info("💡 Please use the **Manual Text Entry** tab or check your API key/model name.")
                    else:
                        st.text_area("📄 Extracted Text (GROQ)", extracted, height=200)
                        with st.spinner("Step 2: Running your XGBoost model..."):
                            pred, prob = predict_invoice(extracted)
                        col1, col2 = st.columns(2)
                        col1.metric("Model Confidence", f"{prob:.2%}")
                        if pred == 1:
                            col2.markdown("<div class='pred-valid'>✅ VALID INVOICE</div>", unsafe_allow_html=True)
                        else:
                            col2.markdown("<div class='pred-invalid'>❌ INVALID INVOICE</div>", unsafe_allow_html=True)
                        with st.expander("🔍 Feature Detection Details"):
                            st.json({
                                "Company found": detect_company_fuzzy(extracted),
                                "Date found": detect_date_fuzzy(extracted),
                                "Total found": detect_total_fuzzy(extracted),
                                "OCR Quality": round(ocr_quality_score(extracted), 3)
                            })
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- TAB 2: Manual Text (Fallback) ----------
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    manual_text = st.text_area("Paste invoice text here (no OCR needed):", height=250)
    if st.button("Classify Text", type="primary"):
        if manual_text.strip():
            pred, prob = predict_invoice(manual_text)
            col1, col2 = st.columns(2)
            col1.metric("Confidence", f"{prob:.2%}")
            if pred == 1:
                col2.markdown("<div class='pred-valid'>✅ VALID INVOICE</div>", unsafe_allow_html=True)
            else:
                col2.markdown("<div class='pred-invalid'>❌ INVALID INVOICE</div>", unsafe_allow_html=True)
            with st.expander("Details"):
                st.json({
                    "Company present": bool(detect_company_fuzzy(manual_text)),
                    "Date present": bool(detect_date_fuzzy(manual_text)),
                    "Total present": bool(detect_total_fuzzy(manual_text))
                })
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; margin-top:2rem;'>Built by TAHA ALI | GROQ Vision + XGBoost</p>", unsafe_allow_html=True)
