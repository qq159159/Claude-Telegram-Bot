from os import getenv, path

from yaml import safe_load

if not path.exists("config/config.yml"):
    # load env vars
    bot_token = getenv("BOT_TOKEN")
    user_ids = [int(user_id) for user_id in getenv("USER_IDS").split(",")]
    claude_api = getenv("CLAUDE_API")
    bard_api = getenv("BARD_API")
else:
    # load yaml config
    with open("config/config.yml", "r") as f:
        config_yaml = safe_load(f)
    # config parameters
    bot_token = config_yaml["telegram"]["bot_token"]
    user_ids = config_yaml["telegram"]["user_ids"]
    claude_api = config_yaml["claude"]["api"]
    bard_api = config_yaml["bard"]["api"]

assert bot_token is not None and user_ids is not None
assert claude_api is not None or bard_api is not None

single_mode = claude_api is None or bard_api is None
default_mode = "Claude" if claude_api is not None else "Bard"
