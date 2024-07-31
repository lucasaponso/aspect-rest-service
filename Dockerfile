# Use the official Python image as the base image
FROM python:latest

# Set environment variables
ENV APP_HOME /app
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR $APP_HOME

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -U -r requirements.txt

# Copy the FastAPI application code to the container
COPY . .


# Expose port 80 for the FastAPI application
EXPOSE 80

# Command to start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]