# Aadhar_Card_OCR_Python
This is a simple implementation of a OCR reader for the Aadhar Card. To use this project: 
- Download the python file in the repository.
- Open the python file in any IDLE and make the necessary changes in the code to match your system.
- Store the image and the python file in the same working directory.
- Make sure that the mysql server is running and that you have created a table in a database with columns for aadhar card number, gender, data of birth, and name.
- Execute the python file.
- The database should reflect the changes once the executing in completed.

The project has the following dependencies:
- [opencv](https://pypi.org/project/opencv-python/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- Regular Expressions - [re](https://pypi.org/project/regex/)
- mysql connector for python - [mysql.connector](https://pypi.org/project/mysql-connector-python/)
