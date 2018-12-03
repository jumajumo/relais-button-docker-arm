FROM hypriot/rpi-python

RUN apt-get update && \
    apt-get -y install gcc && \
    rm -rf /var/lib/apt/lists/*
RUN pip install paho-mqtt -i https://pypi.python.org/simple
RUN pip install rpi.gpio -i https://pypi.python.org/simple

ADD subscribe.py /var/jumajumo/subscribe.py
RUN chmod +x /var/jumajumo/subscribe.py

CMD python /var/jumajumo/subscribe.py
