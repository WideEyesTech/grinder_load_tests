 grinder_load_tests testing
-------------


Use grinder AMIs,

1. Launch the console instance (type m3.medium).
1. Launch a grinder console (type m3.medium).
1. Configure /etc/grinder/console.instance with the console instance id.
1. Send commands via API to console instance.

```
curl -X POST -H "Accept: application/json" "http://ec2-52-18-30-32.eu-west-1.compute.amazonaws.com:6373/agents/start-workers" 
curl -X POST -H "Accept: application/json" "http://ec2-52-18-30-32.eu-west-1.compute.amazonaws.com:6373/agents/stop-workers" 



curl -X GET -H "Accept: application/json" "http://ec2-52-18-30-32.eu-west-1.compute.amazonaws.com:6373/recording/data"
curl -X GET -H "Accept: application/json" "http://ec2-52-18-30-32.eu-west-1.compute.amazonaws.com:6373/recording/status"
curl -X GET -H "Accept: application/json" "http://ec2-52-18-30-32.eu-west-1.compute.amazonaws.com:6373/recording/data-latest"


curl -X POST -H "Accept: application/json" "http://ec2-52-18-30-32.eu-west-1.compute.amazonaws.com:6373/recording/stop"

```