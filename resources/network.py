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


