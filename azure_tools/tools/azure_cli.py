from kubiya_sdk.tools import Arg
from .base import AzureCliTool
from kubiya_sdk.tools.registry import tool_registry

azure_cli_tool = AzureCliTool(
    name="azure_cli",
    description="Logs in to Azure CLI and then runs the specified command.",
    content="az {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="The Azure CLI command to run (example: account). Do not add `az` at the front.",
            required=True),
    ],
)

tool_registry.register("Azure", azure_cli_tool)
