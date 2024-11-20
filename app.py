import streamlit as st

# Page config
st.set_page_config(
    page_title="Meet at AWS Re:Invent! 🚀",
    page_icon="🤝",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    /* Center content and add max-width */
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: 0 auto;
    }

    /* Metrics styling */
    [data-testid="stMetricLabel"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    [data-testid="stMetricLabel"] > div {
        text-align: center !important;
        width: 100% !important;
    }

    [data-testid="stMetricValue"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    [data-testid="stMetricValue"] > div {
        display: flex;
        justify-content: center;
        width: 100%;
        font-size: 32px !important;
    }

    [data-testid="stMetricDelta"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    [data-testid="stMetricDelta"] > div {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* Force center alignment for metric elements */
    .stMetric {
        text-align: center !important;
    }

    .stMetric > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    /* Typography */
    h1 { 
        font-size: 3rem !important;
        margin-bottom: 1.5rem !important;
    }
    h2, h3 {
        margin: 2rem 0 !important;
    }

    /* Gradient text */
    .highlight { 
        background: linear-gradient(120deg, #6366f1 0%, #4f46e5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Calendar iframe */
    .calendar-wrapper {
        width: 100%;
        max-width: 1000px;
        margin: 2rem auto;
    }
    iframe {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        background: white;
        width: 100%;
    }

    /* Topic cards */
    .stAlert {
        border-radius: 10px;
        margin: 0.5rem 0;
    }

    /* Column styling */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 0 1rem;
    }

    /* Bullet points */
    .metrics-list {
        text-align: left;
        width: fit-content;
        margin: 1rem auto;
    }

    .metrics-list ul {
        margin: 0;
        padding-left: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Add container for better centering
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>Let's Chat at <span class='highlight'>AWS Re:Invent</span>! 🤝</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 1.2rem; margin: 1rem 0 3rem;'>
    Join me to discuss the future of AI-powered development with Codeium - 
    where coding meets intelligence! ✨
</p>
""", unsafe_allow_html=True)

# Benefits section with metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Developer Productivity", "↑ 30%", "vs traditional coding")
    st.markdown("""
    <div class="metrics-list">
    <ul>
        <li>Real-time code completions</li>
        <li>Smart code suggestions</li>
        <li>Context-aware assistance</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.metric("Developer Happiness", "↑ 9001%", "IT'S OVER 9000!!!")
    st.markdown("""
    <div class="metrics-list">
    <ul>
        <li>Less time debugging</li>
        <li>More time creating</li>
        <li>Reduced cognitive load</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.metric("Coffee Consumed", "↓ 60%", "Less caffeine needed!")
    st.markdown("""
    <div class="metrics-list">
    <ul>
        <li>Better code quality</li>
        <li>Fewer late nights</li>
        <li>More balanced workday</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Topics we can discuss
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>Topics We Can Discuss 💡</h3>", unsafe_allow_html=True)

topics = st.columns(4)
with topics[0]:
    st.info("🤖 AI Coding Assistants")
with topics[1]:
    st.success("⚡ Codeium Features")
with topics[2]:
    st.warning("🚀 Developer Productivity")
with topics[3]:
    st.error("💻 Future of Development")

# Calendar section
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Schedule a Meeting 📅</h2>", unsafe_allow_html=True)

# Embedded Calendar
st.markdown("""
<div class="calendar-wrapper">
    <iframe src="https://calendar.google.com/calendar/appointments/schedules/AcZssZ3ogWZM7q0XNbtOii42H8269xmwhBELYjPqUpWc9dXW5QRVgIgK_LT6aj5Sqd2pdfBJ5CeJP9z4?gv=true" 
            style="border: 0; height: 600px;" 
            frameborder="0">
    </iframe>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
