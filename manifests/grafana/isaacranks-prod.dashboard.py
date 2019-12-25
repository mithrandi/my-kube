from importlib.machinery import SourceFileLoader
isaacranks = SourceFileLoader('isaacranks', 'isaacranks.py').load_module()
dashboard = isaacranks.make('prod', 'Isaac Ranks (prod)')
