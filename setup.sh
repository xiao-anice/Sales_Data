mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"azhangwenjing@gmail.com\"\n\
" > ~/.streamlit/secrets.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/secrets.toml