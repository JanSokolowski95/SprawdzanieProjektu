import yaml

import torch


def get(args):
    """<short summary>.

    <extended summary>

    Parameters
    ----------
    args : type
        <argument description>

    Returns
    -------
    type
        <return description>

    """
    with open(args.optimizer) as optimizer_file:
        settings = yaml.load(optimizer_file)
    name = settings.pop("name")
    return lambda parameters: getattr(torch.optim, name)(parameters, **settings)
