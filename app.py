import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Universal Offer Letter Generator",page_icon="🔍")
st.title("Company Offer Letter Generator")

# --- Form Inputs ---
with st.form("offer_form"):
    company_name = st.text_input("Company Name", "ABC Tech Pvt. Ltd.")
    company_tagline = st.text_input("Company Tagline", "Data & AI Solutions")
    company_email = st.text_input("Company Email", "support@company.com")
    company_signature = st.text_input("Signature Authority Name", "Rohan Rai")
    designation = st.text_input("Designation of Authority", "Founder & CEO")

    intern_name = st.text_input("Intern's Full Name")
    intern_email = st.text_input("Intern's Email")
    position = st.text_input("Internship Position", "Data Science Intern")
    start_date = st.date_input("Start Date")
    duration = st.text_input("Duration (e.g., 3 Months)")
    working_hours = st.text_input("Working Hours", "10-15 hours/week")
    stipend = st.text_input("Stipend", "Unpaid")
    manager = st.text_input("Reporting Manager", "Team Lead")

    submitted = st.form_submit_button("Generate Offer Letter")

if submitted:
    today = datetime.today().strftime('%d-%m-%Y')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, company_name, ln=True, align='C')
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, company_tagline, ln=True, align='C')
    pdf.cell(0, 8, f"Email: {company_email}", ln=True, align='C')
    pdf.ln(8)
    pdf.cell(0, 8, f"Date: {today}", ln=True, align='R')
    pdf.ln(5)

    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Internship Offer Letter", ln=True)
    pdf.ln(5)

    # Body
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"To,\n{intern_name}\n{intern_email}\n")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Subject: Internship Offer Letter at {company_name}", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8,
        f"Dear {intern_name.split()[0]},\n\n"
        f"We are pleased to offer you the position of {position} at {company_name}, "
        "a company focused on innovation and professional growth. "
        "This internship provides a great opportunity for you to enhance your skills and gain real-world experience.\n"
    )

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Internship Details:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8,
        f"- Position: {position}\n"
        f"- Start Date: {start_date.strftime('%d-%m-%Y')}\n"
        f"- Duration: {duration}\n"
        f"- Mode: Remote\n"
        f"- Working Hours: {working_hours}\n"
        f"- Stipend: {stipend}\n"
        f"- Reporting Manager: {manager}\n"
    )

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Responsibilities:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8,
        "- Assist in project work and assigned tasks.\n"
        "- Participate in discussions and regular meetings.\n"
        "- Learn and apply new tools/technologies.\n"
        "- Contribute to documentation and delivery.\n"
    )

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Terms & Conditions:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8,
        "- Maintain confidentiality of all company data.\n"
        "- Demonstrate professionalism and commitment.\n"
        "- Company reserves the right to terminate internship if expectations are not met.\n"
    )

    pdf.multi_cell(0, 8,
        "Upon successful completion, you will be provided with an Internship Completion Certificate "
        "and a Letter of Recommendation based on your performance.\n\n"
        "We look forward to having you as part of our team."
    )

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Warm regards,", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8,
        f"{company_signature}\n{designation}\n{company_name}\n{company_email}\n"
    )

    file_name = f"{intern_name.replace(' ', '_')}_Offer_Letter.pdf"
    pdf.output(file_name)

    with open(file_name, "rb") as f:
        st.download_button("📥 Download Offer Letter PDF", f, file_name=file_name)


st.markdown("---")
st.markdown("<center>Built ❤️ by <strong>Rohan Rai</strong></center>", unsafe_allow_html=True)
