# **[content] image-views**

## An image view displays a single image — or in some cases, an animated sequence of images — on a transparent or opaque background.
> 이미지 보기는 투명하거나 불투명 배경에 단일 이미지(경우에 따라서는 애니메이션 이미지 순서)를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/image-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/image-view-intro-dark_2x.png)

Within an image view, you can stretch, scale, size to fit, or pin the image to a specific location. Image views are typically not interactive.
> 이미지 보기 내에서 이미지를 특정 위치에 맞게 확장, 축소, 크기 조정 또는 고정할 수 있습니다. 이미지 보기는 일반적으로 상호 작용하지 않습니다.
>




# **Best practices**

**Use an image view when the primary purpose of the view is simply to display an image.** In rare cases where you might want an image to be interactive, configure a system-provided [button](../components/menus-and-actions/buttons) to display the image instead of adding button behaviors to an image view.
> 보기의 주요 목적이 단순히 이미지를 표시하는 것일 때 이미지 보기를 사용하십시오. 드물게 이미지가 대화식으로 표시되도록 하려면 이미지 보기에 단추 동작을 추가하는 대신 시스템이 제공하는 단추를 구성하여 이미지를 표시하십시오.
>




**If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view.** [SF Symbols](../foundations/sf-symbols) provides a large library of streamlined, vector-based images that you can render with various colors and opacities. An [interface icon](../foundations/icons) (also called a glyph or template image) is typically a bitmap image in which the nontransparent pixels can receive color. Both symbols and interface icons can use the accent colors people choose.
> 인터페이스에 아이콘을 표시하려면 이미지 보기 대신 기호나 인터페이스 아이콘을 사용하십시오. SF 심볼은 다양한 색상과 불투명도로 렌더링할 수 있는 벡터 기반 이미지의 큰 라이브러리를 제공합니다. 인터페이스 아이콘(글립 또는 템플릿 이미지라고도 함)은 일반적으로 투명하지 않은 픽셀이 색을 수신할 수 있는 비트맵 이미지이다. 기호와 인터페이스 아이콘은 모두 사람들이 선택하는 악센트 색상을 사용할 수 있다.
>




# **Content**

An image view can contain rich image data in various formats, like PNG, JPEG, and PDF. For more guidance, see [Images](../foundations/images).
> 이미지 보기에는 PNG, JPEG 및 PDF와 같은 다양한 형식의 풍부한 이미지 데이터가 포함될 수 있습니다. 자세한 내용은 이미지를 참조하십시오.
>




**Take care when overlaying text on images.** Compositing text on top of images can decrease both the clarity of the image and the legibility of the text. To help improve the results, ensure the text contrasts well with the image, and consider ways to make the text object stand out, like adding a text shadow or background layer.
> 이미지에 텍스트를 오버레이할 때 주의하십시오. 이미지 위에 텍스트를 합성하면 이미지의 선명도와 텍스트 가독성이 모두 저하될 수 있습니다. 결과를 개선하는 데 도움이 되도록 텍스트와 이미지가 잘 대비되도록 하고 텍스트 그림자나 배경 레이어를 추가하는 등 텍스트 개체를 돋보이게 하는 방법을 고려하십시오.
>




**Aim to use a consistent size for all images in an animated sequence.**When you prescale images to fit the view, the system doesn't have to perform any scaling. In cases where the system must do the scaling, performance is generally better when all images are the same size and shape.
> 애니메이션 시퀀스의 모든 이미지에 대해 일관된 크기를 사용합니다.보기에 맞게 이미지를 미리 축척할 때 시스템에서 축척을 수행할 필요가 없습니다. 시스템이 스케일링을 수행해야 하는 경우 일반적으로 모든 이미지의 크기와 모양이 동일할 때 성능이 더 우수합니다.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS.*
> iOS 또는 iPad OS에 대한 추가 고려 사항 없음.
>




# **macOS**

**If your app needs an editable image view, use an image well.** An [image well](../components/selection-and-input/image-wells) is an image view that supports copying, pasting, dragging, and using the Delete key to clear its content.
> 앱에 편집 가능한 이미지 보기가 필요한 경우 이미지를 잘 사용하십시오. 이미지 웰은 복사, 붙여넣기, 끌기 및 삭제 키를 사용하여 콘텐츠를 지울 수 있는 이미지 보기입니다.
>




**Use an image button instead of an image view to make a clickable image.** An [image button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/#image-buttons) contains an image or icon, appears in a view, and initiates an instantaneous app-specific action.
> 클릭 가능한 이미지를 만들려면 이미지 뷰 대신 이미지 버튼을 사용하십시오. 이미지 버튼은 이미지 또는 아이콘을 포함하고 뷰에 나타나며 즉각적인 앱별 동작을 시작합니다.
>




# **tvOS**

Many tvOS images combine multiple layers with transparency to create a feeling of depth. For guidance, see [Layered Images](https://developer.apple.com/design/human-interface-guidelines/foundations/images/#layered-images).
> 많은 tvOS 이미지들은 깊이의 느낌을 만들기 위해 투명성과 함께 여러 레이어를 결합한다. 자세한 내용은 레이어드 이미지를 참조하십시오.
>




# **watchOS**

**Use SwiftUI to create animations when possible.** If necessary, you can use WatchKit to animate a sequence of images within an image element. For developer guidance, see [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable).
> 스위프트 사용가능한 경우 애니메이션을 만드는 UI입니다. 필요한 경우 WatchKit을 사용하여 이미지 요소 내에서 일련의 이미지를 애니메이션화할 수 있습니다. 개발자 지침은 WKImageAnimatable을 참조하십시오.
>



