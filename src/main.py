import importlib

import torchfunc

import arguments

if __name__ == "__main__":
    torchfunc.seed(7)
    args = arguments.parser.get()
    module = importlib.import_module("commands." + args.command)
    module.run(args)
