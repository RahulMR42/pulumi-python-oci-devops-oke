import pulumi_oci as oci

class oke:
    def create_cluster(self,config,vcn):
        try:
            test_cluster = oci.containerengine.Cluster("test_cluster",
                                                        compartment_id=config.get('compartment_ocid'),
                                                        endpoint_config=oci.containerengine.ClusterEndpointConfigArgs(
                                                            is_public_ip_enabled=config.get('oke_is_public_ip_enabled'),
                                                            subnet_id="ocid1.subnet.oc1.iad.aaaaaaaazirkqejixk4rncgbqfrtpybkzxb7kvtxqnarnf6qvtigjiceom7q",
                                                        ),
                                                        name=config.get('oke_cluster_name'),
                                                       kubernetes_version="v1.23.4",
                                                        options=oci.containerengine.ClusterOptionsArgs(
                                                            kubernetes_network_config=oci.containerengine.ClusterOptionsKubernetesNetworkConfigArgs(
                                                                pods_cidr="10.244.0.0/16",
                                                                services_cidr="10.96.0.0/16",
                                                            ),
                                                            persistent_volume_config=oci.containerengine.ClusterOptionsPersistentVolumeConfigArgs(

                                                            ),
                                                            service_lb_config=oci.containerengine.ClusterOptionsServiceLbConfigArgs(

                                                            ),
                                                            service_lb_subnet_ids=["ocid1.subnet.oc1.iad.aaaaaaaag2sysjgzur7tnhwugf2r6rra6x4tabtti5gbvys7aijvj7dmp67a"],
                                                        ),vcn_id=vcn.id,)
            return  test_cluster

        except Exception as error:
            print("OKE Cluster creation failed " + str(error))




