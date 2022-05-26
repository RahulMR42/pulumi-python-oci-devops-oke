import pulumi_oci as oci

test_user = oci.identity.User("test-user",
                              compartment_id="ocid1.tenancy.oc1..aaaaaaaasu7rvefmsyk5kqczfmdqi5clpddejfjk2attdqnk6sbk72wajq5q",
                              email="testuser@mr.com",
                              description="Test User Created by mr")