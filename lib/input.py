"""
Get parameters from user input.
"""

import configparser
import glob
import os
import os.path
import sys

from lib.format import ind, q

flags, args = {}, []
for s in sys.argv[1:]:
    if s.startswith('-'):  # format to {key:value} from -key=value
        flag = s.split('=')
        flags[flag[0][1:]] = flag[1] if len(flag) > 1 else None
    else:
        args.append(s)

if 'h' in flags or 'help' in flags:
    print("""usage: <dir|profile> [flags]
flags:
    -y: skip confirmation dialog
    -x=<value>, -ext=<value>: file extension to filter for
    -diff=<dir|url>: diff source to use""")
    sys.exit()

__all__ = ["get_params"]
__root__ = os.path.dirname(os.path.dirname(__file__))


def try_user(config, profile):
    """Recursively receives user input until valid profile name entered."""
    try:
        config[profile]  # pylint: disable=pointless-statement
        return profile
    except KeyError:
        profile = input(f"{q(profile)} not found:\t\t")
        return try_user(config, profile)


def get_config(config_filename):
    """Get parameters from config file."""
    raw_config = configparser.ConfigParser()

    config_filename = os.path.join(__root__, config_filename)
    if not os.path.exists(config_filename):
        raise FileNotFoundError("Config file not found.")
    raw_config.read(config_filename)

    profile = "DEFAULT"
    is_path = False
    if len(args) != 0:
        is_path = os.path.isdir(args[0])

        if not is_path:
            profile = args[0]
    elif input(f"Use {q(profile)} profile? [Y/n]\t").lower() == "n":
        profile = input("Config profile name:\t\t")
        profile = try_user(raw_config, profile)

    if profile in raw_config:
        config_user = raw_config[profile]
    else:
        raise ValueError(f'unknown profile/directory: "{profile}"')

    if is_path:
        config_user["ThemeDirectory"] = os.path.abspath(args[0])
    else:
        # backwards compat.
        config_user["ThemeDirectory"] = os.path.abspath(__root__+'/../'+config_user["ThemeDirectory"])

    if "ext" in flags:
        config_user["FileExtension"] = flags["ext"]
    elif "x" in flags:
        config_user["FileExtension"] = flags["x"]

    if "diff" in flags:
        config_user["DiffLocation"] = flags["diff"]
        config_user["UseLocalDiff"] = "no" if flags["diff"].startswith("http") else "yes"

    config = {
        "dir": config_user["ThemeDirectory"],
        "ext": config_user["FileExtension"],
        "uselocaldiff": config_user.getboolean("UseLocalDiff"),
        "location": config_user["DiffLocation"],
    }

    if config["uselocaldiff"] and not os.path.exists(config["location"]):
        raise FileNotFoundError("Diff file not found.")
    return config


def get_params():
    """Return parameters."""
    config = get_config("config.ini")
    print(ind(f"Themes directory:\t{config['dir']}"))
    print(ind(f"File extension:\t{config['ext']}"))
    print(ind(f"Use local diff:\t{config['uselocaldiff']}"))
    print(ind(f"Diff file location:\t{config['location']}"))

    filenames = glob.glob(os.path.join(
        config["dir"], "**", "*." + config["ext"]
    ), recursive=True)

    print(f"\nFound {len(filenames)} {config['ext']} files in {config['dir']}.")
    if 'y' not in flags:
        if os.environ.get("GITHUB_ACTIONS") != "true":
            input("Press enter to continue or Ctrl+C to cancel.")

    return config["uselocaldiff"], config['location'], filenames
