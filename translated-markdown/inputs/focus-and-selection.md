# **[inputs] focus-and-selection**

## Focus visually identifies the onscreen object that will respond to interactions like a mouse click, a keyboard command, or a button press on a remote.
> 포커스는 마우스 클릭, 키보드 명령 또는 리모컨의 버튼 누르기와 같은 상호 작용에 응답하는 화면 개체를 시각적으로 식별합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-focus-and-selection-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-focus-and-selection-intro_2x.png)

Focus enables a simplified, element-based navigation experience tailored to situations where the current input device doesn’t necessarily enable access to every part of the screen. For example, when people use their finger, a pointing device, or Apple Pencil, they can target any onscreen area, often with pixel-level precision. In contrast, when people use an input device like a keyboard, remote, or game controller, they target specific interface elements, not pixels.
> 포커스는 현재 입력 장치가 반드시 화면의 모든 부분에 액세스할 수 있는 것은 아닌 상황에 맞춘 단순화된 요소 기반 탐색 경험을 가능하게 한다. 예를 들어, 사람들이 손가락, 포인팅 장치 또는 애플 펜슬을 사용할 때, 그들은 종종 픽셀 수준의 정밀도로 화면 상의 모든 영역을 대상으로 할 수 있다. 대조적으로, 사람들이 키보드, 원격 또는 게임 컨트롤러와 같은 입력 장치를 사용할 때, 그들은 픽셀이 아닌 특정 인터페이스 요소를 목표로 한다.
>




It’s important to understand that focusing an item is not always the same as selecting it. In tvOS, for example, people generally use one gesture to focus an interface component and another gesture to select it. In iPadOS, bringing focus to an item can also select it, as long as selection doesn’t produce behavior that might be distracting, like switching to a new view or showing an alert.
> 항목에 초점을 맞추는 것이 항상 항목을 선택하는 것과 같지는 않다는 것을 이해하는 것이 중요합니다. 예를 들어, TV OS에서 사람들은 일반적으로 인터페이스 구성 요소에 초점을 맞추기 위해 하나의 제스처를 사용하고 다른 제스처를 사용하여 선택합니다. iPadOS에서 항목에 초점을 맞추면 항목을 선택할 수도 있습니다. 새 보기로 전환하거나 알림을 표시하는 것처럼 주의를 산만하게 할 수 있는 동작이 선택되지 않는 경우입니다.
>




Different platforms communicate focus using different visual indicators. For example, iPadOS and macOS can call attention to a focused item by drawing a ring around it or highlighting it; tvOS generally uses the [parallax effect](https://developer.apple.com/design/human-interface-guidelines/foundations/images#parallax-effect) to give the focused item an appearance of depth and liveliness. The system’s implementation of focus effects and interactions is sometimes called a *focus system* or *focus model*.
> 서로 다른 플랫폼은 서로 다른 시각적 표시기를 사용하여 초점을 전달합니다. 예를 들어, 아이패드OS와 맥 OS는 초점이 맞춰진 항목에 링을 그리거나 강조 표시함으로써 주의를 환기시킬 수 있다. 시스템의 초점 효과와 상호 작용의 구현은 때때로 초점 시스템 또는 초점 모델이라고 불린다.
>




# **Best practices**

**Rely on system-provided focus effects.** System-defined focus effects can provide experiences that feel tactile, responsive, and fluid. In tvOS, for example, when people swipe quickly to move focus from one side of the screen to the other, the system communicates a natural sense of inertia as focus subtly accelerates and then decelerates through onscreen items. Consider creating a custom focus system only if it’s absolutely necessary.
> 시스템이 제공하는 초점 효과에 의존합니다. 시스템 정의 초점 효과는 촉각, 반응성 및 유체를 느끼는 경험을 제공할 수 있습니다. 예를 들어, TV OS에서 사람들이 화면의 한쪽에서 다른 쪽으로 초점을 이동하기 위해 빠르게 스와이프할 때, 시스템은 초점이 미묘하게 가속된 다음 화면 항목을 통해 감속할 때 자연스러운 관성을 전달한다. 꼭 필요한 경우에만 맞춤형 포커스 시스템을 만드는 것을 고려해 보십시오.
>




**Let people control focus movement as much as possible.** People rely on the focus system to help them know where they are in your app, so it’s important to avoid moving focus to a different item without their interaction. An exception is when a previously focused item no longer exists; in this scenario, it’s less confusing to move focus to a new item than it is to hide the visual focus indication.
> 사람들은 포커스 시스템에 의존하여 앱에서 자신의 위치를 알 수 있으므로 상호 작용 없이 다른 항목으로 포커스를 이동하지 않는 것이 중요합니다. 이 시나리오에서는 시각적 초점 표시를 숨기는 것보다 이전에 초점을 맞춘 항목이 더 이상 존재하지 않는 경우가 예외입니다.
>




# **Platform considerations**

*Not supported in iOS or watchOS.*
> iOS 또는 Watch에서 지원되지 않음운영 체제
>




# **iPadOS, macOS**

**Let people bring focus to content elements — such as list items, text fields, and search fields — but not to controls like buttons, sliders, and toggles.** In iPadOS and macOS, people use [Full Keyboard Access](https://support.apple.com/en-mn/guide/mac-help/mchlc06d1059/mac) to reach every control through keyboard interactions, so you need only enable focus for key content features in your app. To learn more about supporting focus behavior in your iPadOS app, see [Keyboard navigation on iPad](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/#keyboard-navigation-on-ipad).
> iPadOS 및 macOS에서는 전체 키보드 액세스를 사용하여 키보드 상호 작용을 통해 모든 컨트롤에 액세스하므로 앱의 주요 콘텐츠 기능에만 포커스를 설정하면 됩니다. iPadOS 앱에서 포커스 동작을 지원하는 방법에 대한 자세한 내용은 iPad의 키보드 탐색을 참조하십시오.
>




**Use consistent visual appearances for focused items.** For example, give a focused list item an inverted highlight that uses your app’s accent color, and give an unfocused list item a light gray highlight when it’s selected (for developer guidance, see [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview/) and [NSTableView](https://developer.apple.com/documentation/appkit/nstableview/)).
> 초점을 맞춘 항목에 일관된 시각적 모양을 사용합니다. 예를 들어 초점을 맞춘 목록 항목에 앱의 액센트 색상을 사용하는 반전된 강조 표시를 지정하고 초점을 맞추지 않은 목록 항목을 선택할 때 옅은 회색 강조 표시를 지정합니다(개발자 지침은 UICollectionView 및 NSTableView 참조).
>




**In general, use a focus ring for a text or search field, but use a highlight in a list or collection.** Although you can use a focus ring to draw attention to an item that fills a cell, like a photo, it’s easier for people to view lists and collections when an entire row is highlighted.
> 일반적으로 텍스트나 검색 필드에는 포커스 링을 사용하지만 목록이나 컬렉션에는 강조 표시를 사용합니다. 사진처럼 셀을 채우는 항목에 주의를 끌 수는 있지만 전체 행이 강조 표시될 때 사용자가 목록과 컬렉션을 쉽게 볼 수 있습니다.
>




# **tvOS**

**Make sure people can bring focus to every element in your app.** People rely on using directional gestures on a remote or game controller (or pressing the arrow keys on an attached keyboard) to reach every onscreen element.
> 사용자는 리모컨이나 게임 컨트롤러에서 방향 제스처를 사용하거나 연결된 키보드에서 화살표 키를 눌러 모든 화면 요소에 액세스할 수 있습니다.
>




**In a full-screen experience, let people use gestures to interact with the content, not to move focus.** When an item displays in full screen, it doesn’t show focus, so people naturally assume that their gestures will affect the object, and not its focus state.
> 전체 화면 환경에서는 포커스를 이동하는 것이 아니라 콘텐츠와 상호 작용하기 위해 제스처를 사용하도록 합니다. 항목이 전체 화면에 표시되면 포커스가 표시되지 않으므로 사람들은 자연스럽게 제스처가 포커스 상태가 아닌 개체에 영향을 미칠 것이라고 가정합니다.
>




**Avoid displaying a pointer.** People expect to navigate a fixed number of items by changing focus, not by trying to drag a tiny pointer around a huge screen. While free-form movement might make sense during gameplay, such as when looking for a hidden object or flying a plane, use the focus model when people navigate menus and other interface elements. If your app requires a pointer, make sure it’s highly visible and feels integrated with your experience.
> 포인터를 표시하지 마십시오. 사람들은 큰 화면 주위에서 작은 포인터를 끌지 않고 초점을 변경하여 일정한 수의 항목을 탐색할 수 있습니다. 숨겨진 물체를 찾거나 비행기를 띄울 때와 같이 게임 플레이 중 자유 형태의 움직임은 의미가 있을 수 있지만, 사람들이 메뉴와 다른 인터페이스 요소를 탐색할 때 초점 모델을 사용한다. 앱에 포인터가 필요한 경우 가시성이 높고 경험과 통합된 느낌인지 확인하십시오.
>




**Design your interface to accommodate components in various focus states.** In tvOS, focusable items can have up to five different states, each of which is visually distinct. Because focusing an item often increases its scale, you need to supply assets for the larger, focused size to ensure they always look sharp, and you need to make sure the larger item doesn’t crowd the surrounding interface.
> 다양한 포커스 상태의 구성 요소를 수용할 수 있도록 인터페이스를 설계합니다. tvOS에서 포커스 가능한 항목은 최대 5개의 서로 다른 상태를 가질 수 있으며, 각각의 상태는 시각적으로 구별됩니다. 항목에 초점을 맞추면 크기가 커지는 경우가 많기 때문에 초점이 맞춰진 더 크고 초점이 맞춰진 크기의 자산을 제공하여 항상 선명하게 보이도록 해야 하며, 큰 항목이 주변 인터페이스를 혼잡하게 만들지 않도록 해야 합니다.
>




[제목 없음](https://www.notion.so/d25c90a1a9c04fe89fe42b1eefc88408)

For developer guidance, see [Adding user-focusable elements to a tvOS app](https://developer.apple.com/documentation/uikit/focus-based_navigation/adding_user-focusable_elements_to_a_tvos_app).
> 개발자 지침은 tvOS 앱에 사용자 중심 요소 추가를 참조하십시오.
>



