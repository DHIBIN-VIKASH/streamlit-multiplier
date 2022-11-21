mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21f3001664@student.onlinedegree.iitm.ac.in\"\n\
" > ~/.streamlit-multiplier

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
