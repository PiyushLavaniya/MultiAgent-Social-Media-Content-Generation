__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
from crewai import LLM
from crew import create_crew

# Streamlit Page Configuration
st.set_page_config(page_title="Social Media Post Generator", page_icon="🚀", layout="centered")

# App Title
st.title("📱 Social Media Post Generator")

# Cloud Provider Selection
provider = st.selectbox("Select Cloud Provider", ["OpenAI", "Anthropic", "GROQ", 'Google'])

# API Key Input (only shown when provider is selected)
api_key = st.text_input(f"Enter your {provider} API Key", type="password")

# User Inputs
platform = st.selectbox("Select Social Media Platform", ["LinkedIn", "Twitter", "Instagram", "Facebook"])
industry = st.text_input("Enter your Industry", placeholder="e.g., AI Technology, Healthcare, Finance")
company_info = st.text_area("Company Information", placeholder="Describe your company...")
product_info = st.text_area("Product Information", placeholder="Describe your product...")

# Generate Post Button
if st.button("🚀 Generate Post"):
    if not api_key:
        st.warning("⚠️ Please enter your API key.")
    elif not industry or not company_info or not product_info:
        st.warning("⚠️ Please fill in all fields before generating the post.")
    else:
        try:
            # Set up the LLM based on user selection
            if provider == "OpenAI":
                llm = LLM(model="openai/gpt-4o", api_key=api_key)
            elif provider == "Anthropic":
                llm = LLM(
                model="anthropic/claude-3-5-sonnet-20241022",
                temperature=0.7
                )
            elif provider == "GROQ":
                llm = LLM(
                    api_key=api_key,
                    model="groq/llama-3.3-70b-versatile",
                    temperature=0.7
                )
            elif provider == "Google":
                    llm = LLM(
                    model="gemini/gemini-1.5-flash",
                    temperature=0.7,
                    api_key=api_key               )

            else:
                st.error("❌ Invalid provider selected.")
                st.stop()

            # Create Crew and Generate Post
            crew = create_crew(platform, industry, company_info, product_info, llm)
            result = crew.kickoff()

            # Display the result
            st.subheader("🎯 Generated Post:")
            st.markdown(result, unsafe_allow_html=True)

        except ValueError as e:
            st.error(f"❌ Error: {e}")
