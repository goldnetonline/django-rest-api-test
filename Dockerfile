FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    default-mysql-client \
    git \
    zip \
    curl \
    sudo \
    nano \
    cron \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/
COPY requirements.txt ./
RUN pip install -r requirements.txt

# This should come before the requirement install
RUN pip install mysqlclient

COPY gunicorn.service /etc/systemd/system/gunicorn.service

COPY nginx.conf /etc/nginx/sites-enabled/tokencredit



COPY . .

EXPOSE 80
EXPOSE 443
# CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
# CMD ["/bin/bash", "server.sh"]

CMD ["gunicorn", "tokencredit.wsgi:application", "-b :80", "--forwarded-allow-ips=\"*\"", "-w 3"]