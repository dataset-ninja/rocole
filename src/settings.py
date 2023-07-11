from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License, Research

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "RoCoLe"
PROJECT_NAME_FULL: str = "RoCoLe: A Robusta Coffee Leaf Images Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Industry] = [Industry.Agriculture(), Research.Biological()]
CV_TASKS: List[CVTask] = [
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_YEAR: int = 2019
HOMEPAGE_URL: str = "https://data.mendeley.com/datasets/c5yvn32dzg/2"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1635253
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/rocole"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/c5yvn32dzg-2.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "healthy": [0, 128, 128],
    "unhealthy": [230, 25, 75],
    "rust_level_1": [255, 250, 200],
    "rust_level_2": [255, 215, 180],
    "rust_level_3": [250, 190, 212],
    "rust_level_4": [170, 110, 40],
    "red_spider_mite": [128, 0, 0],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.sciencedirect.com/science/article/pii/S2352340919307693"
CITATION_URL: Optional[str] = "https://data.mendeley.com/datasets/c5yvn32dzg/2"
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Escuela Superior Politecnica Agropecuaria de Manabi, Equador",
    "Universidad de Santiago de Chile",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "http://www.espam.edu.ec/",
    "https://www.usach.cl/",
]
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }
    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
