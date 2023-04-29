import kfp.dsl as dsl
import os
from dotenv import load_dotenv
from kfp.v2.dsl import component
from kfp.v2 import compiler
from google.cloud import aiplatform as aip

# Define the model training function
def train_model(input: float) -> float:
    return 2.0 + input

# Define the data ingestion function
def ingetst_data(input: float) -> float:
    return 2.0

# Create components for the ingestion and training functions
ingest_data_component = component(ingetst_data)
train_component = component(train_model)

# Define the pipeline using the Kubeflow Pipelines SDK
@dsl.pipeline(
    name="ltv-train",
)
def add_pipeline():
    # Instantiate the ingest_data_component and store its output
    ingest_data = ingest_data_component(input=3.0)
    
    # Instantiate the train_component, passing the output from the ingest_data_component
    train_model = train_component(input=ingest_data.output)
    
    # Disable caching for the train_model component to ensure it runs every time
    train_model.set_caching_options(False)

# Compile the pipeline to generate a YAML file for execution
compiler.Compiler().compile(pipeline_func=add_pipeline, package_path="local_run.yaml")
