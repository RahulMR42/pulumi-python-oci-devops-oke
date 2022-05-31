import os
from resources.common import  common_config
from resources.artifact import  artifacts
from resources.devops import devops
from resources.notification import notification
from resources.oke import oke
from resources.network import network
from resources.logs import logs
from pulumi import Config


"""To remov"""
config_object = common_config('ocid1.compartment.oc1..aaaaaaaalmc42p5bsqbfo5jkle7uy7bwnlazr7ghw26qorsidrwbl6mk6xva',
                              os.environ['TF_VAR_region'],
                              'mr_pulumi')
"""" - """
config = Config()
container_repository = artifacts().container_repo(config)
notification_topic = notification().create_notification_topic(config)
log_group = logs().create_log_group(config)
devops_project = devops().create_devops_project(config,notification_topic)
log = logs().create_logs(config,log_group,devops_project)

vcn = network().create_vcn(config)

service_gateway = network().create_service_gateway(config,vcn)
nat_gateway = network().create_natgateway(config,vcn)
internet_gateway = network().create_internet_gateway(config,vcn)

node_security_list = network().create_node_securitylist(config,vcn)
svclb_security_list = network().create_svclb_securitylist(config,vcn)
apiendpoint_security_list = network().create_apiendpoint_securitylist(config,vcn)

oke_node_route_table=network().create_node_routetable(config,vcn,service_gateway,nat_gateway)
oke_svclb_route_table=network().create_svclb_routetable(config,vcn,internet_gateway)

node_subnet = network().create_node_subnet(config,vcn,oke_node_route_table,node_security_list)
lb_subnet = network().create_lb_subnet(config,vcn,oke_svclb_route_table,svclb_security_list)
apiendpoint_subnet = network().create_apiendpoint_subnet(config,vcn,oke_svclb_route_table,apiendpoint_security_list)
# service_gateway = network().create_service_gateway(config,vcn)
# nat_gateway = network().create_natgateway(config,vcn)
oke_cluster = oke().create_cluster(config,vcn,apiendpoint_subnet,lb_subnet)
