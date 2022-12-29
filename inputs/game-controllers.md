# **[inputs] game-controllers**

## Game controllers can enhance gameplay and increase a player’s immersion in a game.
> 게임 컨트롤러는 게임플레이를 향상시키고 플레이어의 게임 몰입도를 높일 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-game-controller-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-game-controller-intro_2x.png)

Supporting as many types of game controllers as possible gives people additional ways to enjoy interacting with your game.
> 가능한 한 많은 종류의 게임 컨트롤러를 지원하면 사람들이 게임과 상호 작용하는 것을 즐길 수 있는 추가적인 방법을 제공합니다.
>




# **Best practices**

**Support the platform’s default input method.** A game controller is an optional purchase, but every iPhone and iPad has a touchscreen, every Mac has a keyboard and a touchpad or mouse, and every Apple TV has a remote. If you support game controllers, consider letting people use the platform’s default input method to controls games, too.
> 플랫폼의 기본 입력 방식을 지원합니다. 게임 컨트롤러는 선택 구매이지만 모든 아이폰과 아이패드에는 터치스크린이 있고, 모든 맥에는 키보드와 터치패드 또는 마우스가 있으며, 모든 애플 TV에는 리모컨이 있습니다. 게임 컨트롤러를 지원하는 경우 사람들이 플랫폼의 기본 입력 방법을 사용하여 게임을 제어할 수 있도록 하는 것도 고려하십시오.
>




**Determine game controller requirements.** If your game has advanced game mechanics that a platform’s default input method can’t support, you can require the use of a game controller. The App Store displays a "Game Controller Required" badge to help people identify such apps and may warn people if they haven't paired a compatible game controller with their device.
> 게임 컨트롤러 요구 사항을 결정합니다. 게임에 플랫폼의 기본 입력 방법으로 지원할 수 없는 고급 게임 메커니즘이 있는 경우 게임 컨트롤러를 사용하도록 요구할 수 있습니다. 앱스토어에는 이러한 앱을 식별하는 데 도움이 되는 "게임 컨트롤러 필수" 배지가 표시되며, 호환되는 게임 컨트롤러가 장치와 페어링되지 않은 경우 경고가 표시될 수 있습니다.
>




**Confirm required game controller connections.** People can open your game any time, even without a connected controller. If your app requires a game controller, check for its presence and gracefully prompt people to connect one if necessary.
> 필요한 게임 컨트롤러 연결을 확인합니다. 사용자는 연결된 컨트롤러 없이도 언제든지 게임을 열 수 있습니다. 앱에 게임 컨트롤러가 필요한 경우 게임 컨트롤러가 있는지 확인하고 필요한 경우 사용자에게 컨트롤러를 연결하라는 메시지를 표시합니다.
>




**Help people understand the advantages of using a game controller with your app.** If your game is playable without a game controller, but using a game controller is recommended, look for ways to inform players that using a game controller will make playing easier and more enjoyable.
> 앱으로 게임 컨트롤러를 사용하는 것의 장점을 사람들이 이해할 수 있도록 도와줍니다. 게임 컨트롤러 없이 게임을 플레이할 수 있지만 게임 컨트롤러를 사용하는 것이 권장된다면 플레이어에게 게임 컨트롤러를 사용하면 게임을 더 쉽고 즐겁게 플레이할 수 있음을 알리는 방법을 찾아보십시오.
>




**Avoid requiring people to switch input devices.** For example, make sure players can use a game controller to navigate all game menus and interact with all essential functions without needing to switch to the platform’s default input method.
> 게임 컨트롤러를 사용하여 플랫폼의 기본 입력 방식으로 전환할 필요 없이 모든 게임 메뉴를 탐색하고 모든 필수 기능과 상호 작용할 수 있도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/game-controllers/images/game-controller_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/game-controllers/images/game-controller_2x.png)

**Support clickable thumbsticks when present.** Some controllers include thumbsticks that people can click or hold down as well as rotate. These buttons — also known as L3 and R3 — typically let people modify the enabled action by rotating the thumbstick. For example, clicking or holding a left thumbstick that enables motion might let people move at a different speed; clicking or holding a right thumbstick that controls camera orientation might let people zoom in or "crouch." As you consider ways to support clickable thumbsticks, be guided by the behaviors that people expect in various game genres.
> 클릭 가능한 엄지스틱을 지원합니다. 일부 컨트롤러에는 회전뿐만 아니라 클릭하거나 누를 수 있는 엄지스틱이 포함되어 있습니다. L3 및 R3라고도 하는 이러한 단추를 사용하면 일반적으로 사용자가 엄지스틱을 돌려 활성화된 작업을 수정할 수 있습니다. 예를 들어, 움직임을 가능하게 하는 왼쪽 엄지스틱을 클릭하거나 잡고 있으면 사람들이 다른 속도로 움직일 수 있고, 카메라 방향을 제어하는 오른쪽 엄지스틱을 클릭하거나 잡고 있으면 사람들이 확대하거나 "우그려" 할 수 있다. 클릭 가능한 엄지스틱을 지원하는 방법을 고려할 때, 다양한 게임 장르에서 사람들이 기대하는 행동에 따라 안내를 받으십시오.
>




**In general, prefer using the left thumbstick or directional pad (D-pad) button to move focus in the current screen.** Typically, people don't expect to use the right thumbstick to perform focus navigation while in a game.
> 일반적으로 현재 화면에서 포커스를 이동하려면 왼쪽 엄지스틱이나 방향 패드(D-pad) 버튼을 사용하는 것을 선호하며, 일반적으로 게임 중에는 오른쪽 엄지스틱을 사용하여 포커스 탐색을 수행할 것으로 예상하지 않습니다.
>




**Customize onscreen instructions to help people use the connected game controller.** Different controllers can use different colors or symbols to represent similar buttons, so it’s a good idea to avoid using color alone to refer to a button or explain what it does. Instead, refer to a button using the connected controller’s labeling scheme, such as “A” or the image of a triangle or square. In some cases, you might consider also showing an image of the interaction instead of using only a button label. For example, you might display an image of a D-pad, highlighted to indicate the up direction. Using images in addition to labels can be especially helpful for people who aren’t experienced with controllers because it doesn’t require them to hunt for a specific button label during gameplay.
> 다른 컨트롤러는 다른 색이나 기호를 사용하여 비슷한 단추를 나타낼 수 있으므로 단추를 참조하거나 단추의 기능을 설명하기 위해 색만 사용하지 않는 것이 좋습니다. 대신 연결된 컨트롤러의 레이블링 방식(예: "A" 또는 삼각형 또는 사각형의 이미지)을 사용하는 버튼을 참조하십시오. 경우에 따라 단추 레이블만 사용하는 대신 교호작용의 이미지를 표시하는 것도 고려할 수 있습니다. 예를 들어, 위쪽 방향을 나타내기 위해 강조 표시된 D-패드의 이미지를 표시할 수 있습니다. 라벨 외에 이미지를 사용하는 것은 게임 플레이 중 특정 버튼 라벨을 찾을 필요가 없기 때문에 컨트롤러에 익숙하지 않은 사람들에게 특히 도움이 될 수 있다.
>




# **Buttons**

In addition to playing games, people can use a game controller to navigate system and app interfaces, eliminating the need to switch input devices.
> 게임을 하는 것 외에도 게임 컨트롤러를 사용하여 시스템과 앱 인터페이스를 탐색할 수 있으므로 입력 장치를 전환할 필요가 없습니다.
>




| Button | Expected behavior in iOS and iPadOS | Expected behavior in macOS | Expected behavior in tvOS |
| --- | --- | --- | --- |
| D-pad | Moves focus | Moves focus | Moves focus |
| A | Activates a control or selects an item | Activates a control or selects an item | Activates a control or selects an item |
| B | – | – | Returns to previous screen. Exits to Apple TV Home Screen from an app's root-level screen. |
| X | Activates media playback. Pauses/resumes media playback. | Activates media playback. Pauses/resumes media playback. | Activates media playback. Pauses/resumes media playback. |
| Y | – | – | N/A |
| Left shoulder/trigger | Navigates left or moves focus | Navigates left or moves focus | Navigates left or moves focus |
| Right shoulder/trigger | Navigates right or moves focus | Navigates right or moves focus | Navigates right or moves focus |
| Left thumbstick | Navigates. Moves focus. | Navigates. Moves focus. | Navigates. Moves focus. |
| Right thumbstick | – | – | N/A |

A controller with a single auxiliary button needs to support the following behaviors:
> 단일 보조 버튼이 있는 컨트롤러는 다음 동작을 지원해야 합니다.
>




| Interaction with auxiliary button | Expected behavior in iOS and iPadOS | Expected behavior in macOS | Expected behavior in tvOS |
| --- | --- | --- | --- |
| Press | Returns to previous screen or pauses game | Returns to previous screen or pauses game | Returns to previous screen or pauses game |
| Long press | N/A | N/A | Exits to Apple TV Home Screen |
| Double press | Reveals multitasking user interface | Reveals multitasking user interface | Reveals multitasking user interface |

A controller with multiple auxiliary buttons includes a logo button in addition to the Menu button. Such a controller needs to support the following behaviors when people interact with the logo and Menu buttons:
> 여러 개의 보조 버튼이 있는 컨트롤러에는 메뉴 버튼 외에 로고 버튼이 있습니다. 이러한 컨트롤러는 사람들이 로고 및 메뉴 버튼과 상호 작용할 때 다음과 같은 동작을 지원해야 합니다.
>




| Button | Interaction | Expected behavior in iOS and iPadOS | Expected behavior in macOS | Expected behavior in tvOS |
| --- | --- | --- | --- | --- |
| Logo | Press | Reveals Control Center | Reveals Control Center | Reveals Control Center |
|  | Long press | N/A | N/A | Exists to Apple TV Home Screen |
|  | Double press | Reveals multitasking user interface | Reveals multitasking user interface | Reveals multitasking user interface |
| Menu | Press | Pauses game | Pauses game | Pauses game |

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS. Not supported in watchOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항은 없습니다. 워치에서 지원되지 않음운영 체제
>



