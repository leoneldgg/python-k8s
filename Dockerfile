FROM python:3.11-buster

LABEL MANTAINER="Leonel Gareis"
LABEL CONTACT="leonelgareis@proton.me"

WORKDIR /app
EXPOSE 8000


# Install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy source code
COPY ./src .

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
