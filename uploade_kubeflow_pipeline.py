# This script sets up the connection to a Kubeflow Pipelines Artifact Registry
# using the RegistryClient from the kfp.registry module. It loads the necessary
# environment variables and establishes a connection to the registry.

import os
from kfp.registry import RegistryClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve required environment variables
gcp_project = os.getenv("gcp_project","johan-kubeflow")
kubeflow_pipelines_artifact_registyr = os.getenv('kubeflow_pipelines_artifact_registyr',"test-test")



# Create a RegistryClient instance and connect to the Kubeflow Pipelines Artifact Registry
client = RegistryClient(host=f"https://europe-west1-kfp.pkg.dev/{gcp_project}/{kubeflow_pipelines_artifact_registyr}")

# Upload the pipeline to the Kubeflow Pipelines registry
templateName, versionName = client.upload_pipeline(
    # Provide the compiled pipeline YAML file
    file_name="local_run.yaml",
    
    # Assign tags to the pipeline for easier identification and versioning
    tags=["v1", "latest"],
    
    # Add a description to the pipeline using extra_headers
    extra_headers={"description": "This is an example pipeline template."}
)

