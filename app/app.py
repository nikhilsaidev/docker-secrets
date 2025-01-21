from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def display_secrets():
    secrets = []
    for i in range(1, 37):
        secret_path = f"/run/secrets/secret{i}"
        if os.path.exists(secret_path):
            with open(secret_path, "r") as secret_file:
                secrets.append(f"Secret {i}: {secret_file.read().strip()}")
        else:
            secrets.append(f"Secret {i}: Not Found")
    return "<br>".join(secrets)

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=80)
