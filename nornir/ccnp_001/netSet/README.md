# Network Automation
Using Nornir, Netmiko, and Jinja2 Template files to send configurations

**TOPOLOGY**:
![Topology](images/topology.png)

------------------------------------------------------------------------------------------

This is my attepmt at sending the configuration of a three tier campus network, as specified in the host definition files.

Workflow for this is as follows:

- Create Out-of-band managment network
    - Pink links in topology
- Setup SSH login on each device
- Create base configuration **yaml** files 
    - _config.yaml_
    - _defaults.yaml_
    - _groups.yaml_
    - _hosts.yaml_
- Create template configuration **jinja2** files files
- Create python script
- Run script and verfiy config

There are aspcets of this not working yet, which will create a "golden" configuration file to check against. Check back soon for completed project


