# Overview

Ruby interview exercises


# Prerequisites

Candidates are expected to have folling installed on their local machine
* Ruby 2.7.x or 3.x
* Rspec

# Exercises

List of interview exercises

* [1-lru-cache](./1-lru-cache/README.md)

# Setup

Comamnds to install prerequisites

## Install Ruby

```bash
# install rvm to manage multiple ruby versions.  
for KEY in 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB; do
    gpg --keyserver keyserver.ubuntu.com                 --recv-keys $KEY || \
    gpg --keyserver pgp.mit.edu                          --recv-keys $KEY || \
    gpg --keyserver hkp://pool.sks-keyservers.net        --recv-keys $KEY || \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys $KEY;
done

\curl -sSL https://get.rvm.io | bash

# install ruby
rvm install 2.7.5
rvm use 2.7.5
```

## Install Rspec

```bash
gem install rspec
```
