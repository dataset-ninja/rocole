Dataset **RoCoLe** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/b/G/hG/pZBsg0W1WUS17ysuixpeLf0pKvbQnrhMDJ9PfSg2OD83fTdaLfxryyDNLuJQYUiHwf4UqbkS9L8h0YtYCgwPzVD5o4ZqXV5ca3yZrOspGR0D0ZpmpKmUKKuZEQjx.tar)

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