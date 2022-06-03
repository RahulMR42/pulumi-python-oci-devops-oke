import os
import shutil
from git import Repo
import pulumi_oci as oci
from pulumi import Config
from urllib.parse import quote
from resources.random import random_string


class devops:
    def __init__(self):
        self.config = Config()
        self.random_string = random_string()

    def create_devops_project(self,notification_topic):

        try:
            devops_project = oci.devops.Project("devops_project",
                                                compartment_id=self.config.get('compartment_ocid'),
                                                name=self.config.get('oci_devops_project_name'),
                                                notification_config=oci.devops.ProjectNotificationConfigArgs(
                                                    topic_id=notification_topic.id,
                                                ),)
            return  devops_project
        except Exception as error:
            print("Devops project creation failed " + str(error))

    def create_devops_coderepo(self,devops_project):
        try:
            devops_coderepo = oci.devops.Repository("devops_coderepo",
                                                     default_branch="refs/heads/main",
                                                     description=self.config.get('devops_coderepo_description'),
                                                     name=self.config.get('devops_coderepo_name'),
                                                     project_id=devops_project.id,
                                                     repository_type="HOSTED")
            return devops_coderepo

        except Exception as error:
            print("Devops coderepo creation failed " + str(error))


    def clone_and_push_code(self,url):
        try:
            git_ocir_username = quote(os.environ['TF_VAR_oci_user'],safe='')
            oci_remote_url = f"https://{git_ocir_username}:{os.environ['TF_VAR_oci_user_password']}@{url.replace('https://','')}"
            if not os.path.exists(self.config.get('github_clone_path')):
                Repo.clone_from(self.config.get('github_url'), self.config.get('github_clone_path'))
            if not os.path.exists(f"{self.config.get('devops_coderepo_name')}_local"):
                Repo.clone_from(oci_remote_url,f"{self.config.get('devops_coderepo_name')}_local")
            shutil.copytree(self.config.get('github_clone_path'), f"{self.config.get('devops_coderepo_name')}_local",dirs_exist_ok=True ,ignore=shutil.ignore_patterns('.git'))
            repo = Repo(f"{self.config.get('devops_coderepo_name')}_local")
            remote_name = self.random_string
            remote = repo.create_remote(remote_name, url=oci_remote_url)
            repo.git.add(all=True)
            repo.index.commit(f"Pushing via remote - {remote_name}")
            remote.push(refspec='{}:{}'.format('main', 'main'))
        except Exception as error:
            print("Clone and Push code failed " + str(error))

    def create_deploy_env(self,devops_project,oke_cluster):
        try:
            deploy_oke_env = oci.devops.DeployEnvironment("deploy_oke_env",
                                                           cluster_id=oke_cluster.id,
                                                           deploy_environment_type=self.config.get('oci_devops_deploy_env_type'),
                                                           display_name=self.config.get('oci_devops_deploy_env_name'),
                                                           project_id=devops_project.id,
                                                           )
            return deploy_oke_env

        except Exception as error:
            print("Deploy env creation is failing " + str(error))







