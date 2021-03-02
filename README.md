# poc-fastapi
A Proof-of-Concept serverless app using FastAPI

## Installation

Create a virtualenv and install `pip-tools` in it. Then run the following command to install the requirements: 

    pip-sync requirements/requirements.txt requirements/requirements-test.txt requirements/requirements-dev.txt 


## Lambda invocations (locally)

In the `sample_invocations` folder there is a small collection of sample Lambda requests in JSON format, 
for the various supported endpoints. 

To try those locally, first make sure you have the `STAGE` environment variable set:

    export STAGE=dev

then use `sls` to invoke the lambda locally like this:

    sls invoke local --function fastapp --path sample_invocations/list_items.json

Alternatively, you can simply start serverless in offline mode and access it via a browser:

    sls offline

then visit `http://localhost:3000/dev/docs/`
