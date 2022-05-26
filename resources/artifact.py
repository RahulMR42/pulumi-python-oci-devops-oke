import pulumi
import pulumi_oci as oci

class artifacts:
    def container_repo(self,config_object,display_name,is_public):
        try:
            test_container_repository = oci.artifacts.ContainerRepository("testContainerRepository",

                                                                          compartment_id=config_object.compartment_ocid,
                                                                          display_name=f"{config_object.name_prefix}_{display_name}",
                                                                          is_public=is_public
                                                                          )
            return  test_container_repository
        except Exception as error:
            print("Error during container repo creation " + str(error))