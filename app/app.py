import streamlit as st
from search import search_movies

st.set_page_config(
    page_title="Semantic Movie Search",
    layout="wide"
)

st.title("🎬 SceneSense AI")
st.caption("Find movies using natural language")

st.write(
    "Describe a scene, emotion, theme, or storyline and SceneSense AI "
    "will find the most semantically similar movies."
)

query = st.text_input(
    "Search",
    placeholder="Example: A father sacrifices himself for his family"
)

if st.button("🔍 Search", use_container_width=True):

    if query.strip() == "":
        st.warning("Please enter a search query.")
    else:

        results = search_movies(query)

        if results is None:
            st.error("❌ No similar movies found. Try another description.")
        else:

            st.success(f"Found {len(results)} matching movies")
        
            for _, movie in results.iterrows():
                with st.container(border=True):
                    
                    col1, col2 = st.columns([4,1])

                    with col1:
                        st.subheader(movie["title"])
                        st.caption(f"🎭 {movie['genres']} | 📅 {movie['year']}")

                    with col2:
                        st.metric(
                            label="Match",
                            value=f"{movie['Score']}%"
                        )

                    st.write("**Summary**")
                    st.write(movie["Summary"])
                    st.write(movie["Summary"])
                    # st.divider()
                    # with st.expander("View Full Plot"):
                    #     st.write(movie["plot"])

                    
            # with st.sidebar:

            #         st.title("SceneSense AI")

            #         st.markdown("---")

            #         st.write("Model")
            #         st.success("all-MiniLM-L6-v2")

            #         st.write("Search Engine")
            #         st.success("FAISS")

            #         st.write("Dataset")
            #         st.success("2858 Movies ")