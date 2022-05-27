import os
from resources.common import  common_config
from resources.artifact import  artifacts
from resources.devops import devops
from resources.notification import notification
from pulumi import Config
import inspect

"""To remov"""
config_object = common_config('ocid1.compartment.oc1..aaaaaaaalmc42p5bsqbfo5jkle7uy7bwnlazr7ghw26qorsidrwbl6mk6xva',
                              os.environ['TF_VAR_region'],
                              'mr_pulumi')
"""" - """
config = Config()
container_repository = artifacts().container_repo(config)
notification_topic = notification().create_notification_topic(config)
devops_project = devops().create_devops_project(config,notification_topic)
