# plex_notifier

[![Build Status](https://travis-ci.org/co-llabs/plex_notifier.svg?branch=master)](https://travis-ci.org/co-llabs/plex_notifier)
[![GitHub (pre-)release](https://img.shields.io/github/release/co-llabs/plex_notifier/all.svg)]()
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

#### Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Tusk](#tusk)
    * [What It Does](#what-it-does)
    * [Tasks](#tasks)
    * [Where It Is Used](#where-it-is-used)
4. [Setting Parameters](#setting-parameters)
5. [Docker](#docker)
    * [Running the Container](#running-the-container)
6. [Limitations](#limitations)
7. [Disclaimers](#disclaimers)

## Description

A little Python program that queries a Plex server for recently added media and
sends an email to the subscribed users with a list of said media.

### Requirements

* Python 3.6
* Jinja2
* [PlexAPI](https://github.com/pkkid/python-plexapi)
* [Yagmail](https://github.com/kootenpv/yagmail)
* [Tusk](https://github.com/rliebz/tusk)
* Gmail account configured to send from an application

### Tusk

Tusk is a task runner built in go that makes it easy to get started and work
within the confines of a project. You can read all about the project at the link
listed above.

#### What It Does

Tusk does everything from manage dependencies to deployments. There are a number
of tasks configured in the `tusk.yml` file that help make getting started with
and working on this project easier. A full list of tasks can be viewed by
running `tusk --help` and information on each individual task can be viewed by
running `tusk <task> --help`.

#### Tasks

`setup`:  
  * Manage project dependencies

`docker`:  
  * Build, run and destroy the `plex_notifier` Docker container  
  * `options`: _build_, _run_, _destroy_, _tag_

`check`:  
  * Run test suite; `pytest` and `pylint`  
  * `options`: _lint_, _test_

`notify`:  
  * Run `plex_notifer`  
  * `options`: _schedule_, _cancel_

#### Where It Is Used

Tusk is used locally to bootstrap the project as well as to do any amount of
local testing; unit tests, lint, build and run containers.

Tusk is also used in the `.travis.yml` file to bootstrap the container used for
the build and execute the test suite. When a release is made Tusk is used to
build the Docker container for the release version.

Tusk is also used inside the `Dockerfile`. When a `docker build` is executed
part of the build is `tusk` bootstrapping the container and running the test
suite. Tusk is also used to create the cron job to run `plex_notifier` on
container start using the `CMD` section in the `Dockerfile`

### Setting Parameters

The program takes a mix of required and optional parameters. There are some
dependent parameters that become required based on the value of others.
Currently all parameters are set through environment variables but in the future
the option of commandline arguments will be given.

* `plex_username`:
  * Set from the environment parameter `PLEX_USERNAME`
  * Required

* `plex_password`:
  * Set from the environment parameter `PLEX_PASSWORD`
  * Required

* `plex_server`:
  * Set from the environment Parameter `PLEX_SERVER`
  * Required

* `days_passed`:
  * Set from the environment parameter `PLEX_DAYS_PASSED`
  * The number of days to go back to find recently added media
  * Required

* `send_mail`:
  * Set from the environment parameter `PLEX_SEND_MAIL`
  * Whether or not to send the update email
  * Optional (values: true/false; default: false)

* `email_username`:
  * Set from the environment parameter `PLEX_EMAIL_USERNAME`
  * The username for the email address sending the mail
  * Optional unless `send_mail` is `true`

* `email_password`:
  * Set from the environment parameter `PLEX_EMAIL_PASSWORD`
  * The password for the email address sending the mail
  * Optional unless `send_mail` is `true`

* `unsub_emails`:
  * Set from the environment parameter `PLEX_UNSUB_EMAIL`
  * Comma separated string of emails to omit from sending
  * Optional

### Docker

`plex_notifier` can also be run as a container. With each release a Docker
container is built and published to Docker Hub. This might be an easier solution
for those not wanting to deal with setting up a Python environment with Tusk and
managing a scheduler like cron.

#### Running the Container

Docker must be installed on the system the container will run on. For Mac OS X
this can be done with Homebrew. For CentOS distros or Ubuntu distros yum or apt
can be used.

Pull the latest version of the container from [Docker Hub](https://hub.docker.com/r/discr33t/plex_notifier/),
which should be inline with the GitHub release.

Create a `.plex_envs` file in the home directory for the environment variables
necessary to run the application. A list can be found in the [Setting
Parameters](#setting-parameters) section above.

Run the Docker container passing the `.plex_envs` file.
```
docker run --env-file ~/.plex_envs plex_notifier:<version tag>
```

## Limitations

Currently only the `Movies` and `TV Shows` sections are queried, parsed and
formatted.

Currently the only mail provider supported is Gmail. This most likely will not
change.

## Disclaimers

Features and test coverage are limited. More robust features, and a more robust
test suite are on the roadmap.

## Contributions

This is an open source project under the MIT license. All contributions are
welcome. Feel free to submit issues or open pull requests for already opened
issues. For the foreseeable future the contributing guidelines will remain
simple.

1. Fork the project
2. Cut a feature branch
3. Write tests
4. Squash commits
5. Open pull request to `develop` branch

