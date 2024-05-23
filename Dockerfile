FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8080
ENV NAME sample-fast-api-docker
LABEL maintainer="ktchambers"
LABEL org.opencontainers.image.source=https://github.com/PraxisAppDev/python-microservice
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]DockerfileCopy code
