from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config

nr = InitNornir(config_file="config.yaml")

def load_vars(task):
    data = task.run(task=load_yaml,file=f'./host_vars/{task.host}.yaml')
    task.host["facts"] = data.result

def load_base(task):
    b = task.run(task=template_file, template="base.j2", path="./templates")
    task.host["base_config"] = b.result
    base_output = task.host["base_config"]
    base_send = base_output.splitlines()
    task.run(task=netmiko_send_config, name="Base Commands", config_commands=base_send)

def load_switchport(task):
    b = task.run(task=template_file, template="switchport.j2", path="./templates")
    task.host["switchport_config"] = b.result
    switchport_output = task.host["switchport_config"]
    switchport_send = switchport_output.splitlines()
    task.run(task=netmiko_send_config, name="Switchport Commands", config_commands=switchport_send)

# def load_isis(task):
#     i = task.run(task=template_file, template="isis.j2", path="./templates")
#     task.host["isis_config"] = i.result
#     isis_output = task.host["isis_config"]
#     isis_send = isis_output.splitlines()
#     task.run(task=netmiko_send_config, name="IS-IS Commands", config_commands=isis_send)

def load_ether(task):
    e = task.run(task=template_file, template="etherchannel.j2", path="./templates")
    task.host["ether_config"] = e.result
    ether_output = task.host["ether_config"]
    ether_send = ether_output.splitlines()
    task.run(task=netmiko_send_config, name="Etherchannel Commands", config_commands=ether_send)


def load_trunking(task):
    t = task.run(task=template_file, template="trunking.j2", path="./templates")
    task.host["trunk_config"] = t.result
    trunk_output = task.host["trunk_config"]
    trunk_send = trunk_output.splitlines()
    task.run(task=netmiko_send_config, name="Trunk Commands", config_commands=trunk_send)


def load_vlan(task):
    v = task.run(task=template_file, template="vlan.j2", path="./templates")
    task.host["vlan_config"] = v.result
    vlan_output = task.host["vlan_config"]
    vlan_send = vlan_output.splitlines()
    task.run(task=netmiko_send_config, name="VLAN Commands", config_commands=vlan_send)


yaml_targets = nr.filter(all="yes")
yaml_results = yaml_targets.run(task=load_vars)
base_targets = nr.filter(all="yes")
base_results = base_targets.run(task=load_base)
switchport_targets = nr.filter(all="yes")
switchport_results = switchport_targets.run(task=load_switchport)
# isis_targets = nr.filter(routing="yes")
# isis_results = isis_targets.run(task=load_isis)
ether_targets = nr.filter(etherchannel="yes")
ether_results = ether_targets.run(task=load_ether)
trunk_targets = nr.filter(trunking="yes")
trunk_results = trunk_targets.run(task=load_trunking)
vlan_targets = nr.filter(vlan="yes")
vlan_results = vlan_targets.run(task=load_vlan)
print_result(yaml_results)
print_result(base_results)
print_result(switchport_results)
#print_result(isis_results)
print_result(ether_results)
print_result(trunk_results)
print_result(vlan_results)
print_result(base_results)
