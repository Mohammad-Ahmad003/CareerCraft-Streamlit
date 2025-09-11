import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space as avs

import google.generativeai as genai
import PyPDF2
from PIL import Image

#  Page settings
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")
avs(4)

#  API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


# ---------- Helper Functions ----------
def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text


# ---------- Prompt Template ----------
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encopassing Software Engineering,
Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning engineer, 
Cybersecurity analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, 
Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess
resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch 
guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify 
any missing keywords with utmost accuracy.

resume: {text}
description: {jd}

I want the response in the following structure:
1️⃣ Percentage match with the job description (JD)  
2️⃣ Missing keywords  
3️⃣ Profile summary  

Mention the title for all three sections. Add spacing between sections.
"""

# ---------- UI Layout ----------
col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""<p style='text-align: justify;'>
                Introducing CareerCraft, an ATS-optimized Resume analyzer - your ultimate solution for optimizing
                job applications and accelerating career growth. Our innovative platform leverages advanced ATS
                technology to provide job seekers with valuable insights into their resumes' compatibility with 
                job descriptions. From resume optimization and skill enhancement to career progression guidance,
                CareerCraft empowers users to stand out in today's competitive job market.
                </p>""", unsafe_allow_html=True)

with col2:
    st.image("Images/Screenshot 2024-06-23 230719.png", use_container_width=True)

avs(10)

col1, col2 = st.columns([3, 2])
with col2:
    st.header("Wide Range of Offerings")
    st.write('• ATS-Optimized Resume Analysis')
    st.write('• Resume Optimization')
    st.write('• Skill Enhancement')
    st.write('• Career Progression Guidance')
    st.write('• Tailored Profile Summaries')
    st.write('• Streamlined Application Process')
    st.write('• Personal Recommendations')
    st.write('• Efficient Career Navigation')

with col1:
    img1 = Image.open("Images/Screenshot 2024-06-23 230346.png")
    st.image(img1, use_container_width=True)

avs(10)

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF")

    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))
            st.subheader(response)

with col2:
    img2 = Image.open("Images/Screenshot 2024-06-23 230326.png")
    st.image(img2, use_container_width=True)

avs(10)

col1, col2 = st.columns([2, 3])
with col2:
    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
    st.write("**Q:** How does CareerCraft analyze resumes and job descriptions?")
    st.write(
        "**A:** CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility.")

    avs(3)

    st.write("**Q:** Can CareerCraft suggest improvements for my resume?")
    st.write(
        "**A:** Yes, CareerCraft provides personalized recommendations to optimize your resume, including suggestions for missing keywords and alignment with desired job roles.")

    avs(3)

    st.write("**Q:** Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write(
        "**A:** Absolutely! CareerCraft caters to job seekers at all stages, offering tailored insights and guidance to enhance resumes and advance careers.")

with col1:
    img3 = Image.open("Images/Screenshot 2024-06-23 230304.png")
    st.image(img3, use_container_width=True)
