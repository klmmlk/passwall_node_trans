FROM python:3.11-slim

WORKDIR /app

EXPOSE 8000

COPY . .

RUN apt-get update && \
    apt-get -y install cron && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    cp /app/cronjob /etc/cron.d/ && \
    chmod 0644 /etc/cron.d/cronjob && \
    chmod +x /app/start.sh

CMD ["/bin/bash","-c","./start.sh"]
