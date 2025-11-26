"""AI-Powered Content Summarizer using Amazon Bedrock and Claude

A Streamlit application that provides intelligent content summarization
using AWS Bedrock and Claude AI models.
"""

import streamlit as st
import summarization_lib as glib

# Page configuration
st.set_page_config(
    page_title="AI Content Summarizer",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF9900;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .stButton>button {
        background-color: #FF9900;
        color: white;
        font-size: 1.1rem;
        padding: 0.5rem 2rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🤖 AI-Powered Content Summarizer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transform long documents into concise summaries using Amazon Bedrock & Claude</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📋 About")
    st.write("""
    This application uses Amazon Bedrock with Claude AI models to provide
    intelligent content summarization.
    
    **Features:**
    - Multiple file format support
    - Powered by Claude AI
    - Fast and accurate summaries
    - Easy to use interface
    """)
    
    st.header("🛠️ How to Use")
    st.write("""
    1. Upload a document (.txt, .pdf, or .docx)
    2. Click 'Generate Summary'
    3. Get your concise summary instantly!
    """)

# Main content area
col1, col2 = st.columns([3, 2])

with col1:
    st.header("📄 Input")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload your document",
        type=['txt', 'pdf', 'docx'],
        help="Supported formats: TXT, PDF, DOCX"
    )
    
    # Text input as alternative
    st.write("**Or paste your text directly:**")
    input_text = st.text_area(
        "Enter text to summarize",
        height=300,
        placeholder="Paste your content here..."
    )

with col2:
    st.header("⚙️ Options")
    
    summary_length = st.select_slider(
        "Summary Length",
        options=["Brief", "Moderate", "Detailed"],
        value="Moderate"
    )
    
    st.info("""
    **Brief**: Key points only
    
    **Moderate**: Balanced summary
    
    **Detailed**: Comprehensive overview
    """)

# Process button
if st.button("✨ Generate Summary", use_container_width=True):
    content_to_summarize = ""
    
    # Get content from file or text input
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            content_to_summarize = uploaded_file.read().decode("utf-8")
        else:
            st.warning("For demo purposes, please use .txt files or paste text directly.")
    elif input_text:
        content_to_summarize = input_text
    else:
        st.error("Please upload a file or enter text to summarize.")
        st.stop()
    
    if content_to_summarize:
        with st.spinner("🔄 Generating summary with Claude AI..."):
            try:
                # Call the summarization function
                summary = glib.get_text_summary(content_to_summarize)
                
                # Display results
                st.success("✅ Summary generated successfully!")
                
                st.header("📝 Summary")
                st.markdown("---")
                st.write(summary)
                
                # Stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Length", f"{len(content_to_summarize.split())} words")
                with col2:
                    st.metric("Summary Length", f"{len(summary.split())} words")
                with col3:
                    reduction = round((1 - len(summary.split())/len(content_to_summarize.split())) * 100, 1)
                    st.metric("Reduction", f"{reduction}%")
                
            except Exception as e:
                st.error(f"❌ Error generating summary: {str(e)}")
                st.write("Please check your AWS credentials and Bedrock access.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Built with ❤️ for AI for Bharat Workshop 1 | Powered by Amazon Bedrock & Claude</p>
    <p>© 2024 Priyansh Jain</p>
</div>
""", unsafe_allow_html=True)
