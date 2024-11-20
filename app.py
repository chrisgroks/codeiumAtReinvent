import streamlit as st

# Page config
st.set_page_config(
    page_title="Codeium at AWS Re:Invent! ",
    page_icon="",
    layout="wide"
)

# Custom CSS with complete light theme
st.markdown("""
<style>
    /* Global theme override */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    /* Override Streamlit's default dark backgrounds */
    .main {
        background: transparent !important;
    }
    
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: 0 auto;
        background: transparent !important;
    }

    /* Make all text elements light-themed */
    .stMarkdown, .stText, p, span {
        color: #334155 !important;
    }

    /* Metrics styling with updated colors */
    [data-testid="stMetricLabel"] {
        display: flex;
        justify-content: center;
        width: 100%;
        color: #334155 !important;
    }

    [data-testid="stMetricLabel"] > div {
        text-align: center !important;
        width: 100% !important;
    }

    [data-testid="stMetricValue"] {
        display: flex;
        justify-content: center;
        width: 100%;
        color: #1e293b !important;
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
        background: white !important;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }

    .stMetric > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    /* Typography with updated colors */
    h1 { 
        font-size: 3rem !important;
        margin-bottom: 1.5rem !important;
        color: #1e293b !important;
    }
    h2, h3 {
        margin: 2rem 0 !important;
        color: #334155 !important;
    }

    /* Updated gradient text */
    .highlight { 
        background: linear-gradient(120deg, #0ea5e9 0%, #2563eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    /* Calendar iframe with updated styling */
    .calendar-wrapper {
        width: 100%;
        max-width: 1000px;
        margin: 2rem auto;
        padding: 1rem;
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }
    iframe {
        border-radius: 8px;
        background: white;
        width: 100%;
    }

    /* Topic cards with updated styling */
    .stAlert {
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        background: white !important;
        color: #334155 !important;
    }

    /* Override any remaining dark theme elements */
    button[kind="primary"] {
        background-color: #2563eb !important;
        color: white !important;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
        color: white !important;
    }
    .stProgress > div > div > div {
        background-color: #2563eb !important;
    }
    
    /* Description text styling */
    .description {
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 1.5rem auto 2.5rem;
        max-width: 800px;
        color: #475569 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center'><span class='highlight'>Codeium</span> at AWS Re:Invent 2024! </h1>", unsafe_allow_html=True)

# Create two columns for content and image
content_col, img_col = st.columns([3, 2])

with content_col:
    st.markdown("""
    <div class='description'>
        Meet with Chris at Re:Invent! Learn how Codeium's AI-powered coding assistant can supercharge your development team's productivity.
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics in the content column
    st.metric("Developer Productivity", "↑ 30%", "Boost in output")
    st.metric("Developer Happiness", "↑ 9001%", "IT'S OVER 9000!!!")
    st.metric("Coffee Consumed", "↓ 60%", "Less caffeine needed!")

with img_col:
    st.image("hoodwinkt_animated_anime_cartoon_monsters_destroying_buildings__46c8d3fc-7175-4c0e-b495-d5522951f726.png", 
            use_container_width=True)

# Calendar section
st.markdown("<h2 style='text-align: center; margin-top: 3rem;'>Schedule a Meeting</h2>", unsafe_allow_html=True)

# Embedded calendar
st.markdown("""
<div class="calendar-wrapper">
    <iframe src="https://calendar.google.com/calendar/appointments/schedules/AcZssZ3ogWZM7q0XNbtOii42H8269xmwhBELYjPqUpWc9dXW5QRVgIgK_LT6aj5Sqd2pdfBJ5CeJP9z4?gv=true" 
            style="border: 0; height: 600px;" 
            frameborder="0">
    </iframe>
</div>
""", unsafe_allow_html=True)
