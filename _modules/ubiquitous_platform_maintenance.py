import dateutil.parser
from datetime import timezone
from ubiquitous_platform import NGINX_EXTRA_CONFIG


def set_maintenance(basename, enabled, target_time_iso=None):
    """
    Enable or disable maintenance pages.

    :param str basename: Platform basename.
    :param bool enabled: Whether or not maintenance pages should be enabled.
    :param str target_time_iso: Recovery time in ISO 8601 format (e.g. 2018-12-25T09:30:00+00:00).
    """
    if enabled and not target_time_iso:
        raise ArgumentError('target_time_iso is required when enabling maintenance')
    # Make sure the basename is valid -- we don't need the result
    __salt__['ubiquitous_platform.get_config'](basename)

    config_file = NGINX_EXTRA_CONFIG.format(basename=basename, config='maintenance')
    if enabled:
        target_time = dateutil.parser.parse(target_time_iso).astimezone(timezone.utc)
        __salt__['file.write'](config_file, "\n".join([
            'set $platform_maintenance 1;',
            "set $platform_target_time_human '{}';".format(target_time.strftime('%H:%M %Z')),           # 09:00 UTC
            "set $platform_target_time_iso '{}';".format(target_time.strftime('%Y%m%dT%H%M')),          # 20180904T0900
            "set $platform_target_time_datetime '{}';".format(target_time.strftime('%Y-%m-%dT%H:%MZ')), # 2018-09-04T09:00Z
        ]))
    else:
        __salt__['file.remove'](config_file)
    __salt__['service.reload']('nginx')

    return True
