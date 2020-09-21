FROM hickey/rpi-python3

RUN apt-get update && apt-get install -y \
    python3-setuptools \
    gcc \
    cron \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install paho-mqtt -i https://pypi.python.org/simple
RUN pip3 install rpi.gpio -i https://pypi.python.org/simple

ADD cron /var/jumajumo/cron
RUN crontab /var/jumajumo/cron

ADD subscribe.py /var/jumajumo/subscribe.py
RUN chmod +x /var/jumajumo/subscribe.py

CMD python3 /var/jumajumo/subscribe.py
