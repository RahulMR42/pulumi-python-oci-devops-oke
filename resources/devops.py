import pulumi
import pulumi_oci as oci

class devops:
    def create_devops_project(self,config,notification_topic):

        devops_project = oci.devops.Project("testDevopsProject",
                            compartment_id=config.get('compartment_ocid'),
                            name=config.get('oci_devops_project_name'),
                            notification_config=oci.devops.ProjectNotificationConfigArgs(
                                topic_id=notification_topic.id,
                            ),)
        return  devops_project



