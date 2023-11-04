import streamlit as st
pip install streamlit faiss-cpu langchain

from langchain_helper import get_qa_chain, create_vector_db

  # For CPU version



# Set Streamlit app title and page icon
st.set_page_config(
    page_title="UKL Q and A",
    page_icon="📚",
)

# Add a custom title and description
st.title("UKL Q and A")
st.markdown("Ask your questions and get answers!")

# Create a sidebar for additional options
st.sidebar.header("Options")
create_db = st.sidebar.button("Create Knowledgebase")

# Create a container for the main content
main_container = st.container()

# Create the Knowledgebase when the button is clicked
if create_db:
    with main_container:
        st.header("Creating Knowledgebase...")
    create_vector_db()  # You may want to show a loading spinner here

# Get user input
with main_container:
    question = st.text_input("Ask a Question:")
    if st.button("Get Answer", key="get_answer"):
        if question:
            chain = get_qa_chain()
            response = chain(question)

            st.header("Answer")
            st.write(response["result"])

# Add a footer
st.markdown("---")
st.markdown("Powered by Streamlit")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)