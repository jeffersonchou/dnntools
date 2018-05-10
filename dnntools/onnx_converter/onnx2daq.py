import onnx
from onnx import helper, numpy_helper
import numpy as np
from dnntools import model_writer as mw
from dnntools.model_writer import ModelWriter


def convert(onnx_model: str, dest: str = 'nnmodel.daq') -> None:
    model = onnx.load(onnx_model)
    # for node in model.graph.node:
        # print('-----')
        # print(node)
        # print(node.input)
    for initializer in model.graph.initializer:
        print(initializer.name)
        print(initializer.data_type)
