import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    if host.system_info.distribution != "centos" and host.system_info.release == "8":
        # check if locale is present
        available_locales = host.check_output("locale -a")
        assert "de_DE.utf8" in available_locales

        # check if locale is absent
        assert "en_US.utf8" not in available_locales

    # check if locale is set
    locale_conf = host.file("/etc/locale.conf")
    lc_vars = {
        "LANGUAGE": "de_DE",
        "LANG": "de_DE.UTF-8",
        "LC_ADDRESS": "de_DE.UTF-8",
        "LC_COLLATE": "de_DE.UTF-8",
        "LC_CTYPE": "de_DE.UTF-8",
        "LC_IDENTIFICATION": "de_DE.UTF-8",
        "LC_MONETARY": "de_DE.UTF-8",
        "LC_MESSAGES": "de_DE.UTF-8",
        "LC_MEASUREMENT": "de_DE.UTF-8",
        "LC_NAME": "de_DE.UTF-8",
        "LC_NUMERIC": "de_DE.UTF-8",
        "LC_PAPER": "de_DE.UTF-8",
        "LC_TELEPHONE": "de_DE.UTF-8",
        "LC_TIME": "de_DE.UTF-8",
    }
    for k, v in lc_vars.items():
        assert locale_conf.contains("{}=\"{}\"".format(k, v))
