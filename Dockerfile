# Use the official Python image as the base image
FROM python:3.10

# Set environment variables
ENV APP_HOME /app
ENV PYTHONUNBUFFERED 1

ENV ASPECT_SERVER_HOST=10.10.110.95
ENV ASPECT_DB=ASPECT_DB
ENV ACCESS_TOKEN_EXPIRE_MINUTES=30
ENV ALGORITHM=HS256
ENV JWT_SECRET_KEY=ef3ffea74db9ba1606ecbe0c68261b87e6f9b0c1b90e406b136a3b1423e4fcb7

# Set the working directory in the container
WORKDIR $APP_HOME

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code to the container
COPY . .


# Expose port 80 for the FastAPI application
EXPOSE 80

# Command to start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]