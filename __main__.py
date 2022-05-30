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
# service_gateway = network().create_service_gateway(config,vcn)
# nat_gateway = network().create_natgateway(config,vcn)
oke_cluster = oke().create_cluster(config,vcn)
