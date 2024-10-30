# Use the official Rasa SDK image
FROM rasa/rasa-sdk:3.0.0

# Set the environment variable for PORT to 8080, which is expected by Cloud Run
ENV PORT=8080

# Copy your custom actions to the actions directory
COPY ./actions /app/actions

# Install additional dependencies (if any)
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the correct port
EXPOSE 8080

# Run the custom action server, binding it to the PORT environment variable
CMD ["start", "--actions", "actions", "--port", "8080"]