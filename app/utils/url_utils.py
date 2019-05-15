def replace_url_placeholder(url, replace_to):
    PLACEHOLDER = '#{page}'
    new_url = url.replace(PLACEHOLDER,str(replace_to))
    return new_url