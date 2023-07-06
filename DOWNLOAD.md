Dataset **RoCoLe** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/C/9p/nqiW3HLG5V2PLTdBNY1dpARkettuDLczQowzsdhAwrwqS3eOaCt959OxFnOJ0uTiTxHqPfM0AsK6EHXGZb7MBJrZEMvpvTJnhHPtVSriwnvWRkOQR13myY8x7y1W.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='RoCoLe', dst_path='~/dtools/datasets/RoCoLe.tar')
```
The data in original format can be 🔗[downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/c5yvn32dzg-2.zip)