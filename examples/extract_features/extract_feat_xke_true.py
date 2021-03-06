from tools import pra_run


pra_run.extract_features(
    emb_import_path='./results/FB13/TransE/1527033688/',
    neg_rate=2,
    bern=True,
    feature_extractors=['pra'],
    cuda_device=1,
    use_ids=False,
    g_hat_info=None,
    data_to_use='onefold'
)
