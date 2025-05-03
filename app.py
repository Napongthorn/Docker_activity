import os

secret_user = os.getenv("secret_user", "Anonymous")
print(f"Hello, {secret_user}")