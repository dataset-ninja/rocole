Dataset **RoCoLe** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTM1MF9Sb0NvTGUvcm9jb2xlLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogImhkcExwbFFQTmozaU1hWnVHZDQzVkxMbXh6ODI3ZkFrYXRSK2dDUXZQaE09In0=?response-content-disposition=attachment%3B%20filename%3D%22rocole-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='RoCoLe', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/c5yvn32dzg-2.zip).