from environs import Env

env = Env()
env.read_env()

BOT_TOKEN=env.str("BOT_TOKEN")
CHANNEL_ID=env.str("CHANNEL_ID")
ADMIN_ID=env.int("ADMIN_ID")
PHOTO_URL=env.str("PHOTO_URL")