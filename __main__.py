import os
from resources.common import  common_config
from resources.artifact import  artifacts


config_object = common_config('ocid1.compartment.oc1..aaaaaaaalmc42p5bsqbfo5jkle7uy7bwnlazr7ghw26qorsidrwbl6mk6xva',
                              os.environ['TF_VAR_region'],
                              'mr_pulumi')

artifact_object = artifacts()
display_name = "oke_image_store"
is_public = True
test_container_repository = artifact_object.container_repo(config_object,display_name,is_public)