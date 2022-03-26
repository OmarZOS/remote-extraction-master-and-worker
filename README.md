# Extraction worker and proxy containers 

## A distributed way to collect social media data

### Description

These components are supposed to be dependent to packages from my previous repositories.

### Deploying



#### Docker

Use this command to build and deploy the containers:

    sudo docker-compose up -d



### Progress
    

- [ ] Proxy server. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
  - [ ] REST communication for updates.
    - [ ] Lookup available scripts.
    - [ ] Additivity of more scripts.
      - Static  
  - [x] Submit tasks to workers.
- [x] In between node communication. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/67)
- [x] Extraction template. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
  - [x] Sending data to data transformers.
  - [ ] Dynamic script loading.
- [x] Containerisation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
  - [x] Automation of deployment. (docker-compose)
  - [x] Smaller footprint. (fix alpine linux dependencies)
