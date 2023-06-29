# **[technologies-messages-for-business] message-bubble-content**

Message bubbles for standard interactive messages like Apple Pay payment requests, rich links, and pickers include a title, and can optionally include additional text and an image (which can be a video thumbnail). Optional text includes a primary, secondary, and tertiary subtitle, and an image title and subtitle.
> 애플 페이 결제 요청, 리치 링크, 피커와 같은 표준 대화형 메시지에 대한 메시지 버블은 제목을 포함하며, 선택적으로 추가 텍스트와 이미지(비디오 썸네일일 수 있음)를 포함할 수 있다. 선택적 텍스트에는 기본, 보조 및 3차 부제와 이미지 제목 및 부제가 포함됩니다.
>




# **Message bubble layout styles**

Message bubbles for standard interactive messages support the following layout styles.
> 표준 대화형 메시지에 대한 메시지 버블은 다음 레이아웃 스타일을 지원합니다.
>




| Style | Description | Size |
| --- | --- | --- |
| Icon | Horizontal bubble with an icon | 280x65 pt |
| Small | Horizontal bubble with a small image | 280x85 pt |
| Large | Horizontal bubble with a large image | 280x210 pt |

**Scale images based on the layout style.** When using the same image for multiple layout styles, provide a scaled image variation for each layout style. See [Image sizes](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/message-bubble-content#image-sizes) for sizing guidance.
> 레이아웃 스타일에 따라 이미지 크기를 조정합니다. 여러 레이아웃 스타일에 동일한 이미지를 사용할 경우 각 레이아웃 스타일에 대해 크기 조정된 이미지 변형을 제공합니다. 크기 조정 지침은 이미지 크기를 참조하십시오.
>




# **Images for message bubbles**

In a conversation, you can add an image to an interactive message bubble to provide greater context. When asking the customer to choose a product, for example, you could show product photos in a list picker to help people visually distinguish the items. Or, when requesting payment, you could show the item being purchased in the Apple Pay message bubble.
> 대화에서 대화형 메시지 버블에 이미지를 추가하여 더 큰 컨텍스트를 제공할 수 있습니다. 예를 들어 고객에게 제품을 선택하도록 요청할 때 목록 선택기에 제품 사진을 표시하여 사람들이 제품을 시각적으로 구분할 수 있습니다. 또는 결제를 요청할 때 Apple Pay 메시지 버블에 구매 중인 항목을 표시할 수 있습니다.
>




When you include a rich link to a video in a message bubble, you supply a thumbnail image that represents the video. The following size and resolution guidelines apply equally to images and video thumbnails.
> 메시지 버블에 비디오에 대한 리치 링크를 포함하면 비디오를 나타내는 축소 이미지를 제공합니다. 다음 크기 및 해상도 지침은 이미지 및 비디오 미리 보기에도 동일하게 적용됩니다.
>




### **Image sizes**

Provide images at the following sizes, based on where the images are used. When displaying the same image at multiple sizes, provide a separate image for each size.
> 이미지가 사용되는 위치에 따라 다음 크기로 이미지를 제공합니다. 동일한 이미지를 여러 크기로 표시하는 경우 각 크기에 대해 별도의 이미지를 제공합니다.
>




| Usage | Image Size |
| --- | --- |
| Interactive message message bubble (icon) | 40x40 pt (120x120 px @3x) |
| Interactive message message bubble (small) | 60x60 pt (180x180 px @3x) |
| Interactive message message bubble (large) | 263x150 pt (789x450 px @3x) |
| List picker image | 60x60 pt (180x180 px @3x) |

### **Designing high-resolution images**

A standard-resolution display has a 1:1 pixel density (or @1x), where one pixel is equal to one point. High-resolution displays have a higher pixel density, offering a scale factor of 2.0 or 3.0 (referred to as @2x and @3x). As a result, high-resolution displays demand images with more pixels.
> 표준 해상도 디스플레이는 1:1 픽셀 밀도(또는 @1x)를 가지며, 여기서 1 픽셀은 1 포인트와 같다. 고해상도 디스플레이는 픽셀 밀도가 높아 2.0 또는 3.0(@2x 및 @3x로 지칭됨)의 스케일 팩터를 제공합니다. 결과적으로 고해상도는 더 많은 픽셀을 가진 수요 이미지를 표시한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/ImageResolution-Graphic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/ImageResolution-Graphic_2x.png)

For example, suppose you have a standard resolution (@1x) image that’s 100x100 px. The @2x version of this image would be 200x200 px, and the @3x version would be 300x300 px.
> 예를 들어 표준 해상도(@1x) 이미지가 100x100px라고 가정합니다. 이 이미지의 @2x 버전은 200x200px이고 @3x 버전은 300x300px입니다.
>




**Always provide high-resolution images with a scale factor of @3x.** The @3x images you provide automatically scale down to @2x or @1x for display at lower resolutions.
> 항상 배율이 @3x인 고해상도 영상을 제공하십시오. 제공하는 @3x 영상은 낮은 해상도로 표시하기 위해 자동으로 @2x 또는 @1x로 축소됩니다.
>




**Produce artwork in the appropriate format.** Use de-interlaced PNG files for bitmap/raster artwork. Use JPEG for photos.
> 적절한 형식으로 아트워크를 생성하십시오. 비트맵/래스터 아트워크에 인터레이스 해제된 PNG 파일을 사용하십시오. 사진에는 JPEG를 사용합니다.
>




**Use the 8-bit color palette for PNG graphics that don’t require full 24-bit color.** Using an 8-bit color palette reduces file size without reducing image quality.
> 전체 24비트 색상이 필요 없는 PNG 그래픽의 경우 8비트 색상 팔레트를 사용하십시오. 8비트 색상 팔레트를 사용하면 이미지 품질을 저하시키지 않고 파일 크기를 줄일 수 있습니다.
>




**Optimize JPEG files to find a balance between size and quality.** Most JPEG files can be compressed without noticeable degradation of the resulting image. Even a small amount of compression can save significant disk space. Experiment with compression settings on each image to find the optimal value that yields an acceptable result.
> JPEG 파일을 최적화하여 크기와 품질의 균형을 찾으십시오. 대부분의 JPEG 파일은 결과 이미지의 현저한 저하 없이 압축할 수 있습니다. 적은 양의 압축으로도 상당한 디스크 공간을 절약할 수 있습니다. 각 이미지에 대한 압축 설정을 실험하여 허용 가능한 결과를 산출하는 최적의 값을 찾습니다.
>



