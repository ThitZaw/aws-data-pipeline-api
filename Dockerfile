FROM public.ecr.aws/lambda/python:3.12

# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy your app
COPY app/ ./app/

# Set Lambda handler
CMD ["app.services.lambda_handler.lambda_handler"]