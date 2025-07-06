from flask import Flask
from website import create_app

app = create_app()
print("app instance created")
if __name__ == "__main__":
    app.run(debug=True)
