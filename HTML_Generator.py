import os


def generate_base_html(*args):
    description, keywords, author, title = args
    html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
        <meta charset="UTF-8"/>
        <meta name="description" content="{description}"/>
        <meta name="keywords" content="{keywords}"/>
        <meta name="author" content="{author}"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="icon" type="image/x-icon" href="logo.png">
        <link rel="stylesheet" href="style.css"/>
    </head>
    <body>
        <h1>Welcome {author}!</h1>
        <h3>Now you can customise your html</h3>
       <script src="javascript.js" type="text/javascript"></script>
    </body>
</html>
    """
    css = "h1, h3 {color: red; text-align:center}"
    js = 'alert("Javascript is live")'
    # Create the "html" directory
    directory_name = "/home/lenovo/Desktop/HTML3"
    os.makedirs(directory_name,0o755, exist_ok=True)
    # Create the "index.html" file inside the "html" directory
    for asset in ('index.html', 'style.css', 'javascript.js'):
        with open(os.path.join(directory_name, asset), "w") as file:
            if asset == 'index.html':
                file.write(html)
                file.close()
            if asset == 'style.css':
                file.write(css)
                file.close()
            if asset == 'javascript.js':
                file.write(js)
                file.close()


desc = input('Enter Website Short Description: ')
key = input('Enter Website Keywords: ')
auth = input('Enter Website Author: ')
tle = input('Enter Website Title: ')
generate_base_html(desc, key, auth, tle)

