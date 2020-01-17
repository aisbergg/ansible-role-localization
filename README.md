# Ansible Role: `aisbergg.locales`

Sets [locales](https://wiki.archlinux.org/index.php/locale) on Linux systems.

## Requirements

None.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `locales_language_packs` | `[]` | List of language packs to be installed. |
| `locales_present` | `[]` | List of locales to be present. |
| `locales_absent` | `[]` | List of locales to be absent. |
| `locales_default` | `{"lang": "en_US.UTF-8", "lc_all": "en_US.UTF-8"}` | Mapping of default locales variables. |
| `locales_default.lang` |  | `LANG` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.language` |  | `LANGUAGE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_address` |  | `LC_ADDRESS` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_collate` |  | `LC_COLLATE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_ctype` |  | `LC_CTYPE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_identification` |  | `LC_IDENTIFICATION` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_monetary` |  | `LC_MONETARY` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_messages` |  | `LC_MESSAGES` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_measurement` |  | `LC_MEASUREMENT` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_name` |  | `LC_NAME` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_numeric` |  | `LC_NUMERIC` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_paper` |  | `LC_PAPER` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_telephone` |  | `LC_TELEPHONE` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_time` |  | `LC_TIME` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |
| `locales_default.lc_all` |  | `LC_ALL` variable. See [man pages](http://man7.org/linux/man-pages/man7/locale.7.html) for information. |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  vars: 
    locales_present:
      - de_DE.UTF-8
      - en_US.UTF-8
    locales_absent:
      - fr_FR.UTF-8
    locales_default:
      language: de_DE
      lang: de_DE.UTF-8
      lc_all: de_DE.UTF-8
  roles:
    - role: aisbergg.locales
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
