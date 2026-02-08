# 1. Use Python 3.14 as the base image (Slim version is lighter/faster)
FROM python:3.14-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy just the requirements file first (Best practice for caching)
# This prevents Docker from re-installing libraries every time you change a single line of code
COPY requirements.txt .

# 4. Install dependencies
# (Since you have uv.lock, ensure your requirements.txt is up to date first!)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your source code into the container
COPY . .

# 6. Expose the default Streamlit port
EXPOSE 8501

# 7. The command to launch your app
# We use --server.address=0.0.0.0 so it is accessible from Windows
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]