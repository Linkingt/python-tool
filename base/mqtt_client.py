#!/usr/bin/env python
# coding=utf-8
import base64
import hmac
import threading
import time
from hashlib import sha1
from paho.mqtt import client as mqtt
from paho.mqtt.client import MQTT_LOG_INFO, MQTT_LOG_NOTICE, MQTT_LOG_WARNING, MQTT_LOG_ERR, MQTT_LOG_DEBUG


class MqttClient:

    def __init__(self, client_id, access_key, secret_key, instance_id, broker_address, port, topic):
        self.client_thread = None
        self.on_message = None
        self.client_id = client_id
        self.access_key = access_key
        self.secret_key = secret_key
        self.instance_id = instance_id
        self.broker_address = broker_address
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(client_id, protocol=mqtt.MQTTv311, clean_session=True)
        self.lock = threading.Lock()
        self.is_connected = False

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.is_connected = True
        client.subscribe(self.topic)

    def on_message(client, userdata, msg):
        print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}' with QoS {msg.qos}")

    def set_message(self, func):
        self.on_message = func

    def connect(self):
        self.is_connected = True
        self.client.on_log = on_log
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        userName = 'Signature' + '|' + self.access_key + '|' + self.instance_id
        password = base64.b64encode(hmac.new(self.secret_key.encode(), self.client_id.encode(), sha1).digest()).decode()
        self.client.username_pw_set(userName, password)
        # ssl设置，并且port=8883 client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
        # tls_version=ssl.PROTOCOL_TLS, ciphers=None)
        self.client.connect(self.broker_address, self.port, 60)
        self.client_thread = threading.Thread(target=self.client_loop)
        self.client_thread.start()

    def client_loop(self):
        while self.is_connected:
            try:
                self.client.loop(1)  # 非阻塞循环，参数为超时时间（秒）
            except KeyboardInterrupt:
                self.is_connected = False
                break
            time.sleep(1)  # 休眠一段时间，防止CPU占用过高

    def publish(self, topic, message):
        if self.is_connected:
            self.client.publish(topic, message)
        else:
            print("Not connected to MQTT broker. Please connect first.")

    def on_disconnect(self, client, userdata, rc):
        self.is_connected = False
        self.client.disconnect()
        self.client_thread.join()
        if rc != 0:
            print('Unexpected disconnection %s' % rc)

    def disconnect(self):
        print('disconnect.....')
        disconnect = self.client.disconnect()
        self.client_thread.join()
        print(f'disconnect result:{disconnect}')


def create_client(client_id, access_key, secret_key, instance_id, broker_address, port, topic):
    return MqttClient(client_id, access_key, secret_key, instance_id, broker_address, port, topic)


def on_log(userdata, level, buf):
    if level == MQTT_LOG_INFO:
        head = 'INFO'
    elif level == MQTT_LOG_NOTICE:
        head = 'NOTICE'
    elif level == MQTT_LOG_WARNING:
        head = 'WARN'
    elif level == MQTT_LOG_ERR:
        head = 'ERR'
    elif level == MQTT_LOG_DEBUG:
        head = 'DEBUG'
    else:
        head = level
    print('%s: %s' % (head, buf))
