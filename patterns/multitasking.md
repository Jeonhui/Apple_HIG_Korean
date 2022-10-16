# **[patterns] multitasking**

# Multitasking lets people switch quickly from one app to another, performing tasks in each.
> 멀티태스킹을 통해 사람들은 한 앱에서 다른 앱으로 빠르게 전환하고 각각에서 작업을 수행할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-multitasking-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-multitasking-intro-dark_2x.png)

People expect to use multitasking on their devices, and they may think something is wrong if your app doesn’t allow it. With rare exceptions — such as some full-screen–only iPad apps — every app needs to work well with multitasking.
> 사람들은 그들의 기기에서 멀티태스킹을 사용할 것으로 기대하며, 당신의 앱이 그것을 허용하지 않는다면 그들은 무언가 잘못되었다고 생각할지도 모른다. 일부 전체 화면 전용 iPad 앱과 같은 드문 예외를 제외하고 모든 앱은 멀티태스킹과 잘 작동해야 합니다.
>




In addition to app switching, multitasking can enable different experiences on different devices.
> 멀티태스킹은 앱 전환 외에도 다양한 기기에서 다양한 경험을 할 수 있다.
>




On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.
> 아이폰에서 멀티태스킹은 사람들이 다른 앱을 사용하는 동안 페이스타임을 사용하거나 픽처 인 픽처(Picture in Picture)에서 비디오를 볼 수 있게 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-switcher-iphone_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-switcher-iphone_2x.png)

The app switcher displays all currently open apps.
> 앱 전환기는 현재 열려 있는 모든 앱을 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/pip-iphone_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/pip-iphone_2x.png)

A current FaceTime call can continue while people use another app.
> 사람들이 다른 앱을 사용하는 동안 현재 페이스타임 통화는 계속될 수 있다.
>




On iPad, people can view and interact with the windows of several different apps at the same time. An individual app can also enable multiple windows, which lets people view and interact with more than one window in the same app at one time.
> 아이패드에서 사람들은 동시에 여러 다른 앱의 창을 보고 상호작용할 수 있다. 또한 개별 앱은 여러 개의 창을 활성화할 수 있으며, 이를 통해 한 번에 동일한 앱에서 두 개 이상의 창을 보고 상호 작용할 수 있습니다.
>




• [Multitasking](../patterns/multitasking#)
• [Multiple windows](../patterns/multitasking#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-ipad-three-windows_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-ipad-three-windows_2x.png)

With multitasking, windows from several apps — like Notes, Maps, and Photos — can be available onscreen at the same time.
> 멀티태스킹 기능을 사용하면 Notes, Maps 및 Photos와 같은 여러 앱의 창을 동시에 화면에서 사용할 수 있습니다.
>





Apple TV, people can play or browse content while also playing movies or TV shows in Picture in Picture (where supported).
> Apple TV에서는 콘텐츠를 재생하거나 탐색하는 동시에 픽처 인 픽처(Picture in Picture)에서 영화나 TV 프로그램을 재생할 수 있습니다(지원되는 경우).
>




On a Mac, multitasking is the default user experience because people typically run more than one app at a time, switching between windows and tasks as they work.
> 맥에서 멀티태스킹은 기본 사용자 경험으로, 사람들이 일반적으로 한 번에 두 개 이상의 앱을 실행하며, 작업하면서 윈도우와 작업 사이를 전환하기 때문이다.
>




In contrast, watchOS makes it easy for people to switch between favorite or recently used apps, but people don’t open more than one app at a time on their watch.
> 반대로, 보기OS는 사람들이 좋아하는 앱이나 최근에 사용한 앱 사이에서 쉽게 전환할 수 있도록 해주지만, 사람들은 한 번에 둘 이상의 앱을 시계에서 열지 않는다.
>




# **Best practices**

A great multitasking experience helps people accomplish tasks in multiple apps by instantly pausing the current context when they switch away and seamlessly restoring it when they switch back. Because you don’t know when people will initiate multitasking, your app or game always needs to be prepared to save and restore their context.
> 훌륭한 멀티태스킹 경험을 통해 현재 컨텍스트를 전환할 때 즉시 일시 중지하고 다시 전환할 때 원활하게 복원함으로써 여러 앱에서 작업을 수행할 수 있습니다. 사람들이 언제 멀티태스킹을 시작할지 모르기 때문에, 당신의 앱이나 게임은 항상 그들의 컨텍스트를 저장하고 복원할 준비가 되어 있어야 한다.
>




**Pause activities that require people’s attention or active participation when they switch away.** If your app is a game or a media-viewing app, for example, make sure people don’t miss anything when they switch to another app. When they switch back, let them continue as if they never left.
> 사람들의 관심이나 적극적인 참여가 필요한 활동을 그들이 자리를 비울 때 잠시 멈춥니다. 예를 들어, 당신의 앱이 게임이나 미디어 보기 앱이라면, 사람들이 다른 앱으로 전환할 때 어떤 것도 놓치지 않도록 하세요. 그들이 다시 돌아갔을 때, 그들이 결코 떠나지 않은 것처럼 계속하도록 하세요.
>




**Respond smoothly to audio interruptions.** Occasionally, audio from another app or the system itself may interrupt your app’s audio. For example, an incoming phone call or a music playlist initiated by Siri might interrupt your app’s audio. When situations like these occur, people expect your app to respond in the following ways:
> 오디오 중단에 부드럽게 대응합니다. 때때로 다른 앱 또는 시스템 자체의 오디오가 앱의 오디오를 방해할 수 있습니다. 예를 들어 Siri에 의해 시작된 수신 전화 또는 음악 재생 목록이 앱의 오디오를 방해할 수 있습니다. 이와 같은 상황이 발생하면 사람들은 당신의 앱이 다음과 같은 방식으로 반응할 것으로 예상한다.
>




- Pause audio indefinitely for primary audio interruptions, such as playing music, podcasts, or audiobooks.
- >  음악, 팟캐스트 또는 오디오북 재생과 같은 기본 오디오 중단 시 오디오를 무기한 일시 중지합니다.

- Temporarily lower the volume or pause the audio for shorter interruptions, such as GPS directional notifications, and resume the original volume or playback when the interruption ends.
- >  GPS 방향 알림과 같이 더 짧은 인터럽트를 위해 일시적으로 볼륨을 낮추거나 오디오를 일시 중지하고 인터럽트가 끝나면 원래 볼륨 또는 재생을 다시 시작합니다.


For guidance, see [Playing audio](../patterns/playing-audio).

**Finish user-initiated tasks in the background.** When someone starts a task, they expect it to finish even if they switch away from your app. If your app is in the middle of performing a task that doesn’t need additional input, complete it in the background before suspending.
> 백그라운드에서 사용자 시작 작업을 완료합니다. 누군가 어떤 일을 시작하면, 그들은 당신의 앱에서 벗어나도 그것이 끝날 것으로 예상한다. 앱이 추가 입력이 필요 없는 작업을 수행 중인 경우 일시 중단하기 전에 백그라운드에서 완료하십시오.
>




**Use notifications sparingly.** Your app can send notifications when it’s suspended or running in the background. If people start an important or time-sensitive task in your app, and then switch away from it, they might appreciate receiving a notification when the task completes so they can switch back to your app and take the next step. In contrast, people don’t generally need to know the moment a routine or secondary task completes. In this scenario, avoid sending an unnecessary notification; instead, let people check on the task when they return to your app. For guidance, see [Managing notifications](../patterns/managing-notifications).
> 통지는 적게 사용합니다. 앱이 중단되거나 백그라운드에서 실행 중일 때 알림을 보낼 수 있습니다. 앱에서 중요하거나 시간에 민감한 작업을 시작한 다음 다른 사용자가 해당 작업을 사용하지 않을 경우 작업이 완료될 때 알림을 받아 앱으로 다시 전환하고 다음 단계를 수행할 수 있습니다. 이와는 대조적으로, 사람들은 일반적으로 일상적이거나 부차적인 작업이 완료되는 순간을 알 필요가 없다. 이 시나리오에서는 불필요한 알림을 보내지 않도록 하십시오. 대신 다른 사용자가 앱으로 돌아갈 때 작업을 확인하도록 하십시오. 자세한 내용은 알림 관리를 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, macOS, or tvOS. Not supported in watchOS.*
> iOS, macOS 또는 tvOS에 대한 추가 고려 사항 없음. 시계에서 지원되지 않음OS.
>




# **iPadOS**

### **Multitasking on iPad**

iPadOS can present multitasking windows in a variety of configurations, supporting various workflows. The system also provides multitasking controls — which let people switch multitasking configurations — and the app shelf, which lets people access all open windows in an app.
> 아이패드 OS는 다양한 구성의 멀티태스킹 윈도우를 제공하여 다양한 워크플로우를 지원할 수 있다. 이 시스템은 또한 멀티태스킹 구성을 전환할 수 있는 멀티태스킹 제어 기능과 앱에서 열려 있는 모든 창에 액세스할 수 있는 앱 쉘프를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-controls_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/multitasking-controls_2x.png)

Multitasking controls

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-shelf_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/app-shelf_2x.png)

App shelf

People can choose one of the following configurations to open multitasking windows on iPad.
> 사람들은 아이패드에서 멀티태스킹 윈도우를 열기 위해 다음 구성 중 하나를 선택할 수 있다.
>




- *Slide Over* opens a second window in an overlay while the first window continues in full screen. People can change the onscreen location of the Slide Over window, or hide it offscreen and retrieve it later. People can also open multiple windows in Slide Over, where they form a stack.
- >  슬라이드 오버는 첫 번째 창이 전체 화면에서 계속되는 동안 오버레이에서 두 번째 창을 엽니다. 사용자는 슬라이드 오버 창의 화면 위치를 변경하거나 화면 밖으로 숨겼다가 나중에 검색할 수 있습니다. 또한 슬라이드 오버에서 여러 개의 창을 열 수 있으며, 이 창에서 스택을 구성할 수 있습니다.

- *Split View* displays two windows side by side, letting people resize the relative areas of the windows and interact with both. While viewing side-by-side windows in Split View, people can also open a third window in Slide Over.
- >  보기 분할은 두 개의 창을 나란히 표시하여 사용자가 창의 상대 영역 크기를 조정하고 두 창과 상호 작용할 수 있도록 합니다. 분할 보기에서 나란히 표시되는 창을 보는 동안 슬라이드 오버에서 세 번째 창을 열 수도 있습니다.

- *Picture in Picture* opens a video in a movable, resizable window that floats above the full-screen app.
- >  사진의 사진은 전체 화면 앱 위에 떠 있는 이동 가능한 크기 조정 가능한 창에서 비디오를 엽니다.


• [Slide Over](../patterns/multitasking#)
• [Split View](../patterns/multitasking#)
• [Picture in Picture](../patterns/multitasking#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/slideover_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking/images/slideover_2x.png)


**NOTE**Apps don’t control multitasking configurations or receive any indication of the ones that people choose.
> 참고 Apps는 멀티태스킹 구성을 제어하거나 사용자가 선택한 작업의 표시를 수신하지 않습니다.
>




To help your iPad app respond correctly when people open it in Split View or Slide Over, make sure it [adapts gracefully to different screen sizes](../foundations/layout); for developer guidance, see [Multitasking on iPad](https://developer.apple.com/documentation/uikit/app_and_environment/multitasking_on_ipad). To learn more about how people use iPad multitasking features, see [Use multitasking on your iPad](https://support.apple.com/en-us/HT207582).
> iPad 앱을 Split View 또는 Slide Over(분할 보기)에서 열 때 올바르게 응답하려면 다양한 화면 크기에 맞게 조정해야 합니다. 개발자 지침은 iPad의 멀티태스킹을 참조하십시오. iPad 멀티태스킹 기능을 사용하는 방법에 대한 자세한 내용은 iPad에서 멀티태스킹 사용을 참조하십시오.
>




### **Multiple windows on iPad**

Conceptually, iPad apps tend to use two types of windows to provide content:
> 개념적으로 아이패드 앱은 콘텐츠를 제공하기 위해 두 가지 유형의 창을 사용하는 경향이 있다.
>




- A *primary* window presents the app’s full hierarchy, providing access to all of the app’s objects and the actions associated with them. For example, Mail uses a primary window to present all mailboxes and message lists.
- >  기본 창은 앱의 모든 개체와 관련된 작업에 대한 액세스를 제공하는 앱의 전체 계층을 표시합니다. 예를 들어, 메일은 기본 창을 사용하여 모든 사서함과 메시지 목록을 표시합니다.

- An *auxiliary* window presents a specific task or area in the app, often using a modal presentation. Dedicated to one experience, an auxiliary window doesn’t enable navigation to other app areas, and it typically includes buttons people use to close it after completing the task. For example, Mail uses an auxiliary window to present a single message.
- >  보조 창은 종종 모달 프레젠테이션을 사용하여 앱의 특정 작업 또는 영역을 표시합니다. 한 가지 경험만을 위한 보조 창은 다른 앱 영역으로 이동할 수 없으며 일반적으로 작업을 완료한 후 닫는 데 사용하는 버튼을 포함합니다. 예를 들어, 메일은 보조 창을 사용하여 단일 메시지를 표시합니다.


In iPadOS 15 and later, you can specify a presentation style that determines the initial appearance of each window that people open in your app. Although people can reposition a window after opening it, specifying a presentation style can visually reinforce the nature of a window’s task or content. iPadOS defines the following presentation styles:
> iPadOS 15 이상에서는 사용자가 앱에서 여는 각 창의 초기 모양을 결정하는 프레젠테이션 스타일을 지정할 수 있습니다. 사용자가 창을 연 후 창을 재배치할 수 있지만 프레젠테이션 스타일을 지정하면 창의 작업이나 콘텐츠의 특성을 시각적으로 강화할 수 있습니다.
>




- Prominent. A modal presentation that elevates the window, dimming the surrounding areas and preventing interaction with them.
- >  두드러지다. 창을 들어 올려 주변 영역을 어둡게 하고 상호 작용을 방지하는 모달 프레젠테이션입니다.

- Standard. A side-by-side presentation that enables interaction with peer windows, each of which supports the app’s full functionality.
- >  표준. 피어 창과의 상호 작용을 가능하게 하는 나란히 표시되는 프레젠테이션으로, 각 창은 앱의 전체 기능을 지원합니다.

- Automatic. A presentation that the system chooses based on the context in which your app requests the window.
- >  자동. 프로그램이 창을 요청하는 컨텍스트에 따라 시스템이 선택하는 프레젠테이션입니다.


**TIP**If you simply need to let people view a file, you can present it without creating your own window, but you must support multiple windows in your app. For developer guidance, see [QLPreviewSceneActivationConfiguration](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration/).
> 팁 단순히 다른 사람이 파일을 볼 수 있도록 해야 하는 경우 자신의 창을 만들지 않고도 파일을 표시할 수 있지만 앱에서 여러 창을 지원해야 합니다. 개발자 지침은 QLP 검토 장면 활성화 구성을 참조하십시오.
>




**Use the prominent style to present a self-contained task people can complete without opening other parts of your app.** For example, the prominent style works well to enable document editing or another task that’s scoped to a specific file or collection of content. Be sure a prominent window is also useful on its own; avoid using it to present secondary tasks, supplemental actions, or choosing items that affect the main task.
> 눈에 띄는 스타일을 사용하여 앱의 다른 부분을 열지 않고도 사람들이 완료할 수 있는 자체 포함 작업을 제시하십시오. 예를 들어, 눈에 띄는 스타일은 문서 편집이나 특정 파일 또는 내용 모음으로 범위를 지정하는 다른 작업을 가능하게 하는 데 적합합니다. 눈에 띄는 창은 그 자체로 유용해야 합니다. 보조 작업, 보조 작업 또는 주요 작업에 영향을 미치는 항목을 선택하는 데 사용하지 마십시오.
>




**Use the standard style to present multiple versions of the same task or content.** For example, Safari uses the standard style to help people view and interact with two browsing windows onscreen at the same time.
> 표준 스타일을 사용하여 동일한 작업 또는 내용의 여러 버전을 표시할 수 있습니다. 예를 들어 Safari는 표준 스타일을 사용하여 사람들이 동시에 두 개의 검색 창을 보고 상호 작용할 수 있도록 도와줍니다.
>




**Open a new window only when people take an explicit action.** For example, people can tap the Add (+) button in the app shelf or App Exposé, or choose a menu item. Avoid surprising people by opening a new window they don’t request.
> 사용자가 명시적 작업을 수행할 때만 새 창을 엽니다. 예를 들어, 앱 선반이나 앱 노출에서 추가(+) 버튼을 누르거나 메뉴 항목을 선택할 수 있습니다. 요청하지 않은 새 창을 열어 사람들을 놀라게 하는 것을 피하세요.
>




**Make sure your app’s primary windows support every task that you enable.** Multiple windows can offer convenient and efficient workflows, but people always need to be able to access every app feature in each primary window.
> 앱의 기본 창이 활성화하는 모든 작업을 지원하는지 확인하십시오. 여러 개의 창이 편리하고 효율적인 워크플로우를 제공할 수 있지만, 사람들은 항상 각 기본 창의 모든 앱 기능에 액세스할 수 있어야 합니다.
>




**Preserve the state in each window that people open.** When people return to a window, they expect it to be in the same state in which they left it. For developer guidance, see [Restoring your app’s state](https://developer.apple.com/documentation/uikit/uiscenedelegate/restoring_your_app_s_state).
> 사용자가 여는 각 창의 상태를 유지합니다. 사람들이 창으로 돌아갈 때, 그들은 창문이 그들이 창밖으로 떠난 것과 같은 상태일 것이라고 예상한다. 개발자 지침은 앱 상태 복원을 참조하십시오.
>




**Consider letting people use a gesture to open content in a new window.** For example, people can use the pinch gesture to expand a Notes item into a new window. A gesture-enabled transition always uses the prominent presentation style, making the resulting modal window feel like a natural consequence of expanding the item or task. For developer guidance, see [collectionView(_:sceneActivationConfigurationForItemAt:point:)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/3752185-collectionview) (to transition from a collection view item) or [UIWindowScene.ActivationInteraction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction) (to transition from an item in any other view).
> 사람들이 제스처를 사용하여 새 창에서 내용을 열 수 있도록 하는 것을 고려해 보십시오. 예를 들어, 사람들은 집기 제스처를 사용하여 Notes 항목을 새 창으로 확장할 수 있습니다. 제스처 사용 전환은 항상 눈에 띄는 프레젠테이션 스타일을 사용하므로 결과 모달 창이 항목이나 작업을 확장하는 자연스러운 결과처럼 느껴집니다. 개발자 지침은 collectionView(_:sceneActivationConfigurationForItemAt:point:) 또는 UIWindowsScene을 참조하십시오.활성화상호 작용(다른 보기의 항목에서 전환합니다.
>




**Consider providing a menu item that lets people open content in a new window.** When you enable this behavior, the menu presents an “Open in new window” item when your app runs on iPad or on a Mac using Mac Catalyst, but not when your app runs on iPhone. If it makes sense in your app, you can supply an alternative item to display when the app runs on iPhone, such as “Show details...”. You can add an “Open in new window” item to a context menu or to menus attached to buttons and bar button items. For developer guidance, see [UIWindowScene.ActivationAction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction/).
> 새 창에서 내용을 열 수 있는 메뉴 항목을 제공하는 것을 고려해 보십시오. 이 동작을 활성화하면 Mac Catalyst를 사용하여 iPad 또는 Mac에서 앱을 실행할 때는 메뉴에 "새 창에서 열기" 항목이 표시되지만 iPhone에서 앱을 실행할 때는 표시되지 않습니다. 당신의 앱에서 그것이 타당하다면, 당신은 "상세 정보 표시..."와 같이 앱이 아이폰에서 실행될 때 표시할 대체 항목을 제공할 수 있다. 상황에 맞는 메뉴 또는 단추 및 막대 단추 항목에 첨부된 메뉴에 "새 창에서 열기" 항목을 추가할 수 있습니다. 개발자 지침은 UI WindowsScene을 참조하십시오.활성화 작업.
>




**Avoid specifying a layout when providing a way to open content in a new window.** Because you don’t know which multitasking configuration people are using, avoid offering menu items like “Open in split view” or “Open in front.”
> 새 창에서 내용을 여는 방법을 제공할 때 레이아웃을 지정하지 않도록 합니다. 사용자가 어떤 멀티태스킹 구성을 사용하는지 모르기 때문에 "분할 보기에서 열기" 또는 "앞에서 열기"와 같은 메뉴 항목은 제공하지 마십시오.
>




**Use the term *window* in user-facing content.** The system refers to app windows as *windows* regardless of type. Using different terms — including *scene*, which refers to window implementation — is likely to confuse people.
> 사용자 대면 콘텐츠에서 용어 창을 사용합니다. 시스템은 유형에 관계없이 앱 창을 창으로 지칭한다. 창 구현을 의미하는 장면을 포함하여 다른 용어를 사용하면 사람들을 혼란스럽게 할 수 있습니다.
>



