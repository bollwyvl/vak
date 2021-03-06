from datetime import datetime
from pathlib import Path

from .. import config
from .. import core
from .. import logging


def predict(toml_path):
    """make predictions on dataset with trained model specified in config.toml file.
    Function called by command-line interface.

    Parameters
    ----------
    toml_path : str, Path
        path to a configuration file in TOML format.

    Returns
    -------
    None
    """
    toml_path = Path(toml_path)
    cfg = config.parse.from_toml(toml_path)

    if cfg.predict is None:
        raise ValueError(
            f'predict called with a config.toml file that does not have a PREDICT section: {toml_path}'
        )

    # ---- set up logging ----------------------------------------------------------------------------------------------
    timenow = datetime.now().strftime('%y%m%d_%H%M%S')
    logger = logging.get_logger(log_dst=cfg.prep.output_dir,
                                caller='eval',
                                timestamp=timenow,
                                logger_name=__name__)
    logger.info('Logging results to {}'.format(cfg.prep.output_dir))

    model_config_map = config.models.map_from_path(toml_path, cfg.predict.models)

    core.predict(cfg.predict.csv_path,
                 cfg.predict.checkpoint_path,
                 cfg.predict.labelmap_path,
                 cfg.predict.annot_format,
                 cfg.predict.to_format_kwargs,
                 model_config_map,
                 cfg.dataloader.window_size,
                 cfg.predict.num_workers,
                 cfg.spect_params.spect_key,
                 cfg.spect_params.timebins_key,
                 cfg.predict.spect_scaler_path,
                 cfg.predict.device,
                 logger)
