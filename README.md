# How old is my dog?

Application developed in order to discover how old is your dog compared with a human age, as well other curiosities.

[Back-end]

Language: Python

Frameworks: Flask, Pymongo

DB: MongoDB

[Front-end]

HTML5 + CSS + JavasScript


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
<!-- See deployment for notes on how to deploy the project on a live system. -->

### Prerequisites

In order to run this app, you need just install Docker CE and Docker Compose.

For more information, see https://docs.docker.com/install/ and https://docs.docker.com/compose/install/.

Clone this repository:

```
git clone https://github.com/ebarros29/howoldismydog
```

### Installing

A step by step series of examples that tell you how to get a development env running

Installing Docker CE and start Docker daemon

```
https://docs.docker.com/install/
```

Installing Docker Compose

```
https://docs.docker.com/compose/install/
```

Running the environment

```
docker-compose up -d
```

<!-- End with an example of getting some data out of the system or using it for a little demo -->

## Running the tests

Simple tests to make sure that is everthing fine.

### Break down into end to end tests

Checking if all containers are running. You should see only 2 containers up, the first one refers to mongo (MongoDB) and the second one to web-app (Python). 

Remark: Mongo_seed runs only to add data files to MongoDB, afther that this goes down. Use below command in order to check containers status:

```
docker ps -a
```

You can check the logs of each container using the below command:

```
docker logs <container id>
```

<!-- ### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds -->

<!-- ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  -->

## Authors

* **Emerson Barros** - *Initial work* - [ebarros29](https://github.com/ebarros29)

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details -->

## Acknowledgments

* I dedicate this work to all animal lovers, especially dogs lovers.
