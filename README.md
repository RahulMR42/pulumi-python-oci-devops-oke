Deploy OCI Devops and OKE with Pulumi - python 
---

Requirements 

- Python3
- pulumi cli

Set the credentials 
----
export TF_VAR_tenancy_ocid="ocid1.tenancy.xxx"
export TF_VAR_user_ocid="ocid1.user.xxxx"
export TF_VAR_fingerprint="xxxx"
export TF_VAR_region="xxx"
export TF_VAR_private_key_file="xxx"
export TF_VAR_oci_user="xxx"
export TF_VAR_oci_user_password="xxxx"

Procedure
----

```markdown
mkdir oci-pulumi-devops
cd oci-pulumi-devops
pulumi login (refer https://github.com/oracle-devrel/pulumi-python-oci-oke for more login options)
pulumi new https://github.com/RahulMR42/pulumi-python-oci-devops-oke
pulumi config set compartment_ocid "OCID of your compartment"
pulumi config set autobuild_run "False" - Option /to avoid a auto build run
pulumi pre
pulumi up
Once done Access OKE run kubectl run all -n ns-node
Delete the loadbalancer by the OKE and then run pulumi destroy 
```

- Read details here - https://github.com/oracle-devrel/pulumi-python-oci-devops-oke