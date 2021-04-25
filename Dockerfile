FROM python:3.8.5
# Set the working directory to /app
WORKDIR /app
# Copy local contents into the container
ADD . /app
# Install all required dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
