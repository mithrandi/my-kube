from importlib.machinery import SourceFileLoader
isaacranks = SourceFileLoader('isaacranks', 'isaacranks.py').load_module()
dashboard = isaacranks.make('isaacranks-prod', 'Isaac Ranks (prod)')
