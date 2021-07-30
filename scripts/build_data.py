from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    for key in meta:
        if meta[key] is not None and isinstance(meta[key], str):
            meta[key] = meta[key].replace("'", "&#39;")
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
