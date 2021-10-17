from typing import Dict

import torch
from param.lib.operator import (
    CallableOp,
    InPlaceOpByName,
    OperatorInterface,
    register_operator,
    register_operators,
)


# Unary
unary_ops: Dict[str, OperatorInterface] = {
    "aten::add_": InPlaceOpByName("add_"),
    "aten::clamp_": InPlaceOpByName("clamp_"),
}
register_operators(unary_ops)

callable_ops: Dict[str, OperatorInterface] = {
    "aten::add": CallableOp(torch.add),
    "aten::baddbmm": CallableOp(torch.baddbmm),
    "aten::bmm": CallableOp(torch.bmm),
    "aten::cat": CallableOp(torch.cat),
    "aten::matmul": CallableOp(torch.matmul),
    "aten::mean": CallableOp(torch.mean),
    "aten::mm": CallableOp(torch.mm),
    "aten::mul": CallableOp(torch.mul),
    "aten::relu": CallableOp(torch.nn.functional.relu),
    "aten::reshape": CallableOp(torch.reshape),
}
register_operators(callable_ops)

# register_operator("aten::clamp_", InPlaceOpByName("clamp_"))


"""
op_map: Dict[str, OperatorInterface] = {
    "Optimizer.step#FusedLAMB.step": None,
    "aten::_embedding_bag_backward": None,
    "aten::binary_cross_entropy_with_logits": CallableOp(
        torch.nn.functional.binary_cross_entropy_with_logits
    ),
    "aten::binary_cross_entropy_with_logits_backward": None,
    "aten::conj": None,
    "aten::contiguous": None,
    "aten::copy_": None,
    "aten::cumsum": None,
    "aten::detach": None,
    "aten::detach_": None,
    "aten::div": None,
    "aten::embedding_bag": None,
    "aten::empty": None,
    "aten::empty_like": None,
    "aten::expand": None,
    "aten::flatten": None,
    "aten::gather": None,
    "aten::gather_backward": None,
    "aten::layer_norm": None,
    "aten::le": None,
    "aten::log": None,
    "aten::narrow": None,
    "aten::native_layer_norm_backward": None,
    "aten::neg": None,
    "aten::new_empty_strided": None,
    "aten::ones_like": None,
    "aten::permute": None,
    "aten::pin_memory": None,
    "aten::record_stream": None,
    "aten::rsub": None,
    "aten::select": None,
    "aten::select_backward": None,
    "aten::set_": None,
    "aten::sigmoid": None,
    "aten::sigmoid_backward": None,
    "aten::slice": None,
    "aten::split_with_sizes": None,
    "aten::squeeze": None,
    "aten::sub": None,
    "aten::sum": None,
    "aten::t": None,
    "aten::tanh": None,
    "aten::tanh_backward": None,
    "aten::threshold_backward": None,
    "aten::to": None,
    "aten::transpose": None,
    "aten::unsqueeze": None,
    "aten::view": None,
    "aten::where": None,
    "aten::zero_": None,
    "aten::zeros": None,
    "aten::zeros_like": None,
    "enumerate(DataLoader)#_MultiProcessingDataLoaderIter.__next__": None,
    "fb::asynchronous_complete_cumsum": None,
    "fb::asynchronous_exclusive_cumsum": None,
    "fb::offsets_range": None,
    "fb::permute_pooled_embs_auto_grad": None,
    "fb::permute_sparse_features": None,
    "fb::split_embedding_codegen_lookup_rowwise_adagrad_function": None,
    "split_table_batched_embedding_bags_codegen": SplitTableBatchedEmbeddingOp(),
}
"""
