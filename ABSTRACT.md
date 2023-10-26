The authors present a dataset of robusta coffee leaf images known as **RoCoLe**. It comprises 1560 leaf images that exhibit visible red mites and spots to indicate the presence of coffee leaf rust in infection cases. For healthy cases, the dataset includes images without such structures. The dataset also contains annotations describing objects (leaves), their state (healthy or unhealthy), and the severity of disease based on the leaf area with spots. All images were captured under real-world conditions in the same coffee plant field using a smartphone camera. The RoCoLe dataset serves as a valuable resource for assessing the performance of machine learning algorithms in image segmentation and classification tasks related to plant disease recognition.

RoCoLe offers a collection of images in binary and multiclass classification problems, as well as segmentation tasks related to plant disease recognition. This dataset encompasses images of both the upper and back sides of coffee leaves collected from robusta coffee crops, representing various states (*healthy* and *unhealthy*), the presence of diseases (*rust* and *red_spider_mite*), and varying levels of infection severity. Specifically, there are four images available for each of the 390 coffee plants included in the study, resulting in a total of 1560 robusta coffee leaf images in the dataset.

## Experimental Design, Materials, and Methods
The images of healthy and unhealthy coffee plant leaves were captured using a 5-MP smartphone camera at a working distance of 200-300 mm, without employing zoom. These images were taken under diverse real-world conditions, including variations in lighting (cloudy, sunny, and windy days), backgrounds (other plants and weeds), and temperature levels (high and low humidity). This diversity ensures that the dataset includes real and representative samples of coffee plants. The study area featured a crop with 390 coffee plants, and for each coffee plant, images of both the upper and back sides of healthy and infected leaves were obtained, resulting in the collection of 1560 images in total.

To enhance RoCoLe's capabilities for evaluating machine learning methods, a comprehensive annotation process was conducted to label all 1560 coffee leaf images. This annotation process was carried out using a [Labelbox](https://labelbox.com/) and encompassed two types of annotations: object segmentation and classification.

The RoCoLe dataset features annotations for object segmentation, where each object (leaf) is recognized and segmented. Additionally, each object is classified as healthy, exhibiting red mite presence, or manifesting rust at various severity levels, namely *rust_level_1*, *rust_level_2*, *rust_level_3*, and *rust_level_4*. The determination of rust infection severity was based on the OIRSA method, summarized in the following table:

| Level | Affected leaf area (spots) |
|-------|-----------------------------|
| 1     | 1–5%                        |
| 2     | 6–20%                       |
| 3     | 21–50%                      |
| 4     | >50%                        |
