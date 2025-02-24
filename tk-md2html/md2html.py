import sys
import re

def convert_md_to_html(markdown_file, output_file, background):
    try:
        with open(markdown_file, 'r') as file:
            markdown_content = file.read()

        # Convert headings
        markdown_content = re.sub(r'^(#{1,6})\s*(.+)', lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>\n", markdown_content, flags=re.MULTILINE)
        
        # Convert bold
        markdown_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>\n', markdown_content)
        
        # Convert italic
        markdown_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>\n', markdown_content)
        
        # Convert blockquotes
        markdown_content = re.sub(r'^\>\s*(.+)', r'<blockquote>\1</blockquote>\n', markdown_content, flags=re.MULTILINE)
        
        # Convert ordered lists
        markdown_content = re.sub(r'^\d+\.\s*(.+)', r'<ol><li>\1</li></ol>\n', markdown_content, flags=re.MULTILINE)
        
        # Convert unordered lists
        markdown_content = re.sub(r'^\-\s*(.+)', r'<ul><li>\1</li></ul>\n', markdown_content, flags=re.MULTILINE)
        
        # Convert code blocks
        markdown_content = re.sub(r'`(.+?)`', r'<code>\1</code>\n', markdown_content)
        
        # Convert horizontal rules
        markdown_content = re.sub(r'^\-{3,}', r' \n', markdown_content, flags=re.MULTILINE)
        
        # Convert images
        markdown_content = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img class="img" src="\2" alt="\1">\n', markdown_content)

        # Convert links
        markdown_content = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>\n', markdown_content)
        
        # Convert normal text (paragraphs)
        markdown_content = re.sub(r'^(?!\s*#|^\d+\.|^\-|\>|\!\[|\[|`|^\-{3,}).+', r'<p>\g<0></p>', markdown_content, flags=re.MULTILINE)

        # Insert <br> tags for empty lines with newlines
        markdown_content = re.sub(r'\n\n+', r'<br>\n\n', markdown_content)


        # Write to output file
        with open(output_file, 'w') as file:
            file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{output_file}</title>
""")
            if background == "#b3b3b3":
                file.write("""<style>
body {
    font-family: Arial, sans-serif;
    background-color: #b3b3b3;
    text-align: left;
    padding-left: 10%;
}
.img {
    width: 80%;
}
</style>
</head>
<body>
""")
            else:
                file.write("""<style>
body {
    font-family: Arial, sans-serif;
    background-color: #2f3436;
    color: #f0f0f0;
    text-align: left;
    padding-left: 10%;
}
.img {
    width: 80%;
}
</style>
</head>
<body>
""")
            file.write(markdown_content)
            file.write("""</body>
</html>
""")
            
    except Exception as e:
        print(f"Error: {e}")




try:
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        bg = sys.argv[3]
        if bg.lower() == "dark":
            background_color = "#2f3436"
        elif bg.lower() == "light":
            background_color = "#b3b3b3"
    except IndexError:
        background_color = "#b3b3b3"
    except Exception:
        background_color = "#b3b3b3"

    convert_md_to_html(markdown_file, output_file, background_color)
except IndexError:
    print("\nmd2html converter\nCopyright (c) 2025 Tobias Kisling")
    print("Usage: python md2html.py <markdown_file> <output_file> <background (Optional, default: light, possible: dark/light)>")

except Exception as e:
    print(f"Error: {e}")
