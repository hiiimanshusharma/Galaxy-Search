from st_on_hover_tabs import on_hover_tabs
from streamlit_card import card
from streamlit_modal import Modal
import streamlit as st
import requests


API_URL = "http://localhost:8000/api/v1"

def fetch_data(endpoint: str, params: dict) -> dict:
    try:
        response = requests.get(f"{API_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return {}

def regular_search_section():
    st.header("Regular Search")
    modal = Modal(
        "Demo Modal", 
        key="demo-modal",
        
        # Optional
        padding=20,    # default value
        max_width=744  # default value
    )
    search_query = st.text_input("Enter search query:")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        skip = st.number_input("Skip results", min_value=0, value=0)
    with col2:
        limit = st.number_input("Results per page", min_value=1, value=10)
    with col3:
        year = st.text_input("Year (optional):")
    with col4:
        tokenizer = st.selectbox("Tokenizer", ['Standard', 'N-Gram'])


    if st.button("Search"):
        if search_query:
            params = {
                "search_query": search_query,
                "skip": skip,
                "limit": limit,
                "year": year if year else None,
                "tokenizer": tokenizer
            }
            result = fetch_data("regular_search", params)
            if result:
                st.write(f"Total Results: {result['max_pages']} pages")
                
                for hit in result.get("hits", []):
                    
                    has_clicked = card(
                        title=hit['_source']['title'],
                        text=hit['_source']['explanation'],
                        image=hit['_source']['image_url'],
                        styles={
                            "card": {
                                "width": "100%", 
                                "height": "300px",
                                "margin": "0",  # Remove any margin between cards
                                "padding": "0",  # Remove any padding inside the card
                                "box-sizing": "border-box",  # Ensures the padding doesn't add extra space
                            },
                            "image": {
                                "max-height": "200px",  # Adjust image height to ensure cards are more uniform
                                "object-fit": "cover",  # Ensure the image doesn't stretch out of bounds
                            },
                            "text": {
                                "padding": "10px",  # Optional: Add padding inside text area
                                "overflow": "hidden",  # Hide overflow if any content is too large
                            }
                        }
                    )
                    _, _,_,_, col = st.columns(5)
                    with col:
                        with st.popover("See more"):
                                st.title(hit['_source']['title'])
                                st.image(hit['_source']['image_url'])
                                st.write(hit['_source']['explanation'])
                    # st.write(f"Title: {hit['_source']['title']}")
                    # st.write(f"Explanation: {hit['_source']['explanation']}")
                    # st.write("-" * 40)
        else:
            st.warning("Please enter a search query")

def semantic_search_section():
    st.header("Semantic Search")

    search_query = st.text_input("Enter search query:")
    col1, col2, col3= st.columns(3)
    with col1:
        skip = st.number_input("Skip results", min_value=0, value=0)
    with col2:
        limit = st.number_input("Results per page", min_value=1, value=10)
    with col3:
        year = st.text_input("Year (optional):")

    if st.button("Search"):
        if search_query:
            params = {
                "search_query": search_query,
                "skip": skip,
                "limit": limit,
                "year": year if year else None
            }
            result = fetch_data("sematic_search", params)
            if result:
                st.write(f"Total Results: {result['max_pages']} pages")
                for hit in result.get("hits", []):
                    st.write(f"Title: {hit['_source']['title']}")
                    st.write(f"Explanation: {hit['_source']['explanation']}")
                    st.write("-" * 40)
        else:
            st.warning("Please enter a search query")

def main():
    st.set_page_config(layout="wide")

    st.title("Galaxy Search :star2:")
    st.markdown('<style>' + open('./template/css/style.css').read() + '</style>', unsafe_allow_html=True)

    with st.sidebar:
        tabs = on_hover_tabs(tabName=['Regular Search', 'Semantic Search'], 
                         iconName=['dashboard', 'dashboard'], default_choice=0)

    if tabs == "Regular Search":
        regular_search_section()
    elif tabs == "Semantic Search":
        semantic_search_section()

if __name__ == "__main__":
    main()
