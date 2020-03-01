FROM python:3.7.3-stretch

# Working Directory
WORKDIR /project-two

# Copy source code to working directory
COPY . app.py /project-two/


RUN pip install pandas

# CMD echo "Hello! This is my first Docker image. Everything functions properly..."
CMD ["python", "app.py"]