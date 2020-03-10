# Ansible Role: `aisbergg.localization`

This Ansible role takes care of the localization settings on Linux systems. It includes options to set the [locales](https://wiki.archlinux.org/index.php/locale), [keymap](https://wiki.archlinux.org/index.php/Keyboard_configuration_in_console) and timzone.

## Requirements

None.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `localization_language_packs` | `[]` | List of language packs to be installed. For Debian distributions package names are: `language-pack-*` and for CentOS 8 `glibc-langpack-*` |
| `localization_locales_present` | `[]` | List of locales to be present. |
| `localization_locales_absent` | `[]` | List of locales to be absent. |
| `localization_locales_default` | `{"lang": "en_US.UTF-8", "lc_all": "en_US.UTF-8"}` | Mapping of default locales variables. |
| `localization_locales_default.lang` |  | `LANG` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.language` |  | `LANGUAGE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_address` |  | `LC_ADDRESS` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_collate` |  | `LC_COLLATE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_ctype` |  | `LC_CTYPE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_identification` |  | `LC_IDENTIFICATION` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_monetary` |  | `LC_MONETARY` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_messages` |  | `LC_MESSAGES` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_measurement` |  | `LC_MEASUREMENT` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_name` |  | `LC_NAME` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_numeric` |  | `LC_NUMERIC` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_paper` |  | `LC_PAPER` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_telephone` |  | `LC_TELEPHONE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_time` |  | `LC_TIME` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_locales_default.lc_all` |  | `LC_ALL` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `localization_keymap` | `en` | The keymap to be set. |
| `localization_keymap_toggle` | | The alternative keymap to be set. |
| `localization_timezone` |  | The timezone to be set. If left empty, the timezone stays untouched. |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  vars: 
    localization_locales_present:
      - de_DE.UTF-8
      - en_US.UTF-8
    localization_locales_absent:
      - fr_FR.UTF-8
    localization_locales_default:
      language: de_DE
      lang: de_DE.UTF-8
      lc_all: de_DE.UTF-8
    localization_keymap: de
    localization_keymap_toggle: de-latin1
    localization_timezone: Europe/Berlin
  roles:
    - aisbergg.localization
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
