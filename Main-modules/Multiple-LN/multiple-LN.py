from torch import nn


class _DomainSpecificLayerNorm(nn.Module):
    _version = 1

    def __init__(self, num_features, num_domains, eps=1e-5,
                 track_running_stats=True):
        super(_DomainSpecificLayerNorm, self).__init__()
        self.lns = nn.ModuleList(
            [nn.LayerNorm(num_features, eps, ) for _ in range(num_domains)])

    nn.LayerNorm
    def reset_running_stats(self):
        for ln in self.lns:
            ln.reset_running_stats()

    def reset_parameters(self):
        for bn in self.bns:
            bn.reset_parameters()

    def _check_input_dim(self, input):
        raise NotImplementedError

    def forward(self, x, domain_label):
        self._check_input_dim(x)
        bn = self.lns[domain_label[0]]
        return ln(x), domain_label


class DomainSpecificBatchNorm2d(_DomainSpecificLayerNorm):
    def _check_input_dim(self, input):
        if input.dim() != 4:
            raise ValueError('expected 4D input (got {}D input)'
                             .format(input.dim()))