# Use the Rasa base image
FROM rasa/rasa:3.5.0

# Set the environment variable for the PORT (Cloud Run uses port 8080)
ENV PORT=8080

# Copy all project files at once
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Expose the port that Cloud Run will use
EXPOSE 8080

# Run the Rasa server, ensuring it binds to port 8080
CMD ["run", "--model", "/app/models", "--enable-api", "--cors", "*", "--port", "8080"]
