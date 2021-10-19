FROM python:3.8-slim-buster
WORKDIR /app
RUN sudo apt update && sudo apt install fortune-mod -y
RUN pip3 install -U Flask
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]