# Password Manager

## Description
This is a simple Password Manager built using Python and Tkinter. It allows users to generate secure passwords, copy them to the clipboard, and save them in a text file for future use.

## Features
- Generate secure passwords with a mix of letters, numbers, and symbols.
- Copy generated passwords to the clipboard automatically.
- Save website credentials (website, email/username, password) to a `passwords.txt` file.
- Simple and user-friendly GUI.

## Requirements
Ensure you have the following dependencies installed before running the program:

- Python 3.x
- Tkinter (comes with Python by default)
- `pyperclip` module (for copying passwords to clipboard)

To install `pyperclip`, run:
```sh
pip install pyperclip
```

## Installation and Usage
1. Clone or download this repository:
```sh
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```
2. Place an image file named `logo.png` in the same directory as the script.
3. Run the script:
```sh
python password_manager.py
```
4. Enter website, email/username, and generate a password.
5. Click "Add" to save the credentials to `passwords.txt`.

## File Structure
```
password-manager/
│-- password_manager.py  # The main Python script
│-- passwords.txt        # Stores saved credentials (created automatically upon first save)
│-- logo.png             # Padlock image used in the UI
│-- README.md            # This README file
```

## Notes
- The program does not implement encryption. Passwords are stored in plain text.
- Be sure to keep `passwords.txt` secure to prevent unauthorized access.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is open-source and available for modification and distribution.

## Contact
For any questions or suggestions, feel free to reach out!
 
