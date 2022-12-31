# **[inputs] pointing-devices**

## People can use pointing devices like a trackpad or mouse to supplement touchscreen and keyboard input, letting them use clicks and fluid, intuitive gestures to initiate actions.
> 트랙패드나 마우스와 같은 포인팅 장치를 사용하여 터치스크린과 키보드 입력을 보완하여 클릭과 유동적이고 직관적인 제스처를 사용하여 작업을 시작할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-pointing-devices-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-pointing-devices-intro_2x.png)

People appreciate the precision and flexibility that pointing devices offer. iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn’t replace touch.
> 사람들은 포인팅 장치가 제공하는 정밀도와 유연성을 높이 평가합니다. iPadOS는 포인터를 현재 컨텍스트에 자동으로 적용하고 터치스크린 장치에서 일반적인 작업을 단순화하는 정밀도 수준에서 풍부한 시각적 피드백을 제공하는 전통적인 포인터 경험을 기반으로 합니다. 아이패드OS 포인팅 시스템은 사람들에게 터치를 대체하지 않고 앱 및 콘텐츠와 상호 작용할 수 있는 추가적인 방법을 제공합니다.
>




On iPad, some people may continue to use touch only, whereas others may prefer to use the pointer or a combination of both. On a Mac, people typically use a mouse or trackpad to control the pointer, although many people prefer to use the keyboard to do so.
> 아이패드에서 어떤 사람들은 터치만 계속해서 사용하는 반면, 다른 사람들은 포인터나 둘의 조합을 사용하는 것을 선호할 수 있다. Mac에서는 일반적으로 마우스나 트랙패드를 사용하여 포인터를 제어하지만, 많은 사람들이 키보드를 사용하여 포인터를 제어하는 것을 선호합니다.
>




# **Best practices**

**Be consistent when responding to mouse and trackpad gestures.**People expect most gestures to work the same throughout the system, regardless of the app or game they’re using. On a Mac, for example, people rely on the “Swipe between pages” gesture to behave the same way whether they’re browsing individual document pages, webpages, or images.
> 마우스 및 트랙패드 제스처에 응답할 때 일관성을 유지합니다.사람들은 그들이 사용하는 앱이나 게임에 관계없이 대부분의 제스처가 시스템 전체에서 동일하게 작동하기를 기대한다. 예를 들어 Mac에서는 "페이지 간 전환" 제스처를 사용하여 개별 문서 페이지, 웹 페이지 또는 이미지를 검색할 때와 동일한 방식으로 동작합니다.
>




**Avoid redefining systemwide trackpad gestures.** Even in a game that uses app-specific gestures in a custom way, people expect systemwide gestures to be available for actions like revealing the Dock or Mission Control. Remember that Mac users can customize the gestures for performing systemwide actions.
> 시스템 전체의 트랙패드 제스처를 재정의하지 마십시오. 앱별 제스처를 사용자 지정 방식으로 사용하는 게임에서도 도킹 또는 미션 컨트롤을 표시하는 등의 작업에 시스템 전체의 제스처를 사용할 수 있기를 기대합니다. Mac 사용자는 시스템 전체 작업을 수행하기 위한 제스처를 사용자 지정할 수 있습니다.
>




**Provide a consistent experience in your iPadOS app, whether people are using touchscreen gestures, a pointing device, or a keyboard.** On their iPad, people tend to move fluidly between using touch and a connected input device, and they don’t want to learn different interactions for each mode or for each app they use.
> iPad에서는 터치스크린 제스처, 포인팅 장치 또는 키보드를 사용하는 경우에도 iPad OS 앱에서 일관된 경험을 제공합니다. iPad에서는 터치와 연결된 입력 장치 사이를 유동적으로 이동하는 경향이 있으며 각 모드 또는 사용하는 앱에 대해 서로 다른 상호 작용을 배우고 싶어하지 않습니다.
>




**Let people use the pointer to reveal and hide controls that automatically minimize or fade out.** In iPadOS, for example, people can reveal the minimized Safari toolbar by holding the pointer over it (the toolbar minimizes again when the pointer moves away). People can also move the pointer to reveal or hide playback controls while they watch a full-screen video.
> 예를 들어, iPadOS에서 사용자는 포인터를 사용하여 자동으로 최소화하거나 페이드아웃하는 컨트롤을 표시하거나 숨길 수 있습니다. 또한 사용자는 전체 화면 비디오를 보는 동안 재생 컨트롤을 표시하거나 숨길 수 있습니다.
>




**Enable a consistent experience when people press and hold a modifier key while interacting with objects in your app.** For example, if people can duplicate an object by pressing and holding the Option key while they drag that object, ensure the result is the same whether they drag using touch or the pointer.
> 사용자가 앱에서 개체와 상호 작용하는 동안 수정자 키를 길게 누를 때 일관된 환경을 사용할 수 있습니다. 예를 들어, 사용자가 개체를 끌 때 옵션 키를 길게 눌러 개체를 복제할 수 있는 경우 터치를 사용하든 포인터를 사용하여 끌든 결과가 동일한지 확인하십시오.
>




# **Platform considerations**

*No additional considerations for iOS. Not supported in tvOS or watchOS.*
> iOS에 대한 추가 고려 사항은 없습니다. TVOS 또는 워치에서 지원되지 않음운영 체제
>




# **iPadOS**

**Enable multiple selection in custom views when necessary.** In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself. For developer guidance, see [UIBandSelectionInteraction](https://developer.apple.com/documentation/uikit/uibandselectioninteraction).
> 필요한 경우 사용자 지정 보기에서 다중 선택을 사용할 수 있습니다. iPadOS 15 이상에서는 포인터를 클릭하여 여러 항목 위로 끌어 선택할 수 있습니다. 사람들이 이러한 방식으로 포인터를 사용하면 포인터가 포함된 항목을 선택하는 가시적인 직사각형으로 확장됩니다. 표준 비목록 컬렉션 보기는 기본적으로 이 상호 작용을 지원합니다. 사용자 정의 보기에서 다중 선택을 지원하려면 사용자가 직접 구현해야 합니다. 개발자 지침은 UIB 및 선택을 참조하십시오.상호작용.
>




**Distinguish between pointer and finger input only if it provides value.**For example, a scrubber can give people an additional way to target a location in a video when they’re using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.
> 값을 제공하는 경우에만 포인터와 손가락 입력을 구별합니다.예를 들어, 스크러버는 사용자가 포인터를 사용할 때 비디오의 위치를 지정하는 추가 방법을 제공할 수 있습니다. 이 시나리오에서 사용자는 포인터나 터치를 사용하여 플레이헤드를 끌 수 있지만 포인터를 사용하여 정확한 탐색 대상을 클릭할 수 있습니다.
>




### **Pointer shape and content effects**
> 포인터 모양 및 내용 효과
>




iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.
> 아이패드OS는 포인터의 모양과 동작을 통합하여 포인터가 대상으로 하는 항목에 초점을 맞춘다. 시스템에서 제공하는 포인터 효과를 지원하거나 사용자 환경에 맞게 수정할 수 있습니다.
>




By default, the pointer’s shape is a circle, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.
> 기본적으로 포인터의 모양은 원이지만, 사용자가 포인터를 특정 요소 또는 영역으로 이동할 때 시스템 정의 또는 사용자 정의 모양을 표시할 수 있습니다. 예를 들어, 포인터는 사람들이 텍스트 입력 영역 위로 이동할 때 익숙한 I-빔 모양을 자동으로 사용합니다.
>




Play

With a *content effect*, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. Depending on the type of content effect, the pointer can retain its current shape or transform into a shape that integrates with the element’s new appearance.
> 콘텐츠 효과를 사용하여 포인터 아래의 UI 요소 또는 영역도 사람이 포인터를 잡을 때 모양을 변경할 수 있습니다. 내용 효과의 유형에 따라 포인터는 현재 모양을 유지하거나 요소의 새 모양과 통합되는 모양으로 변환할 수 있습니다.
>




iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.
> iPadOS는 앱의 다양한 대화형 요소 유형에 초점을 맞추는 세 가지 콘텐츠 효과를 정의합니다.
>




The *highlight* effect transforms the pointer into a translucent, rounded rectangle that acts as a background for a control and includes a gentle parallax. The subtle highlighting and movement bring focus to the control without distracting people from their task. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.
> 하이라이트 효과는 포인터를 반투명하고 둥근 직사각형으로 변환하여 컨트롤의 배경 역할을 하며 완만한 시차를 포함합니다. 미묘한 강조 표시와 움직임은 사람들이 그들의 일에서 주의를 산만하게 하지 않고 조정기에 초점을 맞춘다. 기본적으로 iPadOS는 막대 단추, 탭 모음, 세그먼트화된 컨트롤 및 편집 메뉴에 강조 표시 효과를 적용합니다.
>




Play

The *lift* effect combines a subtle parallax with the appearance of elevation to make an element seem like it’s floating above the screen. As the pointer fades out beneath the element, iPadOS creates the illusion of lift by scaling the element up while adding a shadow below it and a soft specular highlight on top of it. By default, iPadOS applies the lift effect to app icons and to buttons in Control Center.
> 리프트 효과는 미묘한 시차와 상승의 모양을 결합하여 요소가 화면 위에 떠 있는 것처럼 보이게 합니다. 포인터가 요소 아래로 사라지면, 아이패드OS는 요소 아래에 그림자와 그 위에 부드러운 스펙타클 하이라이트를 추가하면서 요소를 위로 확장함으로써 상승하는 환상을 만들어낸다. 기본적으로 iPadOS는 앱 아이콘과 Control Center의 버튼에 리프트 효과를 적용합니다.
>




Play

*Hover* is a generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn’t transform the default pointer shape.
> 호버는 포인터가 요소 위로 이동할 때 요소에 사용자 지정 척도, 색조 또는 그림자 값을 적용할 수 있는 일반적인 효과입니다. 호버 효과는 사용자 지정 값을 결합하여 항목에 초점을 맞추지만 기본 포인터 모양은 변환되지 않습니다.
>




Play

### **Pointer accessories**

Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.
> 포인터 부속품은 포인터를 사용하여 현재 UI 요소와 상호 작용하는 방법을 이해하는 데 도움이 되는 시각적 표시기입니다. 예를 들어 크기 조정 요소에 접근하는 포인터는 요소가 특정 축을 따라 크기 조정을 허용함을 나타내기 위해 작은 화살표를 표시할 수 있습니다.
>




Unlike pointer shapes and content effects, accessories are secondary items that can combine with any pointer to communicate additional information. For developer guidance, see [UIPointerAccessory](https://developer.apple.com/documentation/uikit/uipointeraccessory).
> 포인터 모양 및 내용 효과와 달리 액세서리는 추가 정보를 전달하기 위해 포인터와 결합할 수 있는 보조 항목입니다. 개발자 지침은 UIPointerAccessory를 참조하십시오.
>




**Use clear, simple images to create custom accessories.** A pointer accessory is small, so it’s essential to create an image that communicates the pointer interaction without using too many details.
> 포인터 액세서리는 크기가 작기 때문에 너무 많은 세부 정보를 사용하지 않고 포인터 상호 작용을 전달하는 이미지를 만들어야 합니다.
>




**Consider using the accessory transition to signal a change in an element’s state or behavior.** In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects. For example, you could communicate that an add action has become unavailable by transitioning the pointer accessory from the `plus`symbol to the `circle.slash` symbol.
> 요소의 상태 또는 동작의 변화를 알리기 위해 액세서리 전환을 사용하는 것을 고려하십시오. 포인터 액세서리의 출현 및 소멸을 애니메이션화하는 것 외에도, 시스템은 콘텐츠 효과를 수반할 수 있는 액세서리 모양 및 위치 간의 전환을 애니메이션화합니다. 예를 들어 포인터 액세서리를 "플러스" 기호에서 "원"으로 전환하여 추가 작업을 사용할 수 없게 되었다는 것을 알릴 수 있습니다.기호를 자르다
>




### **Pointer magnetism**

iPadOS helps people use the pointer to target an element by making the element appear to attract the pointer. People can experience this magnetic effect when they move the pointer close to an element and when they flick the pointer toward an element.
> iPadOS는 요소가 포인터를 끌어당기는 것처럼 보이게 함으로써 사람들이 포인터를 사용하여 요소를 표적으로 삼을 수 있도록 도와줍니다. 사람들은 포인터를 요소에 가까이 움직일 때와 포인터를 요소 쪽으로 튕길 때 이러한 자기 효과를 경험할 수 있다.
>




When people move the pointer close to an element, the system starts transforming the pointer’s shape as soon as it reaches the element’s hit region. Because an element’s hit region typically extends beyond its visible boundaries, the pointer begins to transform before it appears to touch the element itself, creating the illusion that the element is pulling the pointer toward it.
> 사람들이 포인터를 요소에 가까이 움직이면, 시스템은 포인터가 요소의 적중 영역에 도달하자마자 포인터의 모양을 변환하기 시작한다. 요소의 적중 영역은 일반적으로 눈에 보이는 경계를 넘어 확장되기 때문에 포인터가 요소 자체에 닿기 전에 변형되기 시작하여 요소가 포인터를 그쪽으로 끌어당기는 것 같은 착각을 일으킨다.
>




Play

When people flick the pointer toward an element, iPadOS examines the pointer’s trajectory to discover the element that’s the most likely target. When there’s an element in the pointer’s path, the system uses magnetism to pull the pointer toward the element’s center.
> 사람들이 요소를 향해 포인터를 흔들면, iPadOS는 포인터의 궤적을 조사하여 가장 가능성이 높은 요소를 발견한다. 포인터의 경로에 요소가 있을 때, 시스템은 자력을 사용하여 포인터를 요소의 중심으로 당깁니다.
>




By default, iPadOS applies magnetism to elements that use the lift effect (like app icons) and the highlight effect (like bar buttons), but not to elements that use hover. Because a hover-enabled element doesn’t transform the default pointer shape, adding magnetism could be jarring and might make people feel that they’ve lost control of the pointer.
> 기본적으로 아이패드OS는 리프트 효과(앱 아이콘)와 하이라이트 효과(바 버튼)를 사용하는 요소에는 자력을 적용하지만 호버를 사용하는 요소에는 적용하지 않는다. 호버를 사용할 수 있는 요소는 기본 포인터 모양을 변환하지 않기 때문에 자력을 추가하는 것은 방해가 될 수 있으며 사람들이 포인터를 제어하지 못하는 것처럼 느끼게 할 수 있습니다.
>




The system also applies magnetism to text-entry areas, where it can help people avoid skipping to another line if they make unintended vertical movements while they’re selecting text.
> 이 시스템은 또한 문자 입력 영역에 자력을 적용하여 사람들이 문자를 선택하는 동안 의도하지 않은 수직 이동을 할 경우 다른 줄로 건너뛰는 것을 방지할 수 있습니다.
>




### **Standard pointers and effects**

**When possible, enable the system-provided content effects.** People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. To provide a consistent user experience, align your interactions with the design intent of each effect. Specifically:
> 가능하면 시스템에서 제공하는 콘텐츠 효과를 활성화합니다. 사람들은 시스템 전체에서 볼 수 있는 콘텐츠 효과에 빠르게 익숙해지고 일반적으로 자신의 경험이 사용하는 모든 앱에 적용되기를 기대합니다. 일관된 사용자 환경을 제공하려면 상호 작용을 각 효과의 설계 의도에 맞게 조정하십시오. 구체적으로:
>




- Use highlight for a small element that has a transparent background.
- >  배경이 투명한 작은 요소에는 강조 표시를 사용합니다.

- Use lift for a small element that has an opaque background.
- >  배경이 불투명한 작은 요소에는 리프트를 사용합니다.

- Use hover for large elements and customize the scale, tint, and shadow attributes as needed (for guidance, see [Customizing pointers](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices#customizing-pointers)).
- >  큰 요소에는 호버를 사용하고 필요에 따라 척도, 색조 및 그림자 속성을 사용자 지정합니다(자세한 내용은 포인터 사용자 지정 참조).


**Prefer the system-provided pointer appearances for standard buttons and text-entry areas.** You can help people feel more comfortable with your app when the pointer behaves in ways they expect.
> 표준 단추 및 텍스트 입력 영역에 대해 시스템에서 제공하는 포인터 모양을 선호합니다. 포인터가 원하는 방식으로 작동할 때 사용자의 앱을 더 편안하게 사용할 수 있도록 도와줄 수 있습니다.
>




**Add padding around interactive elements to create comfortable hit regions.** You might need to experiment to determine the right size for an element’s hit region. If the hit region is too small, it can make people feel that they have to be extra precise when interacting with the element. On the other hand, when an element’s hit region is too large, people can feel that it takes a lot of effort to pull the pointer away from the element. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element’s visible edges.
> 편안한 적중 영역을 만들려면 대화형 요소 주위에 패딩을 추가하십시오. 요소의 적중 영역에 적합한 크기를 결정하려면 실험이 필요할 수 있습니다. 타격 부위가 너무 작으면, 사람들이 요소와 상호 작용할 때 더 정확해야 한다고 느끼게 할 수 있다. 반면에, 요소의 적중 영역이 너무 클 때, 사람들은 포인터를 요소로부터 떼어내는 데 많은 노력이 필요하다는 것을 느낄 수 있다. 일반적으로 베젤이 포함된 요소 주변에 약 12포인트의 패딩을 추가하는 것이 효과적이며, 베젤이 없는 요소의 경우 요소의 보이는 가장자리 주변에 약 24포인트의 패딩을 추가하는 것이 효과적이다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/images/padding-for-button-with-bezel_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/images/padding-for-button-with-bezel_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/images/padding-for-glyph_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/images/padding-for-glyph_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/images/padding-for-button-without-bezel_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/images/padding-for-button-without-bezel_2x.png)

**Create contiguous hit regions for custom bar buttons.** If there’s space between the hit regions of adjacent buttons in a bar, people may experience a distracting motion when the pointer reverts briefly to its default shape as it moves between buttons.
> 사용자 지정 막대 단추를 위한 인접한 적중 영역을 만듭니다. 막대에서 인접한 단추의 적중 영역 사이에 공간이 있으면 포인터가 단추 사이를 이동할 때 기본 모양으로 잠시 되돌아갈 때 사람들이 산만한 동작을 경험할 수 있습니다.
>




**Specify the corner radius of a nonstandard element that receives the lift effect.** With the system-provided lift effect, the pointer transforms to match the element’s shape as it fades out. By default, the pointer uses the system-defined corner radius to transform into a rounded rectangle. If your element is a different shape — if it’s a circle, for example — you need to provide the radius so the pointer can animate seamlessly into the shape of the element. For developer guidance, see [UIPointerShape.roundedRect(_:radius:)](https://developer.apple.com/documentation/uikit/uipointershape/roundedrect_radius).
> 리프트 효과를 받는 비표준 요소의 모서리 반지름을 지정합니다. 시스템에서 제공하는 리프트 효과를 사용하면 포인터가 퇴화함에 따라 요소의 모양에 맞게 변환됩니다. 기본적으로 포인터는 시스템 정의 모서리 반지름을 사용하여 둥근 직사각형으로 변환합니다. 예를 들어 원과 같은 요소가 다른 모양인 경우 포인터가 요소 모양으로 원활하게 애니메이션될 수 있도록 반지름을 제공해야 합니다. 개발자 지침은 UIPointerShape.roundedRect(_:radius:)를 참조하십시오.
>




### **Customizing pointers**

**Prefer system-provided pointer effects for custom elements that behave like standard elements.** When a custom element behaves like a standard one, people generally expect to interact with it using familiar pointer interactions. For example, if buttons in a custom navigation bar don’t use the standard highlight effect, people might think they’re broken.
> 표준 요소처럼 동작하는 사용자 지정 요소에 대해 시스템에서 제공한 포인터 효과를 선호합니다. 사용자 지정 요소가 표준 요소처럼 동작할 때, 사람들은 일반적으로 친숙한 포인터 상호 작용을 사용하여 해당 요소와 상호 작용하기를 기대합니다. 예를 들어 사용자 지정 탐색 모음의 단추가 표준 강조 표시 효과를 사용하지 않는 경우 사용자는 단추가 손상되었다고 생각할 수 있습니다.
>




**Use pointer effects in consistent ways throughout your app.** For example, if your app helps people draw, enable a similar pointer experience for every drawing area in your app so that people can apply the knowledge they gain in one area to the others.
> 예를 들어, 앱이 사람들이 그림을 그리는 데 도움이 된다면 앱의 모든 그리기 영역에 대해 유사한 포인터 경험을 사용하여 한 영역에서 얻은 지식을 다른 영역에 적용할 수 있습니다.
>




**Avoid creating gratuitous pointer and content effects.** People notice when the appearance of the pointer or the UI element beneath it changes, and they expect the changes to be useful. Creating a purely decorative pointer effect can distract and even irritate people without providing any practical value.
> 불필요한 포인터와 내용 효과를 만들지 마십시오. 사람들은 포인터의 모양이나 그 아래에 있는 UI 요소가 변경될 때 이를 알아차리고 변경 사항이 유용할 것으로 기대합니다. 순수하게 장식적인 포인터 효과를 만드는 것은 실질적인 가치를 제공하지 않고 사람들을 산만하게 하고 심지어 짜증나게 할 수 있다.
>




**Keep custom pointer shapes simple.** Ideally, the pointer’s shape signals the action people can take in the current context without drawing too much attention to itself. If people don’t instantly understand your custom pointer shape, they’re likely to waste time trying to discover what the shape means.
> 사용자 지정 포인터 모양을 단순하게 유지합니다. 이상적으로는 포인터 모양은 사람들이 현재 컨텍스트에서 너무 많은 주의를 끌지 않고 수행할 수 있는 작업을 나타냅니다. 사용자 지정 포인터 모양을 즉시 이해하지 못하면 모양이 무엇을 의미하는지 알아보려고 시간을 낭비할 수 있습니다.
>




**Consider enhancing the pointer experience by displaying custom annotations that provide useful information.** For example, you could display X and Y values when people hold the pointer over a graphing area in your app. Keynote uses annotations to display the current width and height of a resizable image.
> 유용한 정보를 제공하는 사용자 지정 주석을 표시하여 포인터 경험을 향상시키는 것을 고려해 보십시오. 예를 들어, 사람들이 앱의 그래프 영역 위에 포인터를 놓을 때 X 및 Y 값을 표시할 수 있습니다. 키노트는 주석을 사용하여 크기 조정 가능한 이미지의 현재 너비와 높이를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/ios/images/useful-pointer-annotation_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/useful-pointer-annotation_2x.png)

**Avoid displaying instructional text with a pointer.** A pointer that displays instructional text can make an app seem complicated and difficult to use. Instead of providing instructions, prioritize clarity and simplicity in your interface, so that people can quickly grasp how to use your app whether they’re using the pointer or touching the screen.
> 지침 텍스트를 포인터로 표시하지 마십시오. 지침 텍스트를 표시하는 포인터는 앱을 복잡하고 사용하기 어렵게 만들 수 있습니다. 지침을 제공하는 대신 인터페이스에서 명확성과 단순성의 우선 순위를 지정하여 사용자가 포인터를 사용하든 화면을 터치하든 상관없이 앱을 사용하는 방법을 빠르게 파악할 수 있습니다.
>




