""" Select AttentionFactory Method

Hacked together by Ross Wightman
"""
import torch
from .se import SqueezeExcite, SqueezeExciteV2
from .eca import EfficientChannelAttn, CircularEfficientChannelAttn
from .cbam import ConvBlockAttn, LightConvBlockAttn


def create_attn(attn_type, channels, **kwargs):
    module_cls = None
    if attn_type is not None:
        if isinstance(attn_type, str):
            attn_type = attn_type.lower()
            if attn_type == 'se':
                module_cls = SqueezeExcite
            elif attn_type == 'sev2':
                module_cls = SqueezeExciteV2
            elif attn_type == 'eca':
                module_cls = EfficientChannelAttn
            elif attn_type == 'ceca':
                module_cls = CircularEfficientChannelAttn
            elif attn_type == 'cbam':
                module_cls = ConvBlockAttn
            elif attn_type == 'lcbam':
                module_cls = LightConvBlockAttn
            else:
                assert False, "Invalid attn module (%s)" % attn_type
        else:
            module_cls = attn_type
    if module_cls is not None:
        return module_cls(channels, **kwargs)
    return None