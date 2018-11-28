import json
import config

#Load the configuration
with open('config.json') as f:
    data = json.load(f)
cfg = config.Config()
cfg.watchDirectory = data["WatchDirectory"]

print(cfg.watchDirectory)
