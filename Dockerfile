FROM python:3.11-slim

WORKDIR /app
ENV TZ=Asia/Shanghai
EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x /app/start.sh && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

CMD ["/bin/bash","-c","./start.sh"]
