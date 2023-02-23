_base_ = [
    '../configs/skeleton/posec3d/slowonly_r50_u48_240e_gym_limb.py'
]

model = dict(
    cls_head=dict(
        num_classes=4,
    ),
    test_cfg=dict(average_clips=None)
)

dataset_type = 'PoseDataset'
ann_file_train = '../data/train_label0-3.pkl'
ann_file_val = '../data/val_label0-3.pkl'


data = dict(
    videos_per_gpu=16,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        ann_file=ann_file_train,
    ),
    val=dict(
        type=dataset_type,
        ann_file=ann_file_val,
    ),
    test=dict(
        type=dataset_type,
        ann_file=ann_file_val,
    ))

load_from = 'pretrained_models/slowonly_r50_u48_240e_gym_limb-c0d7b482.pth'
gpu_ids = range(0, 1)

checkpoint_config = dict(interval=10)

total_epochs = 500

evaluation = dict(
    interval=1,
    save_best='top_k_accuracy',
    topk=(1, ),
)
log_config = dict(interval=5, hooks=[dict(type='TextLoggerHook')])

