import pyfiglet

def create_banner(text, font="slant"):
    ascii_banner = pyfiglet.figlet_format(text, font=font)
    print(ascii_banner)

# Example usage
text = input("Enter text for banner: ")
create_banner(text)