def replace_url_placeholder(url, replace_to):
    PLACEHOLDER = '#{page}'
    return url.replace(PLACEHOLDER,str(replace_to))