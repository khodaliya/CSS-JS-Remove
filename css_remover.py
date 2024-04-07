from bs4 import BeautifulSoup
import re

def remove_css_js_classes(html_content):
    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove CSS
    for style in soup.find_all('style'):
        style.extract()
    
    # Remove JavaScript
    for script in soup.find_all('script'):
        script.extract()
    
    # Remove classes and ids
    for tag in soup.find_all(True):
        for attribute in ["class", "id"]:
            if tag.has_attr(attribute):
                del tag[attribute]

    # Remove <span> tags
    for span in soup.find_all('span'):
        span.unwrap()

     # Remove <a> tags
    for a_tag in soup.find_all('a'):
        a_tag.unwrap()

    # Remove multiple spaces
    cleaned_html = re.sub(r'\s{2,}', ' ', str(soup))
    
    # Return the modified HTML content
    return cleaned_html

def main(input_file, output_file):
    # Read input HTML file
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Process HTML content
    cleaned_html = remove_css_js_classes(html_content)

    # Write modified HTML to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_html)

# Example usage
input_file = "input.html"
output_file = "output.html"
main(input_file, output_file)
print(f"Output written to {output_file}.")
