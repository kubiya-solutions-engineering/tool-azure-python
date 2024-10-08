from kubiya_sdk.tools.models import Tool
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES

AZURE_ICON_URL = "https://azure.microsoft.com/svghandler/azure-logo/?width=300&height=300"
SCRIPT_LOGIN   = "az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID"

class AzureCliTool(Tool):
    def __init__(self, name, description, content, args, long_running=False, mermaid_diagram=None):
        # Combine the login and received content into a single script
        full_content = f"{SCRIPT_LOGIN}\n{content}"

        super().__init__(
            name=name,
            description=description,
            icon_url=AZURE_ICON_URL,
            type="docker",
            image="mcr.microsoft.com/azure-cli:latest",
            content=full_content,
            args=args,
            env=COMMON_ENVIRONMENT_VARIABLES,
            secrets=COMMON_SECRET_VARIABLES,
            long_running=long_running,
            mermaid_diagram=mermaid_diagram
        )

