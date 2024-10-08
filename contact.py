import streamlit as st
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def show_contacts():
    st.title("Interact with us")
    st.warning('We want to hear from you, send us a mail or contact via whatssap and we will be in touch with you ASAP!')
    # Formulario de contacto
    with st.form(key='contact_form'):
        contact_reason = st.selectbox("Reason for contact:", ["Project Inquiry", "Employment", "Tutoring", "General Information"])
        contact_info = st.text_input("Your contact info (WhatsApp or email):")
        message = st.text_area("Your message:")
        
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            # Enviar el correo electrónico
            email_recipient = "jjusturi@gmail.com"
            email_subject = f"Contact Form Submission: {contact_reason}"
            email_body = f"Reason: {contact_reason}\nContact Info: {contact_info}\nMessage: {message}"
            
            msg = MIMEMultipart()
            msg['From'] = contact_info
            msg['To'] = email_recipient
            msg['Subject'] = email_subject
            msg.attach(MIMEText(email_body, 'plain'))
            
            try:
                # Configurar el servidor SMTP
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(st.secrets["smtp"]["username"], st.secrets["smtp"]["password"])
                text = msg.as_string()
                server.sendmail(contact_info, email_recipient, text)
                server.quit()
                st.success("Your message has been sent successfully!")
            except Exception as e:
                st.error(f"Error sending message: {e}")

            # Generar enlace de WhatsApp
            whatsapp_message = f"Reason: {contact_reason}\nContact Info: {contact_info}\nMessage: {message}"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_link = f"https://wa.me/5930993513082?text={encoded_message}"
            
            st.markdown(f"Or contact me via WhatsApp: [Click here](https://wa.me/5930993513082?text={encoded_message})")
