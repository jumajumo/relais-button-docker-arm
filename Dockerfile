FROM hypriot/rpi-python

RUN pip install paho-mqtt -i https://pypi.python.org/simple

ADD subscribe.py /var/jumajumo/subscribe.py
RUN chmod +x /var/jumajumo/subscribe.py

CMD python /var/jumajumo/subscribe.py
