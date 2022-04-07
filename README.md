# Extraction proxy and worker containers

## A distributed way to collect social media data

### Description

These components are supposed to be dependent to packages from my previous repositories.

### Deploying

#### Docker

Use this command to build and deploy the containers:

    sudo docker-compose up -d

#### Development

  The folder [env](/env/) contains environment variables for each supported online social network.
  Depending on your implementation, there are variables that are global (like `TwitterCredentials`) and there are some that are specific for a service.
  These variable names are shown in [extractors.json](/worker/extractors.json)  and initialised inside constants.py in order to be used in a generic way and avoid to mess around inside the code.

  - To use the variables in a large scaled extraction, you should initialise every variable mentioned in `extractors.json` after launching the `shared context` subsystem.




### Progress
    

- [x] Proxy server. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
  - [x] Service choice depending on the query model. 
  - [x] Submit tasks to workers.
- [x] Choreographed extraction using context. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
- [x] Extraction template. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/85)
  - [x] Sending data to data transformers.
  - [x] Environment variables to initialise the extraction.
  - Image Extraction.
  - Youtube video downloading. 
- [x] Containerisation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
  - [x] Automation of deployment. (docker-compose)
  - [x] Smaller footprint.

>## NOTES:
> - Proxy and worker components are dependent on the context component.
> - Workers depend on the proxy.
>