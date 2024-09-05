FROM registry.astralinux.ru/library/alse:1.7.5
RUN apt update && apt install -y rabbitmq-server
RUN rabbitmq-plugins enable rabbitmq_management
RUN mkdir -p /etc/parsec/
RUN touch /etc/parsec/privsock.conf
RUN chmod 644 /etc/rabbitmq/enabled_plugins
RUN echo "default_user = astra" >> /etc/rabbitmq/rabbitmq.conf
RUN echo "default_pass = astra" >> /etc/rabbitmq/rabbitmq.conf
EXPOSE 1883
EXPOSE 4369
EXPOSE 5551-5552
EXPOSE 5671-5672
EXPOSE 6000-6500
EXPOSE 8883
EXPOSE 15671-15672
EXPOSE 15674-15675
EXPOSE 15692
EXPOSE 25672
EXPOSE 35672-35682
EXPOSE 61613-61614
ENTRYPOINT /usr/sbin/rabbitmq-server
