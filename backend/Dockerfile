FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
