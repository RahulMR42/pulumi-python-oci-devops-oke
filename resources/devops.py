import os
from git import Repo
import pulumi_oci as oci
from urllib.parse import quote


class devops:
    def create_devops_project(self,config,notification_topic):

        try:
            devops_project = oci.devops.Project("devops_project",
                                                compartment_id=config.get('compartment_ocid'),
                                                name=config.get('oci_devops_project_name'),
                                                notification_config=oci.devops.ProjectNotificationConfigArgs(
                                                    topic_id=notification_topic.id,
                                                ),)
            return  devops_project
        except Exception as error:
            print("Devops project creation failed " + str(error))

    def create_devops_coderepo(self,config,devops_project):
        try:
            devops_coderepo = oci.devops.Repository("devops_coderepo",
                                                     default_branch="refs/heads/main",
                                                     description=config.get('devops_coderepo_description'),
                                                     name=config.get('devops_coderepo_name'),
                                                     project_id=devops_project.id,
                                                     repository_type="HOSTED")
            return devops_coderepo

        except Exception as error:
            print("Devops coderepo creation failed " + str(error))

    def clone_and_push_code(self,config,devops_coderepo,devops_project):
        try:
            #if not os.path.exists(config.get('github_clone_path')):
            repo = Repo.clone_from(config.get('github_url'), config.get('github_clone_path'))
            git_ocir_username = quote(os.environ['TF_VAR_oci_user'],safe='')
            oci_remote_url = f"https://{git_ocir_username}:{os.environ['TF_VAR_oci_user_password']}@devops.scmservice.us-ashburn-1.oci.oraclecloud.com/namespaces/fahdabidiroottenancy/projects/oci_pulumi_devops_project/repositories/oci_pulumi_nodejs"
            remote = repo.create_remote('oci', url=oci_remote_url)
            remote.push(refspec='{}:{}'.format('main', 'main'))
        except Exception as error:
            print("Clone and Push code failed " + str(error))






