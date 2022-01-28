# Changelog

All notable changes to this project will be documented in this file.

- [3.1.0 (2022-01-28)](#3.1.0-2022-01-28)
- [3.0.0 (2021-10-11)](#300-2021-10-11)
- [2.4.0 (2020-08-22)](#240-2020-08-22)
- [2.3.2 (2020-06-05)](#232-2020-06-05)
- [2.3.1 (2020-05-22)](#231-2020-05-22)
- [2.2.0 (2020-04-18)](#220-2020-04-18)
- [2.1.0 (2020-03-22)](#210-2020-03-22)
- [2.0.0 (2020-03-10)](#200-2020-03-10)
- [1.1.2 (2020-02-07)](#112-2020-02-07)
- [1.1.1 (2020-01-31)](#111-2020-01-31)
- [1.1.0 (2020-01-22)](#110-2020-01-22)
- [1.0.0 (2020-01-17)](#100-2020-01-17)

---

<a name="3.1.0"></a>
## [3.1.0](https://github.com/aisbergg/ansible-role-localization/compare/v3.0.0...3.1.0) (2022-01-28)

### CI Configuration

- fix automatic release and publish process

### Chores

- include changelog in bump commits


<a name="3.0.0"></a>
## [3.0.0](https://github.com/aisbergg/ansible-role-localization/compare/v2.4.0...v3.0.0) (2021-10-11)

### Bug Fixes

- date

### CI Configuration

- add Github action for automatic releases

### Chores

- update changelog
- update development configs
- **.ansible-lint:** update linter config
- **.pre-commit-config.yaml:** bump pre-commit hook versions
- **CHANGELOG.tpl.md:** update changelog template
- **requirements.yml:** add role requirements

### Code Refactoring

- drop support for Ansible < 2.10


<a name="2.4.0"></a>
## [2.4.0](https://github.com/aisbergg/ansible-role-localization/compare/v2.3.2...v2.4.0) (2020-08-22)

### Bug Fixes

- sorting of LC vars
- locales cfg path for debian

### Chores

- update changelog


<a name="2.3.2"></a>
## [2.3.2](https://github.com/aisbergg/ansible-role-localization/compare/v2.3.1...v2.3.2) (2020-06-05)

### Bug Fixes

- quotes


<a name="2.3.1"></a>
## [2.3.1](https://github.com/aisbergg/ansible-role-localization/compare/v2.2.0...v2.3.1) (2020-05-22)

### Bug Fixes

- version comparison

### Code Refactoring

- clean up


<a name="2.2.0"></a>
## [2.2.0](https://github.com/aisbergg/ansible-role-localization/compare/v2.1.0...v2.2.0) (2020-04-18)

### Chores

- **CHANGELOG.md:** update changelog

### Documentation

- clarify use of `localization_language_packs` option

### Features

- use uppercase names for locales


<a name="2.1.0"></a>
## [2.1.0](https://github.com/aisbergg/ansible-role-localization/compare/v2.0.0...v2.1.0) (2020-03-22)

### Bug Fixes

- linting
- correct Ansible version requirement

### Chores

- update changelog
- add bump2version configuration

### Features

- pass the list of requirements directly to package module


<a name="2.0.0"></a>
## [2.0.0](https://github.com/aisbergg/ansible-role-localization/compare/v1.1.2...v2.0.0) (2020-03-10)

### Chores

- update changelog

### Features

- add options to set keymap and timezone


<a name="1.1.2"></a>
## [1.1.2](https://github.com/aisbergg/ansible-role-localization/compare/v1.1.1...v1.1.2) (2020-02-07)

### Bug Fixes

- linting
- for EL7

### Chores

- update changelog


<a name="1.1.1"></a>
## [1.1.1](https://github.com/aisbergg/ansible-role-localization/compare/v1.1.0...v1.1.1) (2020-01-31)

### Chores

- update changelog

### Code Refactoring

- surround pipe symbol with one space
- split long command into several lines


<a name="1.1.0"></a>
## [1.1.0](https://github.com/aisbergg/ansible-role-localization/compare/v1.0.0...v1.1.0) (2020-01-22)

### Chores

- update changelog

### Features

- add compatibility with CentOS8


<a name="1.0.0"></a>
## [1.0.0]() (2020-01-17)

Initial Release
