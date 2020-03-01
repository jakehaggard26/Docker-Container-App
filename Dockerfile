FROM python:3.7.3-stretch

# Working Directory
WORKDIR /project-twp

# Copy source code to working directory
COPY . app.py /project-two/

# CMD echo "Hello! This is my first Docker image. Everything functions properly..."
CMD ["python3 app.py"]