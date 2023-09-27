# **[foundations] images**

### To make sure your artwork looks great on all devices you support, learn how the system displays content on the screen and how to deliver art at the appropriate scale factors.
> 지원하는 모든 장치에서 예술 작품이 멋지게 보이도록 하려면 시스템이 화면에 콘텐츠를 표시하는 방법과 적절한 스케일 팩터로 예술을 전달하는 방법을 배우십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-images-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-images-intro-dark_2x.png)

# **Scale factors**

All platforms use a coordinates system based on measurements in points, which map to pixels in the display. A standard-resolution display has a 1:1 pixel density (also called @1x), where one pixel is equal to one point. High-resolution displays have a higher pixel density, such as 2:1 or 3:1. A 2:1 density (called @2x) has a scale factor of 2, and a 3:1 density (called @3x) has a scale factor of 3. Because of higher pixel densities, high-resolution displays demand images with more pixels.
> 모든 플랫폼은 디스플레이의 픽셀에 매핑되는 점 단위 측정을 기반으로 한 좌표계를 사용합니다. 표준 해상도 디스플레이는 1:1 픽셀 밀도(@1x라고도 함)를 가지며, 여기서 한 픽셀은 한 점과 같다. 고해상도 디스플레이는 2:1 또는 3:1과 같이 더 높은 픽셀 밀도를 갖는다. 2:1 밀도(@2x라고 함)는 스케일 팩터가 2이고, 3:1 밀도(@3x라고 함)는 스케일 팩터가 3이다. 고해상도 디스플레이는 더 높은 픽셀 밀도로 인해 더 많은 픽셀의 이미지를 요구한다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/images/images/image-resolution-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/images/images/image-resolution-dark_2x.png)

# **Formats**

As you create different types of images, consider the following recommendations.
> 다른 유형의 이미지를 생성할 때 다음 권장 사항을 고려하십시오.
>




# **Best practices**

**Supply high-resolution images for all artwork in your app, for every device you support.** You accomplish this by multiplying the number of pixels in each image by a specific scale factor. As you add each image to your project’s asset catalog, identify its scale factor by appending “@1x,” “@2x,” or “@3x” to its filename. Use the following values for guidance; for additional scale factors, see [Layout](../foundations/layout).
> 지원하는 모든 장치에 대해 앱의 모든 아트워크에 고해상도 이미지를 제공합니다. 각 이미지의 픽셀 수에 특정 배율을 곱하면 됩니다. 프로젝트의 자산 카탈로그에 각 이미지를 추가할 때 파일 이름에 "@1x", "@2x" 또는 "@3x"를 추가하여 축척 요소를 식별합니다. 다음 값을 기준으로 사용합니다. 추가 척도 인자는 레이아웃을 참조하십시오.
>




**In general, design images at the lowest resolution and scale them up to create high-resolution assets.** When you use resizable vectorized shapes, you might want to position control points at whole values so that they’re cleanly aligned at 1x. This positioning allows the points to remain cleanly aligned to the raster grid at higher resolutions, because 2x and 3x are multiples of 1x. In contrast, there are times when you don’t want to keep a shape perfectly aligned to the raster grid; for example, aligning a circle to the grid can make it appear flattened at the top and bottom.
> 일반적으로 가장 낮은 해상도로 이미지를 설계하고 크기를 조정하여 고해상도 자산을 생성합니다. 크기 조정 가능한 벡터 도형을 사용할 경우 제어점을 전체 값으로 배치하여 1x로 깔끔하게 정렬할 수 있습니다. 2x와 3x는 1x의 배수이기 때문에 이 위치를 통해 점이 더 높은 분해능에서 래스터 그리드에 깨끗하게 정렬됩니다. 이와는 대조적으로 래스터 그리드에 완벽하게 정렬된 모양을 유지하고 싶지 않은 경우가 있습니다. 예를 들어, 그리드에 원을 정렬하면 위쪽과 아래쪽에서 모양이 평평하게 보일 수 있습니다.
>




**Include a color profile with each image.** Color profiles help ensure that your app’s colors appear as intended on different displays. For guidance, see [Color management](https://developer.apple.com/design/human-interface-guidelines/foundations/color/#color-management).
> 각 이미지에 색상 프로파일을 포함합니다. 색상 프로파일은 앱의 색상이 다른 디스플레이에 의도한 대로 나타나도록 하는 데 도움이 됩니다. 자세한 내용은 색 관리를 참조하십시오.
>




**Always test images on a range of actual devices.** An image that looks great at design time may appear pixelated, stretched, or compressed when viewed on various devices.
> 항상 다양한 실제 장치에서 이미지를 테스트합니다. 디자인 시점에 훌륭하게 보이는 이미지는 다양한 장치에서 볼 때 픽셀화되거나 늘어나거나 압축된 상태로 나타날 수 있습니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or macOS.*
> iOS, iPadOS 또는 macOS에 대한 추가 고려 사항은 없습니다.
>




# **tvOS**

Layered images are at the heart of the Apple TV user experience. The system combines layered images, transparency, scaling, and motion to produce a sense of realism and vigor that evokes a personal connection as people interact with onscreen content.
> 계층화된 이미지는 Apple TV 사용자 경험의 핵심입니다. 이 시스템은 레이어드 이미지, 투명성, 스케일링 및 모션을 결합하여 사람들이 화면상의 콘텐츠와 상호 작용할 때 개인적인 연결을 불러일으키는 사실감과 활력감을 연출합니다.
>




### **Parallax effect**

*Parallax* is a subtle visual effect the system uses to convey depth and dynamism when an element is in focus. As an element comes into focus, the system elevates it to the foreground, gently swaying it while applying illumination that makes the element's surface appear to shine. After a period of inactivity, out-of-focus content dims and the focused element expands.
> 시차는 요소가 포커스에 있을 때 깊이와 역동성을 전달하기 위해 시스템이 사용하는 미묘한 시각적 효과입니다. 초점이 맞춰지면, 시스템은 요소 표면을 빛나게 하는 조명을 적용하면서 부드럽게 흔들면서 요소를 전경으로 올립니다. 일정 시간 동안 사용하지 않으면 초점이 맞지 않는 내용이 희미해지고 초점이 맞춰진 요소가 확장됩니다.
>




Layered images are required to support the parallax effect.
> 시차 효과를 지원하려면 계층화된 이미지가 필요합니다.
>




### **Layered images**

A *layered image* consists of two to five distinct layers that come together to form a single image. The separation between layers, along with use of transparency, creates a feeling of depth. As someone interacts with an image, layers closer to the surface elevate and scale, overlapping lower layers farther back and producing a 3D effect.
> 레이어드 이미지는 두 개에서 다섯 개의 서로 다른 레이어로 구성되어 하나의 이미지를 형성합니다. 투명성의 사용과 함께 레이어 간의 분리는 깊이의 느낌을 만듭니다. 누군가 이미지와 상호 작용함에 따라, 표면에 가까운 층은 상승하고 확장되며, 더 먼 뒤쪽에서 하위 층과 겹치고 3D 효과를 생성한다.
>




**IMPORTANT**Your tvOS [app icon](../foundations/app-icons) must use a layered image. For other focusable images in your app, including [Top Shelf](../components/system-experiences/top-shelf) images, layered images are strongly encouraged, but optional.
> 중요 tvOS 앱 아이콘은 계층형 이미지를 사용해야 합니다. 상단 선반 이미지를 포함하여 앱에서 포커스가 가능한 다른 이미지의 경우 계층화된 이미지가 권장되지만 선택 사항입니다.
>




**Use standard interface elements to display layered images.** If you use standard views and system-provided focus APIs — such as [FocusState](https://developer.apple.com/documentation/swiftui/focusstate) — layered images automatically get the parallax treatment when people bring them into focus.
> 표준 인터페이스 요소를 사용하여 계층화된 이미지를 표시할 수 있습니다. 표준 보기와 FocusState와 같은 시스템에서 제공한 포커스 API를 사용하면 계층화된 이미지가 포커스를 맞출 때 자동으로 시차 처리를 받습니다.
>




**Identify logical foreground, middle, and background elements.** In foreground layers, display prominent elements like a character in a game, or text on an album cover or movie poster. Middle layers are perfect for secondary content and effects like shadows. Background layers are opaque backdrops that showcase the foreground and middle layers without upstaging them.
> 논리적 전경, 중간 및 배경 요소를 식별합니다. 전경 레이어에서 게임 속 캐릭터나 앨범 표지 또는 동영상 포스터에 텍스트와 같이 눈에 띄는 요소를 표시합니다. 중간 레이어는 그림자와 같은 2차 콘텐츠와 효과에 완벽합니다. 배경 레이어는 전경 레이어와 중간 레이어를 업스테이지하지 않고 보여주는 불투명한 배경입니다.
>




**Generally, keep text in the foreground.** Unless you want to obscure text, bring it to the foreground layer for clarity.
> 일반적으로 텍스트를 전경에 둡니다. 텍스트를 모호하게 하고 싶지 않은 경우 명확성을 위해 텍스트를 전경 레이어로 가져오십시오.
>




**Keep the background layer opaque.** Using varying levels of opacity to let content shine through higher layers is fine, but your background layer must be opaque — you’ll get an error if it’s not. An opaque background layer ensures your artwork looks great with parallax, drop shadows, and system backgrounds.
> 배경 레이어를 불투명하게 유지합니다. 다양한 수준의 불투명도를 사용하여 상위 레이어를 통해 콘텐츠를 비추는 것은 좋지만 배경 레이어가 불투명해야 합니다. 그렇지 않으면 오류가 발생합니다. 불투명 배경 레이어는 시차, 드롭 섀도 및 시스템 배경과 함께 예술 작품이 멋지게 보이도록 합니다.
>




**Keep layering simple and subtle.** Parallax is designed to be almost unnoticeable. Excessive 3D effects can appear unrealistic and jarring. Keep depth simple to bring your content to life and add delight.
> 단순하고 미묘하게 레이어링하십시오. 시차는 거의 눈에 띄지 않도록 설계되었습니다. 과도한 3D 효과는 비현실적이고 불쾌하게 보일 수 있다. 깊이를 단순하게 유지하여 컨텐츠를 생생하게 만들고 즐거움을 더하십시오.
>




**Leave a safe zone around your content.** During focus and parallax, content around the edges of some layers may be cropped or difficult to see clearly as the image scales and moves. To ensure that your primary content is always visible, don’t put it too close to the edges. Be aware that the safe zone can vary, depending on the image size, layer depth, and motion, and that foreground layers are cropped more than background layers.
> 콘텐츠 주변에 안전 영역을 남겨 두십시오. 포커스 및 시차 중에 일부 레이어의 가장자리 주변의 콘텐츠가 잘리거나 이미지의 크기 조정 및 이동에 따라 선명하게 보기 어려울 수 있습니다. 기본 콘텐츠를 항상 볼 수 있도록 하려면 가장자리에 너무 가까이 두지 마십시오. 안전 영역은 이미지 크기, 레이어 깊이 및 움직임에 따라 달라질 수 있으며, 전경 레이어가 배경 레이어보다 더 잘립니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/images/images/icons-and-images-icon-safe-zone_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/images/images/icons-and-images-icon-safe-zone_2x.png)

**Always preview layered images.** To ensure your layered images look great on Apple TV, preview them throughout your design process using Xcode, the Parallax Previewer app for macOS, or the Parallax Exporter plug-in for Adobe Photoshop. Pay special attention as scaling and clipping occur, and readjust your images as needed to keep important content safe. After your layered images are final, preview them on an actual TV for the most accurate representation of what people will see. To download Parallax Previewer and Parallax Exporter, see [Resources](https://developer.apple.com/design/resources/#tvos-apps).
> 겹겹이 쌓인 이미지를 항상 미리 봅니다. 겹겹이 쌓인 이미지를 Apple TV에서 멋지게 보이려면 Xcode, MacOS용 Pararacle Previewer 앱 또는 Adobe Photoshop용 Paracle Exporter 플러그인을 사용하여 디자인 프로세스 전반에 걸쳐 미리 보십시오. 스케일링 및 클리핑이 발생할 때 각별히 주의를 기울이고, 중요한 콘텐츠를 안전하게 유지하기 위해 필요에 따라 이미지를 재조정하십시오. 레이어드된 이미지가 최종 완성되면 실제 TV에서 미리 보기하여 사람들이 볼 수 있는 이미지를 가장 정확하게 표현합니다. 시차 미리 보기 및 시차 내보내기 프로그램을 다운로드하려면 리소스를 참조하십시오.
>




**Use both the unfocused and focused states to determine the appropriate size for a layered image.** During the parallax effect, the system may crop background layers slightly, so keep essential content within a safe zone and include some additional space to make sure your content looks good.
> 비초점 상태와 초점 상태를 모두 사용하여 레이어 이미지에 적합한 크기를 결정합니다. 시차 효과 동안 시스템이 배경 레이어를 약간 잘라낼 수 있으므로 필수 콘텐츠를 안전 영역 내에 유지하고 콘텐츠가 보기 좋게 보이도록 추가 공간을 포함합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/foundations/images/images/layered-image-zones_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/images/images/layered-image-zones_2x.png)

The following formulas can help you calculate sizing for a layered image based on the size of the image when it’s not in focus.
> 다음 공식은 포커스가 맞지 않을 때 이미지 크기를 기준으로 계층화된 이미지의 크기를 계산하는 데 도움이 될 수 있습니다.
>




You can embed layered images in your app or retrieve them from a content server at runtime. To create layered images for inclusion within your app, use one of the following tools:
> 응용 프로그램에 계층화된 이미지를 포함하거나 런타임에 콘텐츠 서버에서 검색할 수 있습니다. 앱에 포함할 계층화된 이미지를 만들려면 다음 도구 중 하나를 사용하십시오.
>




- **Parallax Previewer app for macOS.** Parallax Previewer can import PNG files to serve as individual layers, layered images (`.lsr`) created with the Parallax Exporter plug-in, and layered Photoshop images (`.psd`). Parallax Previewer can export LSR files that you can import directly into an Xcode project.
- >  PNG 파일을 가져와 개별 레이어, 패러락스 익스포터 플러그인으로 만든 레이어드 이미지(thorlsr), 레이어드 포토샵 이미지(thorpsd)로 활용할 수 있다. 시차 미리 보기에서는 LSR 파일을 내보내고 이를 Xcode 프로젝트로 직접 가져올 수 있습니다.

- **Parallax Exporter Adobe Photoshop plug-in.** Use this plug-in to test your layered images in Photoshop and export them as LSR files that you can import directly into an Xcode project.
- >  시차 내보내기 Adobe Photoshop 플러그인. 이 플러그인을 사용하여 Photoshop에서 계층화된 이미지를 테스트하고 Xcode 프로젝트로 직접 가져올 수 있는 LSR 파일로 내보낼 수 있습니다.

- **Xcode.** Drag standard PNG files into your app’s asset catalog to serve as individual layers of an image stack in Xcode. Image stacks can be exported as LSR files. Xcode can also import LSR files.
- >  Xcode. 표준 PNG 파일을 앱의 자산 카탈로그로 끌어 Xcode에서 이미지 스택의 개별 계층으로 사용할 수 있습니다. 이미지 스택은 LSR 파일로 내보낼 수 있습니다. Xcode는 LSR 파일을 가져올 수도 있습니다.


If your app retrieves layered images from a content server at runtime, you must provide those images in runtime layered image (`.lcr`) format. You don’t create runtime layered images directly; you generate them from LSR files or Photoshop files using the `layerutil` command-line tool that Xcode provides. Runtime layered images are intended to be downloaded — don’t embed them within your app.
> 앱이 런타임에 콘텐츠 서버에서 계층화된 이미지를 검색하면 해당 이미지를 런타임 계층화된 이미지(--lcr') 형식으로 제공해야 합니다. 런타임 계층화 이미지는 직접 생성하지 않고 Xcode가 제공하는 layerutil 명령줄 도구를 사용하여 LSR 파일이나 Photoshop 파일에서 생성합니다. 런타임 계층화된 이미지는 다운로드하기 위한 것이므로 앱에 포함시키지 마십시오.
>




# **watchOS**

**In general, avoid transparency to keep image files small.** If you always composite an image on the same solid background color, it’s more efficient to include the background in the image. However, transparency is necessary in complication images, menu icons, and other interface icons that serve as template images, because the system uses it to determine where to apply color.
> 일반적으로 이미지 파일을 작게 유지하려면 투명도를 사용하지 마십시오. 항상 동일한 솔리드 배경 색상에 이미지를 합성하는 경우 이미지에 배경을 포함하는 것이 더 효율적입니다. 그러나 시스템이 색상을 적용할 위치를 결정하기 위해 사용하기 때문에 복잡도 이미지, 메뉴 아이콘 및 템플릿 이미지 역할을 하는 기타 인터페이스 아이콘에는 투명성이 필요합니다.
>




**Use autoscaling PDFs to let you provide a single asset for all screen sizes.** Design your image for the 40mm and 42mm screens at 2x. When you load the PDF, WatchKit automatically scales the image based on the device’s screen size, using the values shown below:
> 자동 스케일링 PDF를 사용하여 모든 화면 크기에 대해 단일 자산을 제공할 수 있습니다. 40mm 및 42mm 화면의 이미지를 2배 크기로 디자인하십시오. PDF를 로드할 때 WatchKit은 아래 표시된 값을 사용하여 장치의 화면 크기에 따라 이미지의 크기를 자동으로 조정합니다.
>




| Image type | Format |
| --- | --- |
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don't require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

| Platform | Scale factors |
| --- | --- |
| iOS | @2x and @3x |
| iPadOS | @2x |
| macOS, tvOS | @1x and @2x |
| watchOS | @2x |

| Image side | Focused/Safe zone size | Actual size |
| --- | --- | --- |
| Longest | Length of longest unfocused side + 70 pt | Length of longest focused side x 106% |
| Shortest | Proportional based on longest side | Proportional based on longest side |

| Screen size | Image scale |
| --- | --- |
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |
