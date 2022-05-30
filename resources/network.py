import pulumi_oci as oci

class network:
    def create_vcn(self,config):
        try:
            test_vcn = oci.core.Vcn("testVcn",
                                    compartment_id=config.get('compartment_ocid'),
                                    cidr_block=config.get('vcn_cidr_block'),
                                    display_name=config.get('vcn_display_name'),
                                    )
            return  test_vcn
        except Exception as error:
            print("VNC Creation failed " + str(error))

    def create_service_gateway(self,config,vcn):
        try:

            test_service_gateway = oci.core.ServiceGateway("test_service_gateway",
                                                           compartment_id=config.get('compartment_ocid'),
                                                           display_name=config.get('servicegateway_name'),
                                                           services=[oci.core.ServiceGatewayServiceArgs(
                                                               service_id=oci.core.get_services().services[1].id,
                                                           )],
                                                           vcn_id=vcn.id,
                                                           )
            return  test_service_gateway
        except Exception as error:
            print("Service gateway Creation failed " + str(error))

    def create_natgateway(self,config,vcn):
        try:
            test_nat_gateway = oci.core.NatGateway("test_nat_gateway",
                                                   compartment_id=config.get('compartment_ocid'),
                                                   display_name=config.get('natgateway_name'),
                                                   # public_ip_id="ocid1.publicip.oc1.iad.aaaaaaaatsq2mryszw3msna665l4goxjfg3pon5cni7szhxyiestzv3okb7a",
                                                   vcn_id=vcn.id,)

            return  test_nat_gateway

        except Exception as error:
            print("Nat gateway Creation failed " + str(error))
