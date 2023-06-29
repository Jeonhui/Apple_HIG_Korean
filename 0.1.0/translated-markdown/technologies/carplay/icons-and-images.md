# **[technologies-carplay] icons-and-images**

## **Image size and resolution**

The coordinate system CarPlay uses to place content onscreen is based on measurements in points, which map to pixels in the display. A standard-resolution display has a 1:1 pixel density (or @1x), where one pixel is equal to one point. High-resolution displays have a higher pixel density, offering a scale factor of 2.0 or 3.0 (referred to as @2x and @3x). As a result, high-resolution displays demand images with more pixels.
> CarPlay가 화면에 콘텐츠를 배치하는 데 사용하는 좌표계는 디스플레이의 픽셀에 매핑되는 점 단위의 측정을 기반으로 합니다. 표준 해상도 디스플레이는 1:1 픽셀 밀도(또는 @1x)를 가지며, 여기서 1 픽셀은 1 포인트와 같다. 고해상도 디스플레이는 픽셀 밀도가 높아 2.0 또는 3.0(@2x 및 @3x로 지칭됨)의 스케일 팩터를 제공합니다. 결과적으로 고해상도는 더 많은 픽셀을 가진 수요 이미지를 표시한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ImageResolution-Graphic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ImageResolution-Graphic_2x.png)

For example, suppose you have a standard resolution (@1x) image that's 100px × 100px. The @2x version of this image would be 200px × 200px, and the @3x version would be 300px × 300px.
> 예를 들어 표준 해상도(@1x) 이미지가 100px x 100px라고 가정합니다. 이 이미지의 @2x 버전은 200px x 200px이고, @3x 버전은 300px x 300px입니다.
>




**Supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork in your app.** The system automatically shows the correct images and scales them appropriately, based on the resolution and size of the car’s display.
> 앱에 있는 모든 CarPlay 아트워크에 대해 @2x 및 @3x의 스케일 팩터로 고해상도 이미지를 제공합니다. 시스템은 자동으로 올바른 이미지를 보여주고 자동차 디스플레이의 해상도와 크기에 따라 적절히 스케일을 조정합니다.
>




# **App icon**

Every CarPlay app needs a beautiful, memorable icon that stands out on the Home screen and is easy to tap while driving.
> 모든 카플레이 앱은 홈 스크린에서 눈에 띄고 운전 중 탭하기 쉬운 아름답고 기억에 남는 아이콘이 필요하다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/audiobooks_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/audiobooks_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/maps_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/maps_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/message_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/message_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/music_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/music_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/now_playing_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/now_playing_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/phone_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/phone_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/podcasts_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/podcasts_2x.png)

**Mirror your iPhone app icon.** A well-designed app icon works well in CarPlay and on iPhone, without the need for a second design.
> iPhone 앱 아이콘을 미러링합니다. 잘 디자인된 앱 아이콘은 두 번째 디자인 없이도 CarPlay와 iPhone에서 잘 작동합니다.
>




**Don't use black for your icon’s background.** Lighten a black background or add a border so the icon doesn’t blend into the display background.
> 아이콘 배경에 검은색을 사용하지 마십시오. 검은색 배경을 밝게 하거나 테두리를 추가하여 아이콘이 화면 배경에 섞이지 않도록 합니다.
>




**Provide a single focus point.** Design an icon with a single, centered point that immediately captures attention and clearly identifies your app.
> 단일 포커스 포인트를 제공합니다. 중앙에 위치한 단일 포인트로 아이콘을 디자인하면 즉시 주의를 끌 수 있고 앱을 명확하게 식별할 수 있습니다.
>




**Embrace simplicity.** Add details cautiously. If an icon’s content or shape is overly complex, the details can be hard to discern. Design an icon that instantly communicates your app’s purpose. For example, the Messages app icon uses a chat bubble, which is universally associated with messaging.
> 단순함을 받아들이고 세부사항을 조심스럽게 추가하세요. 아이콘의 내용이나 모양이 지나치게 복잡한 경우 세부 사항을 식별하기 어려울 수 있습니다. 앱의 목적을 즉시 전달하는 아이콘을 디자인합니다. 예를 들어, 메시지 앱 아이콘은 일반적으로 메시징과 관련된 채팅 버블을 사용합니다.
>




**Make sure your icon is opaque (not transparent), and keep the background simple.** Give your icon a simple background so it doesn’t overpower other app icons nearby. You don’t need to fill the entire icon with content.
> 아이콘이 불투명한지(투명하지 않음) 확인하고 배경을 단순하게 유지하십시오. 아이콘이 근처의 다른 앱 아이콘을 압도하지 않도록 간단한 배경을 지정하십시오. 아이콘 전체를 내용으로 채울 필요는 없습니다.
>




**Use words only when they’re essential or part of a logo.** An app’s name appears below its icon on the Home screen. Don’t include nonessential words that repeat the name or tell people what to do with your app, like “Play.” If your design includes any text, emphasize words that relate to the actual content your app offers.
> 앱 이름은 홈 스크린의 아이콘 아래에 표시됩니다. 이름을 반복하거나 "재생"과 같이 사용자의 앱으로 무엇을 해야 하는지 알려주는 불필요한 단어를 포함하지 마십시오 디자인에 텍스트가 포함된 경우 앱에서 제공하는 실제 콘텐츠와 관련된 단어를 강조합니다.
>




**Don’t include photos, screenshots, or interface elements.** Photographic details can be very hard to see at small sizes. Screenshots are too complex for an app icon and don’t generally help communicate your app’s purpose. Interface elements in an icon are misleading and confusing.
> 사진, 스크린샷 또는 인터페이스 요소를 포함하지 마십시오. 작은 크기에서는 사진 세부 정보를 보기가 매우 어려울 수 있습니다. 스크린샷은 앱 아이콘에 비해 너무 복잡하고 일반적으로 앱의 목적을 전달하는 데 도움이 되지 않습니다. 아이콘의 인터페이스 요소는 오해의 소지가 있고 혼란스럽다.
>




**Don’t place your app icon throughout the interface.** It can be confusing to see an icon used for different purposes throughout an app. Instead, consider incorporating your icon’s color scheme. See [Color](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/visual-design#color).
> 앱 아이콘을 인터페이스 전체에 배치하지 마십시오. 앱 전체에서 다른 용도로 사용되는 아이콘을 보는 것은 혼란스러울 수 있습니다. 대신 아이콘의 색 구성표를 통합하는 것을 고려하십시오. 색상을 참조하십시오.
>




**Keep icon corners square.** The system applies a mask that rounds icon corners automatically.
> 아이콘 모서리를 정사각형으로 유지합니다. 시스템은 아이콘 모서리를 자동으로 둥글게 만드는 마스크를 적용합니다.
>




For app icon design guidance, see [App icons](../foundations/app-icons).
> 앱 아이콘 설계 지침은 앱 아이콘을 참조하십시오.
>




### **App icon sizes**

In addition to its iPhone app icons, your app must include CarPlay app icons in the following sizes.
> iPhone 앱 아이콘 외에도 다음 크기의 CarPlay 앱 아이콘이 포함되어 있어야 합니다.
>




---

120px by 120px (60pt by 60pt @2x)
> 가로 120cm, 세로 120cm(가로 60cm, 세로 60cm @2x)
>




---

180px by 180px (60pt by 60pt @3x)
> 180°x180°(60ptx60pt@3x)
>




---

# **Custom icons**

If your app includes tasks or modes that can’t be represented by an [SF Symbol](../foundations/sf-symbols), or if you need icons that match your app’s style, you can create custom icons. A custom icon, sometimes called a template, discards color information and uses a mask to produce the appearance you see onscreen in a navigation bar or tab bar.
> 앱에 SF 기호로 나타낼 수 없는 작업이나 모드가 포함되어 있거나 앱 스타일에 맞는 아이콘이 필요한 경우 사용자 지정 아이콘을 만들 수 있습니다. 템플릿이라고도 하는 사용자 지정 아이콘은 색상 정보를 무시하고 마스크를 사용하여 탐색 모음이나 탭 모음에서 화면에 표시되는 모양을 만듭니다.
>




**Create simple, recognizable designs.** Too many details can make an icon appear sloppy or unreadable. Strive for a design most people will interpret correctly and won’t find offensive.
> 단순하고 알아보기 쉬운 디자인을 만듭니다. 세부 정보가 너무 많으면 아이콘이 엉성하거나 읽을 수 없게 될 수 있습니다. 대부분의 사람들이 올바르게 해석하고 불쾌하게 생각하지 않는 디자인을 위해 노력하세요.
>




**Design a solid color icon with transparency, anti-aliasing, and no drop shadow.** The system ignores all color information, so there’s no need to use more than one fill color. Allow transparency to define the shape of the icon.
> 투명도, 앤티앨리어싱 및 드롭 섀도우가 없는 솔리드 컬러 아이콘을 디자인합니다. 시스템은 모든 색상 정보를 무시하므로 두 개 이상의 채우기 색상을 사용할 필요가 없습니다. 투명도를 통해 아이콘 모양을 정의할 수 있습니다.
>




**Keep your icons consistent.** Whether you use only custom icons or mix custom and system icons, all icons in your app should be the same in terms of size, level of detail, perspective, and stroke weight. If you want an icon to look like it's related to the system icon family, use a very thin stroke to draw it. A 1-point stroke (2px for @2x, 3px for @3x) works well for most icons.
> 사용자 지정 아이콘만 사용하든, 사용자 지정 아이콘과 시스템 아이콘을 혼합하든, 앱의 모든 아이콘은 크기, 세부 정보 수준, 원근감 및 스트로크 무게 면에서 동일해야 합니다. 아이콘이 시스템 아이콘 패밀리와 관련된 것처럼 보이려면 매우 얇은 스트로크를 사용하여 아이콘을 그립니다. 1점 스트로크(@2x의 경우 2px, @3x의 경우 3px)는 대부분의 아이콘에서 잘 작동합니다.
>




**Provide two versions of custom tab bar icons.** Provide icons for both the selected and unselected states. The selected icon is often a filled-in version of the unselected icon, but some designs call for variations to this approach. For example, Apple apps sometimes invert icon interiors, increase or reduce strokes, and enclose the icon within a shape, such as a circle.
> 두 가지 버전의 사용자 지정 탭 모음 아이콘을 제공하십시오. 선택한 상태와 선택하지 않은 상태 모두에 대한 아이콘을 제공하십시오. 선택한 아이콘은 종종 선택되지 않은 아이콘의 채워진 버전이지만, 일부 설계에서는 이 접근 방식을 변경해야 합니다. 예를 들어, 애플 앱은 때때로 아이콘 내부를 반전시키고, 획을 늘리거나 줄이며, 아이콘을 원과 같은 모양으로 둘러싸기도 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_A.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_A.svg)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_B.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_B.svg)

**Don’t use text in a tab bar icon.** If you need to show text, display a title beneath the tab and adjust its placement accordingly.
> 탭 표시줄 아이콘에 텍스트를 사용하지 마십시오. 텍스트를 표시하려면 탭 아래에 제목을 표시하고 그에 따라 위치를 조정하십시오.
>




### **Custom icon sizes**

| Navigation bar icon size | Tab bar icons |
| --- | --- |
| 108px × 108px (36pt × 36pt @3x) | 108px × 108px (36pt × 36pt @3x) |
| 72px × 72px (36pt × 36pt @2x) | 72px × 72px (36pt × 36pt @2x) |
