# **[inputs] remotes**

## The Siri Remote is the primary input method for Apple TV, helping people feel connected to onscreen content from across the room.
> 시리 리모트는 애플 TV의 주요 입력 방식으로, 사람들이 방 전체에서 화면 콘텐츠에 연결되는 것을 느낄 수 있도록 도와준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-remotes-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-remotes-intro_2x.png)

In addition to several specific buttons, the Siri Remote combines a clickpad and touch surface to support familiar gestures like swipe and press that people use to navigate tvOS apps, browse channels and content, play and pause media, and make selections.
> 몇 가지 특정 버튼 외에도, 시리 리모컨은 클릭패드와 터치 표면을 결합하여 사람들이 TVOS 앱을 탐색하고 채널과 콘텐츠를 탐색하고 미디어를 재생하고 일시 중지하고 선택하는 데 사용하는 스와이프 및 프레스와 같은 익숙한 제스처를 지원합니다.
>




# **Best practices**

**Prefer using standard gestures to perform standard actions.** Unless people are actively playing a game, they expect the remote to behave in standard ways in every app they use. Redefining or repurposing standard remote behaviors can cause confusion and add complexity to your experience. For guidance, see [Gestures](https://developer.apple.com/design/human-interface-guidelines/inputs/remotes#gestures).
> 표준 동작을 수행하기 위해 표준 제스처를 사용하는 것을 선호합니다. 사람들이 게임을 적극적으로 하지 않는 한, 그들은 리모컨이 그들이 사용하는 모든 앱에서 표준 방식으로 동작하기를 기대합니다. 표준 원격 동작을 재정의하거나 용도를 변경하면 혼란이 발생하고 사용자 환경이 복잡해질 수 있습니다. 자세한 내용은 제스처를 참조하십시오.
>




**Be consistent with the tvOS focus experience.** The [focus experience](../inputs/focus-and-selection)forges a strong connection between people and the content they’re viewing. Reinforce this link in your app by ensuring that you combine gestures with the focus experience in ways that are familiar to people, such as always moving focus in the same direction as the gesture.
> TVOS 포커스 경험과 일치해야 합니다. 포커스 경험은 사람들과 그들이 보고 있는 콘텐츠 사이에 강력한 연결을 형성합니다. 항상 제스처와 동일한 방향으로 포커스를 이동하는 것과 같이 사람들에게 친숙한 방식으로 제스처와 포커스 경험을 결합함으로써 앱에서 이 링크를 강화합니다.
>




**Provide clear feedback that shows people what happens when they make gestures in your app.** For example, lightly resting a thumb on the remote shows people where to swipe down so that they can reveal an info area.
> 예를 들어, 리모컨에 엄지 손가락을 살짝 갖다 대면 정보 영역을 표시할 수 있는 위치를 보여주는 명확한 피드백을 제공합니다.
>




**Define new gestures only when it makes sense in your app.** Within gameplay, for example, custom gestures can be a fun part of the experience. In most other situations, people expect to use standard gestures and may not appreciate having to discover or remember new ones.
> 앱에서 의미가 있을 때만 새로운 제스처를 정의하십시오. 예를 들어, 게임플레이 내에서 사용자 지정 제스처는 경험의 재미있는 부분이 될 수 있습니다. 대부분의 다른 상황에서, 사람들은 표준 제스처를 사용하기를 기대하고 새로운 제스처를 발견하거나 기억해야 하는 것을 좋아하지 않을 수도 있다.
>




**Differentiate between press and tap, and avoid responding to an inadvertent tap.** Pressing is an intentional action, and it works well for choosing a button, confirming a selection, and initiating an action during gameplay. Tap gestures are fine for navigation or showing additional information, but keep in mind that people might cause an inadvertent tap when they rest a thumb on the remote, pick it up, move it around, or hand it to someone else, so it often works well to avoid responding to taps during live video playback.
> 누르기와 탭을 구분하고, 실수로 탭을 누르는 것에 반응하지 않도록 합니다. 누르기는 의도적인 동작이며, 게임 플레이 중에 버튼을 선택하고 선택을 확인하며 동작을 시작하는 데 효과적입니다. 탭 제스처는 탐색하거나 추가 정보를 표시하는 데 사용할 수 있지만, 사용자가 리모컨에 엄지손가락을 올려놓거나 움직이거나 다른 사람에게 전달할 때 실수로 탭이 발생할 수 있으므로 라이브 비디오 재생 중 탭에 응답하지 않는 것이 좋습니다.
>




**Consider using the position of a tap to aid with navigation or gameplay.**The remote can differentiate between up, down, left, and right tap gestures on the touch surface. Respond to positional taps only if it makes sense in the context of your app and if such behavior is intuitive and discoverable.
> 탭의 위치를 사용하여 탐색 또는 게임 플레이를 도와주는 것을 고려해 보십시오.리모컨은 터치 표면에서 위, 아래, 왼쪽 및 오른쪽 탭 제스처를 구별할 수 있습니다. 앱의 맥락에서 의미가 있고 이러한 동작이 직관적이고 발견 가능한 경우에만 위치 탭에 응답하십시오.
>




**In almost all cases, open the parent of the current screen when people press the Back button.** At the top level of an app or game, the parent is the Apple TV Home Screen; within an app, the parent is defined by the app hierarchy, and isn’t necessarily the previous screen. The exception to this standard behavior is when people are actively playing a game, where it can be easy to accidentally press the Back button repeatedly. To avoid disrupting gameplay in this scenario, respond to the Back button by opening an in-game pause menu that lets people use a different interaction to navigate back to the game’s main menu. When the in-game pause menu is open, respond to a Back-button press by closing the menu and resuming the game. Note that people press and hold the Back button to go to the Home Screen from any location. For guidance, see [Buttons](https://developer.apple.com/design/human-interface-guidelines/inputs/remotes#buttons).
> 대부분의 경우 사람들이 뒤로 버튼을 누를 때 현재 화면의 상위를 엽니다. 앱 또는 게임의 최상위 수준에서 상위는 Apple TV 홈 화면입니다. 앱 내에서 상위는 앱 계층에 의해 정의되며 이전 화면일 필요는 없습니다. 이러한 표준 동작의 예외는 사람들이 능동적으로 게임을 하고 있을 때인데, 여기서 실수로 뒤로 버튼을 반복적으로 누르기 쉬울 수 있다. 이 시나리오에서 게임 플레이를 방해하지 않으려면 사람들이 다른 상호 작용을 사용하여 게임의 기본 메뉴로 다시 이동할 수 있는 게임 내 일시 중지 메뉴를 열어 뒤로 버튼에 응답하십시오. 게임 내 일시 중지 메뉴가 열려 있으면 메뉴를 닫고 게임을 다시 시작하여 뒤로 버튼을 누르면 응답합니다. 사용자는 아무 위치에서나 홈 스크린으로 이동하려면 뒤로 버튼을 길게 누릅니다. 자세한 내용은 단추를 참조하십시오.
>




**Respond correctly to the Play/Pause button during media playback.**When playing music or video, people expect pressing the Play/Pause button to play, pause, or resume playback.
> 미디어 재생 중에 재생/일시 중지 단추에 올바르게 응답합니다.음악 또는 비디오를 재생할 때 재생/일시 중지 단추를 눌러 재생, 일시 중지 또는 다시 시작합니다.
>




# **Gestures**

The clickpad's touch surface detects swipes and presses.
> 클릭패드의 터치면이 스위프 및 누름을 감지합니다.
>




**Swipe.** Swiping lets people scroll effortlessly through large numbers of items with movement that starts fast and then slows down, based on the strength of the swipe. When people swipe up or down on the edge of the remote, they can speed through items very quickly.
> 스와이프. 스와이프를 사용하면 스와이프의 강도에 따라 빠르게 시작했다가 느려지는 동작으로 많은 항목을 쉽게 스크롤할 수 있습니다. 사람들이 리모컨의 가장자리를 위아래로 문지르면, 그들은 매우 빠르게 항목을 통과할 수 있다.
>




**Press.** People press to activate a control or select an item. Also, people press before swiping to activate scrubbing mode.
> 누르면 컨트롤을 활성화하거나 항목을 선택할 수 있습니다. 또한, 사람들은 문지르기 모드를 활성화하기 위해 닦기 전에 누릅니다.
>




# **Buttons**

Ensure that your app or game responds to specific presses in the following ways.
> 앱 또는 게임이 다음과 같은 방법으로 특정한 프레스에 응답하는지 확인합니다.
>




| Button or area | Expected behavior in an app | Expected behavior in a game |
| --- | --- | --- |
| Touch surface (swipe) | Navigates.Changes focus. | Performs directional pad behavior. |
| Touch surface (press) | Activates a control or an item.Navigates deeper. | Performs primary button behavior. |
| Back | Returns to previous screen.Exits to Apple TV Home Screen. | Pauses/resumes gameplay.Returns to previous screen, exits to main game menu, or exits to Apple TV Home Screen. |
| Play/Pause | Activates media playback.Pauses/resumes media playback. | Performs secondary button behavior.Skips intro video. |

# **Compatible remotes**

Some remotes that are compatible with Apple TV include buttons for browsing live TV or other channel-based content. For example, a remote might include a button people can use to open an electronic program guide (EPG) and other buttons they can use to browse the guide or change channels. For developer guidance, see [Providing channel navigation](https://developer.apple.com/documentation/tvservices/providing_channel_navigation); for design guidance, see [EPG experience](https://developer.apple.com/design/human-interface-guidelines/patterns/live-viewing-apps#epg-experience).
> Apple TV와 호환되는 일부 원격에는 라이브 TV 또는 기타 채널 기반 콘텐츠를 탐색하기 위한 버튼이 포함되어 있습니다. 예를 들어 리모컨에는 전자 프로그램 가이드(EPG)를 여는 데 사용할 수 있는 단추와 가이드를 탐색하거나 채널을 변경하는 데 사용할 수 있는 기타 단추가 포함될 수 있습니다. 개발자 지침은 채널 탐색 제공을 참조하고, 설계 지침은 EPG 경험을 참조하십시오.
>




**If your live-viewing app provides an EPG, respond to a remote’s EPG-browsing buttons in ways people expect.** When people press a “guide” or “browse” button, they expect your EPG to open. While they’re viewing your EPG, people expect to navigate through it by pressing a “page up” or “page down” button. Avoid responding to these buttons in other ways while people are browsing the EPG. On the Siri Remote and compatible remotes, people can also tap on the upper or lower area of the Touch surface to browse the EPG. If your app doesn’t support an EPG experience, the system routes these button presses to the default guide app on the viewer’s device.
> 라이브 뷰잉 앱이 EPG를 제공하는 경우 리모컨의 EPG 브라우징 버튼에 사람들이 기대하는 방식으로 응답하십시오. 사람들이 "가이드" 또는 "찾아보기" 버튼을 누르면 EPG가 열릴 것으로 예상됩니다. EPG를 보는 동안 사람들은 "페이지 위로" 또는 "페이지 아래로" 버튼을 눌러 EPG를 탐색할 것으로 예상합니다. 사람들이 EPG를 검색하는 동안 이러한 버튼에 다른 방식으로 응답하지 않도록 합니다. Siri Remote 및 호환되는 원격에서는 터치 표면의 위쪽 또는 아래쪽 영역을 눌러 EPG를 탐색할 수도 있습니다. 앱이 EPG 경험을 지원하지 않는 경우 시스템은 이러한 버튼을 뷰어 장치의 기본 가이드 앱으로 라우팅합니다.
>




**While your content plays, respond to a compatible remote’s “page up” or “page down” button by changing the channel.** People expect these buttons to behave differently when they switch between viewing content and browsing an EPG.
> 콘텐츠가 재생되는 동안 채널을 변경하여 호환되는 리모컨의 "페이지업" 또는 "페이지다운" 단추에 응답하십시오. 사람들은 콘텐츠를 보는 것과 EPG를 보는 것 사이에서 전환할 때 이러한 단추가 다르게 작동할 것으로 예상합니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or watchOS.*
> iOS, iPadOS, macOS 또는 watch에서 지원되지 않음운영 체제
>



