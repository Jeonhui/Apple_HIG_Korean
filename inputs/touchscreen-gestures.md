# **[inputs] touchscreen-gestures**

## Gestures are a key way for people to interact with their touchscreen devices, eliciting a close personal connection with content and enhancing the sense of directly manipulating onscreen objects.
> 제스처는 사람들이 터치스크린 장치와 상호 작용하는 핵심 방법으로 콘텐츠와 개인적으로 밀접한 연결을 유도하고 화면 물체를 직접 조작하는 감각을 향상시킨다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-gestures-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-gestures-intro_2x.png)

In addition to using a touchscreen, people can also gesture using devices such as a trackpad, mouse, remote, or game controller. For example, people can use a trackpad to interact with their iPad or Mac, and they can use a game controller to interact with iPhone, iPad, Mac, and Apple TV. For guidance incorporating input from these devices, see [Pointing devices](../inputs/pointing-devices), [Remotes](../inputs/remotes), and [Game controllers](../inputs/game-controllers).
> 터치스크린을 사용하는 것 외에도 트랙패드, 마우스, 리모컨 또는 게임 컨트롤러와 같은 장치를 사용하여 제스처를 취할 수도 있습니다. 예를 들어, 사람들은 트랙패드를 사용하여 iPad 또는 Mac과 상호 작용할 수 있고, 게임 컨트롤러를 사용하여 iPhone, iPad, Mac 및 Apple TV와 상호 작용할 수 있습니다. 이러한 장치의 입력을 통합하는 지침은 포인팅 장치, 원격 및 게임 컨트롤러를 참조하십시오.
>




Touchscreen devices all use basic gestures like tap, swipe, and drag. Some platforms define additional gestures; for example, iOS and iPadOS support pinch and rotate. As you incorporate touchscreen gestures into your interface, you need to understand the behaviors of each platform’s [standard gestures](https://developer.apple.com/design/human-interface-guidelines/inputs/touchscreen-gestures#standard-gestures) so that you can provide a familiar and consistent experience.
> 터치스크린 장치는 모두 탭, 스와이프 및 드래그와 같은 기본 제스처를 사용합니다. 일부 플랫폼은 추가 제스처를 정의합니다. 예를 들어 iOS와 iPadOS는 핀치와 회전을 지원합니다. 터치스크린 제스처를 인터페이스에 통합할 때 각 플랫폼의 표준 제스처 동작을 이해해야 친숙하고 일관된 경험을 제공할 수 있습니다.
>




# **Best practices**

**In general, respond to gestures in ways that are consistent with other apps.** People expect most gestures to work the same regardless of their current context. For example, people expect the pinch gesture to adjust a view’s zoom level or scale a selected object. Avoid using a familiar gesture to perform an action that’s unique to your app; similarly, avoid creating a unique gesture to perform a standard action like choosing a button or scrolling a long view.
> 일반적으로 다른 앱과 일치하는 방식으로 제스처에 응답합니다. 사람들은 현재 상황에 상관없이 대부분의 제스처가 동일하게 작동하기를 기대합니다. 예를 들어, 사람들은 핀치 제스처가 보기의 확대/축소 수준을 조정하거나 선택한 개체의 크기를 조정하기를 기대합니다. 익숙한 제스처를 사용하여 앱에 고유한 작업을 수행하지 않도록 하고, 마찬가지로 단추를 선택하거나 긴 보기를 스크롤하는 등의 표준 작업을 수행하는 고유한 제스처를 만들지 않도록 합니다.
>




**Define custom gestures only when necessary.** People might find it difficult to discover and remember a custom gesture, and if it's awkward to perform, people may not want — or be able — to use it. Prefer custom gestures for situations where your app offers an immersive experience that requires context-specific interactions, like in a game or a drawing app, or when the system doesn’t handle a standard gesture, such as pinch in watchOS, or a gesture in a SpriteKit or SceneKit scene. If you decide to define a custom gesture, make sure it’s:
> 필요한 경우에만 사용자 지정 제스처를 정의합니다. 사용자 지정 제스처를 발견하고 기억하는 것이 어려울 수 있으며, 사용자 지정 제스처를 수행하는 것이 어색하면 사용자가 사용을 원하지 않거나 사용할 수 없습니다. 게임이나 드로잉 앱과 같이 상황별 상호 작용이 필요한 몰입형 환경을 제공하거나, 시스템이 워치OS 핀치와 같은 표준 제스처를 처리하지 않거나, 스프라이트킷 또는 씬킷 장면의 제스처를 처리하지 않는 상황에 적합한 사용자 지정 제스처를 선호합니다. 사용자 지정 제스처를 정의하려면 다음과 같이 하십시오:
>




- Easy to discover and perform
- >  검색 및 수행이 용이함

- Not too similar to gestures people already know
- >  사람들이 이미 알고 있는 제스처와 너무 비슷하지 않다

- Not the only way to perform an important action in your app
- >  앱에서 중요한 작업을 수행하는 유일한 방법은 아닙니다


**Make sure gestures apply to the appropriate content.** In general, gestures should apply to the content with which people are currently interacting, such as a selected element, an active view in a window, or an area on top of an item, like a photo. Start by using finger positions to help you identify the most specific content people are likely to be manipulating, and make that content the gesture’s target. If the content doesn’t respond to the gesture, consider targeting higher content levels and containers.
> 일반적으로 제스처는 선택한 요소, 창의 활성 보기 또는 사진처럼 항목 위의 영역과 같이 사용자가 현재 상호 작용하고 있는 콘텐츠에 적용되어야 합니다. 손가락 위치를 사용하여 사용자가 조작할 가능성이 있는 가장 구체적인 콘텐츠를 식별하고 해당 콘텐츠를 제스처의 대상으로 만듭니다. 콘텐츠가 제스처에 반응하지 않는 경우 더 높은 콘텐츠 수준과 컨테이너를 대상으로 지정하는 것이 좋습니다.
>




**Handle gestures as responsively as possible.** Gestures enhance the experience of direct manipulation and provide immediate live feedback. As people perform a gesture in your app, provide feedback that helps them predict its results and, if necessary, communicates the extent and type of movement required to complete the action.
> 가능한 한 반응적으로 제스처를 처리합니다. 제스처는 직접 조작의 경험을 향상시키고 즉각적인 라이브 피드백을 제공합니다. 사용자가 앱에서 제스처를 수행할 때 결과를 예측하는 데 도움이 되는 피드백을 제공하고 필요한 경우 동작을 완료하는 데 필요한 동작의 범위와 유형을 전달합니다.
>




**Enable shortcut gestures to supplement standard gestures, not to replace them.** People need simple, familiar ways to navigate and perform actions, even if it means an extra tap or two. For example, in an app that supports navigation through a hierarchy of screens, people expect to find a back button in a navigation bar that lets them return to the previous screen with a single tap. To help accelerate this action, many apps also offer a shortcut gesture — such as swiping from the side of the display or window — while continuing to provide the back button.
> 바로 가기 제스처를 사용하여 표준 제스처를 대체하는 것이 아니라 바로 가기 제스처를 사용할 수 있습니다. 사람들은 단순하고 친숙한 방법으로 탐색하고 동작을 수행해야 합니다. 비록 그것이 추가적인 탭을 의미하더라도 말입니다. 예를 들어, 화면의 계층 구조를 통해 탐색을 지원하는 앱에서, 사람들은 한 번의 탭으로 이전 화면으로 돌아갈 수 있는 탐색 모음에서 뒤로 버튼을 찾을 것으로 기대한다. 이 작업을 가속화하기 위해 많은 앱은 뒤로 버튼을 계속 제공하면서 디스플레이나 창 측면에서 스위핑하는 것과 같은 바로 가기 제스처도 제공합니다.
>




**Avoid interfering with systemwide screen-edge gestures.** Depending on the device, screen-edge gestures can provide access to the Home Screen, App Switcher, Notification Center, Control Center, and Dock. People rely on these gestures to work in every app. In rare cases, an immersive app like a game might require custom screen-edge gestures that take priority over the system's gestures. In this rare scenario, the game can use a behavior called *edge protect* in which the first swipe invokes the app-specific gesture and a second swipe invokes the system gesture. If you must enable custom screen-edge gestures, use edge protect sparingly, because people must perform a second gesture before they can access the system-level actions. For developer guidance, see the [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/uikit/uiviewcontroller/2887512-preferredscreenedgesdeferringsys)property of [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller).
> 장치에 따라 화면 가장자리 제스처를 사용하여 홈 스크린, 앱 전환기, 알림 센터, 제어 센터 및 독에 액세스할 수 있습니다. 사람들은 모든 앱에서 작동하기 위해 이러한 제스처에 의존한다. 드물게 게임과 같은 몰입형 앱은 시스템 제스처보다 우선하는 사용자 지정 화면 가장자리 제스처가 필요할 수 있습니다. 이 드문 시나리오에서 게임은 에지 프로텍트라는 동작을 사용할 수 있는데, 첫 번째 스와이프는 앱별 제스처를 호출하고 두 번째 스와이프는 시스템 제스처를 호출한다. 사용자 지정 화면 가장자리 제스처를 사용해야 하는 경우 사용자가 시스템 수준 작업에 액세스하려면 먼저 두 번째 제스처를 수행해야 하므로 에지 보호를 사용하지 마십시오. 개발자 지침은 UIViewController의 기본 화면 모서리 지연 시스템 제스처 속성을 참조하십시오.
>




# **Standard gestures**

| Gesture | iOS | iPadOS | watchOS | Standard action |
| --- | --- | --- | --- | --- |
| Tap | ● | ● | ● | Activate a control.Select an item. |
| Swipe | ● | ● | ● | Reveal actions and controls.Dismiss views.Scroll. |
| Pan (UIKit) / Drag (SwiftUI) | ● | ● | ● | Move a UI element. |
| Pinch (UIKit) / Magnification (SwiftUI) | ● | ● | – | Zoom a view.Magnify content. |
| Long press | ● | ● | ● | Reveal additional controls or functionality |
| Rotation | ● | ● | – | Rotate a selected item. |
| Edge swipe | ● | ● | ● | Navigate.Reveal controls, information, or system experiences. |
| Double tap | ● | ● | – | Zoom in.Zoom out if already zoomed in. |
| Three-finger swipe | ● | ● | – | Initiate undo (left swipe).Initiate redo (right swipe). |
| Four-finger swipe | – | ● | – | Switch between apps. |
| Three-finger pinch | ● | ● | – | Copy selected text (pinch in).Paste copied text (pinch out). |

# **Platform considerations**

*Not supported in macOS or tvOS.*
> macOS 또는 tvOS에서는 지원되지 않습니다.
>




# **iOS, iPadOS**

**Consider enabling simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](../inputs/apple-pencil-and-scribble).
> 동시 제스처가 게임 이외의 앱에서는 유용하지 않을 수 있지만 게임에는 조이스틱과 발사 단추와 같은 여러 개의 화면 컨트롤이 포함되어 사람이 동시에 조작할 수 있습니다. iPadOS 앱에서 터치스크린 입력을 Apple Pencil 입력과 통합하는 방법에 대한 지침은 Apple Pencil 및 Scribble을 참조하십시오.
>




# **watchOS**

**Consider alternatives to the long press gesture.** In versions of watchOS earlier than watchOS 7, people could press firmly on the display to do things like change the watch face or reveal a hidden menu called a Force Touch menu. In watchOS 7 and later, system apps make previously hidden menu items accessible in a related screen or a settings screen. If you formerly supported a long-press gesture to open a hidden menu, consider relocating the menu items elsewhere. For guidance, see [Menus](../components/menus-and-actions/menus).
> 길게 누르는 제스처에 대한 대안을 생각해보세요. 시계 버전에서워치보다 빠른 OSOS 7, 사람들은 디스플레이를 단단히 눌러 시계의 얼굴을 바꾸거나 Force Touch 메뉴라고 불리는 숨겨진 메뉴를 보여줄 수 있다. 당직중OS 7 이상의 시스템 앱은 이전에 숨겨진 메뉴 항목을 관련 화면이나 설정 화면에서 액세스할 수 있게 합니다. 이전에 숨겨진 메뉴를 열기 위해 길게 누르는 제스처를 지원한 경우 메뉴 항목을 다른 곳으로 재배치하는 것이 좋습니다. 자세한 내용은 메뉴를 참조하십시오.
>



