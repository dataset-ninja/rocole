import os
import sys
from pathlib import Path

import supervisely as sly

# my_app = sly.AppService()
# api: sly.Api = my_app.public_api

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

# TASK_ID = int(os.environ["TASK_ID"])
# TEAM_ID = int(os.environ['context.teamId'])
# WORKSPACE_ID = int(os.environ['context.workspaceId'])

logger = sly.logger

# project_name = "Robusta coffee leaves"
dataset_name = "ds"
work_dir = "coffee_leaves"
coffee_leaves_url = (
    "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/c5yvn32dzg-2.zip"
)

arch_name = "c5yvn32dzg-2.zip"

images_folder_name = "export"
annotation_folder_name = "Annotations"
annotations_file_name = "RoCoLE-json.json"
annotations_for_shape = "RoCoLE-coco.json"
images_arh_name = "RoCoLe-voc.tar.gz"

images_ext = ".jpeg"

sample_percent = round(int(100) * 15.6)
class_name = "coffee_leaf"

batch_size = 30

obj_class = sly.ObjClass(class_name, sly.Polygon)
# obj_class_collection = sly.ObjClassCollection([obj_class])

class_names = (
    "healthy",
    "unhealthy",
    "rust_level_1",
    "rust_level_2",
    "rust_level_3",
    "rust_level_4",
    "red_spider_mite",
)

obj_classes = [sly.ObjClass(class_name, sly.Polygon) for class_name in class_names]

cls_to_obj_classes = {cls_name: obj_class for cls_name, obj_class in zip(class_names, obj_classes)}


# tag_name_classification = "classification"
# tag_meta_classification = sly.TagMeta(tag_name_classification, sly.TagValueType.ANY_STRING)
# tag_name_state = "state"
# tag_meta_state = sly.TagMeta(tag_name_state, sly.TagValueType.ANY_STRING)
# tag_metas = [tag_meta_classification, tag_meta_state]

# tag_meta_collection = sly.TagMetaCollection(tag_metas)

meta = sly.ProjectMeta(obj_classes=obj_classes)

# storage_dir = sly.app.get_data_dir()
storage_dir = "./APP_DATA"
work_dir_path = os.path.join(storage_dir, work_dir)
sly.io.fs.mkdir(work_dir_path)
archive_path = os.path.join(work_dir_path, arch_name)

image_name_to_polygon = {}
image_name_to_classification = {}
image_name_to_shape = {}
