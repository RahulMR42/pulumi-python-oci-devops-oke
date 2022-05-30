import pulumi_oci as oci

class network:
    def create_vcn(self,config):
        try:
            test_vcn = oci.core.Vcn("test_vcn",
                                    cidr_blocks=[config.get('vcn_cidr_block')],
                                    compartment_id=config.get('compartment_ocid'),
                                    display_name=config.get('vcn_display_name'),
                                    dns_label=config.get('vcn_dns_label'),
                                    )
            return  test_vcn


        except Exception as error:
            print("VNC Creation failed " + str(error))

