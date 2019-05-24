# relais-button-docker-arm
Docker to provide a relais-button-actor listening on a mqtt topic

# build it 
docker build --rm -t jumajumo/relais_button .

# run it
docker run -d --network="host" --privileged -e brokeraddr=192.168.0.150 -e thingid=rbGaragedoor -e pin=17 --restart always --name "jumajumo_relais_button" jumajumo/relais_button

- --privileged: privileged is necessary in order to allow access to gpio
- -e brokeraddr: ip address of the mqtt broker (default port 1883 is used) (default "openhabian")
- -e thingid: thing id of the sensor (used for mqtt-topic) (default "actor")
- -e pin: the gpio pin used for the sensor (default 17)
- --restart: define the restart policy. always: start container on each start of the docker daemon
- --name: give it a name
