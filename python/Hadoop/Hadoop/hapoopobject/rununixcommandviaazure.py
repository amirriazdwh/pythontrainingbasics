from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_run_command.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="24fb23e3-6ba3-41f0-9b6e-e41131d5d61e",
    )

    response = client.virtual_machines.begin_run_command(
        resource_group_name="crptestar98131",
        vm_name="vm3036",
        parameters={"commandId": "RunPowerShellScript"},
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2024-07-01/examples/runCommandExamples/VirtualMachineRunCommand.json
if __name__ == "__main__":
    main()


from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def main():
    # Use DefaultAzureCredential, which will automatically use the managed identity if available
    credential = DefaultAzureCredential()

    client = ComputeManagementClient(
        credential=credential,
        subscription_id="24fb23e3-6ba3-41f0-9b6e-e41131d5d61e",
    )

    response = client.virtual_machines.begin_run_command(
        resource_group_name="crptestar98131",
        vm_name="vm3036",
        parameters={"commandId": "RunPowerShellScript"},
    ).result()
    print(response)

if __name__ == "__main__":
    main()


"""https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/run-command?view=rest-compute-2024-07-01&tabs=HTTP"""