# Password Manager

A simple password manager built using Python and Tkinter. It allows users to generate strong passwords, store them securely in a text file, and copy generated passwords to the clipboard.

## Features
- Generate strong passwords with random letters, numbers, and symbols.
- Save website credentials (Website, Email/Username, Password) to a local text file.
- Copy generated passwords directly to the clipboard.
- Simple and intuitive user interface.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You also need to install `pyperclip` for clipboard functionality:

```sh
pip install pyperclip
```

### Clone the Repository
```sh
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```

## Usage
Run the script using Python:
```sh
python password_manager.py
```

### UI Overview
- **Website**: Enter the website name.
- **Email/Username**: Enter your email or username (pre-filled with `xxx@gmail.com`).
- **Password**: Generate a secure password by clicking "Generate Password."
- **Add**: Save the credentials to `passwords.txt`.

### Screenshot

![image](https://github.com/user-attachments/assets/fb5f1c2d-5a71-403e-815f-0b1f19a8ee93)

## File Structure
```
password-manager/
│-- password_manager.py  # Main application script
│-- logo.png             # Padlock image for UI
│-- passwords.txt        # Stored credentials (created after first save)
│-- README.md            # Project documentation
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests for improvements!
