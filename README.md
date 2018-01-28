# plex_notifier

[![Build Status](https://travis-ci.org/co-llabs/plex_notifier.svg?branch=master)](https://travis-ci.org/co-llabs/plex_notifier)
[![GitHub (pre-)release](https://img.shields.io/github/release/co-llabs/plex_notifier/all.svg)]()
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

#### Table of Contents

1. [Description](#description)
2. [Setup](#setup)
    * [Setup](#requirements)
    * [Setting Parameters](#setting-parameters)
3. [Limitations](#limitations)
4. [Disclaimers](#disclaimers)

## Description

A little Python program that queries a Plex server for recently added media and
sends an email to the subscribed users with a list of said media.

## Setup

### Requirements

* Python 2.7
* plexapi pip package
* Gmail account configured to send from an application
  For Gmail reference look [here](http://naelshiab.com/tutorial-send-email-python/)

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

## Limitations

Currently only Python 2.7 is supported. A future upgrade to Python 3 is in the
roadmap as part of Milestone 2

Currently only the `Movies` section is queried, parsed and formatted. A future
update to include the `TV Shows` section is in the roadmap for Milestone 2.

Currently the only mail provider supported is Gmail. This most likely will not
change.

## Disclaimers

A first release candidate has been cut. This is minimal viable product but
stable. Features are limited, test coverage is limited, and there is no
automated build pipeline yet. A `develop` branch has been cut and work will
continue there. A build pipeline is on the roadmap for Milestone 2.

This is a first draft and quick pass at a README. A better README and more
detailed documentation will follow.

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

