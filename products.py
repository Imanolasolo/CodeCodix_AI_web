import streamlit as st

def show_products_services():
    st.title("Products & Services")

    # Content in columns
    col1, col2 = st.columns(2)

    # Product Information
    with col1:
        st.header(":red[Explore Our Innovative Solutions]")
        st.warning("Discover how our cutting-edge products can transform your business. From AI-powered chatbots to interactive business cards, we provide solutions that enhance engagement, streamline operations, and drive growth. Dive into our diverse offerings and find out how we can help you achieve your goals.")
        
        st.write("- AI-based chatbots")
        st.download_button(
            label="Download Product Info",
            data=open('CodeCodix_products.pdf', 'rb').read(),
            file_name='products_info.pdf',
            mime='application/pdf',
            key='download_product_info'  # Unique key for this button
        )

        st.write("- Virtual assistants")
        st.download_button(
            label="Download Virtual Assistant Info",
            data=open('CodeCodix_assistant_AI.pdf', 'rb').read(),
            file_name='assistant_info.pdf',
            mime='application/pdf',
            key='download_assistant_info'  # Unique key for this button
        )

        st.write("- Interactive Cards")
        st.download_button(
            label="Download Interactive Card Info",
            data=open('CodeCodix_Interactive_card.pdf', 'rb').read(),
            file_name='interactive_card_info.pdf',
            mime='application/pdf',
            key= 'download_interactive_card_info' # Unique key for this button
        )        

    # Service Information
    with col2:
        st.header(":red[Elevate Your Business with Our Expert Services]")
        st.warning("Unlock the potential of your business with our tailored services designed to meet your unique needs. Whether it's optimizing customer interactions through AI-driven solutions or receiving expert guidance on AI implementation, our services are crafted to enhance efficiency, drive innovation, and deliver exceptional results. Explore how we can partner with you to achieve success..")
        
        st.write("- AI driven Customer Service")
        st.download_button(
            label="Download AI driven Customer service info",
            data=open('CodeCodix_AI_Driven_Customer_Service_Solutions.pdf', 'rb').read(),
            file_name='AI_driven_customer_service_solution.pdf',
            mime='application/pdf',
            key= 'download_AI_driven_Customer_service_info'
        )
        st.write("- AI Consultory")

        st.download_button(
           label="Download consultory Info",
           data=open('CodeCodix_Consultory_Service.pdf', 'rb').read(),
           file_name='Consultory_info.pdf',
           mime='application/pdf',
           key='download_consultory_info'  # Unique key for this button
         )

# Call the function in your main file
if __name__ == "__main__":
    show_products_services()
