FROM python:3.8-slim

# Set default execution directory
WORKDIR /model-api

RUN pip install pandas scikit-learn==1.0.1 flask gunicorn

# Copy rest of the project and install
COPY . .
RUN pip install .

# Expose the necessary port for the API
EXPOSE 8080

# Default command
CMD ["gunicorn", "--chdir", "model_api", "app:app"]