FROM python:3.8-slim-buster
WORKDIR /app
RUN apt update && apt install fortune-mod -y
RUN pip3 install -U Flask
COPY . .
ENV FLASK_RUN_PORT=80
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app.py"]