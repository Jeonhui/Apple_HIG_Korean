### [[Components - Menus and actions](./translated-human-interface-guidelines-markdown/components/menus-and-actions.md)]  
  
# **Buttons**  

**Design feedback sounds for custom buttons.** visionOS doesn’t play haptics, so it’s important to provide audible feedback for interactions with custom buttons.

**Design feedback sounds for custom buttons.** visionOS doesn’t play haptics, so it’s important to provide audible feedback for interactions with custom buttons.

> **사용자 정의 버튼에 대한 디자인 피드백 사운드.** 시력OS는 햅틱을 재생하지 않으므로 사용자 지정 버튼과의 상호 작용을 위해 청각적 피드백을 제공하는 것이 중요합니다.
>



### [watchOS](/design/human-interface-guidelines/buttons#watchOS)



watchOS displays all buttons using the [`capsule`](https://developer.apple.com/design/human-interface-guidelines/documentation/SwiftUI/ButtonBorderShape/capsule)

> watchOS는 ['watch'](https://developer.apple.com/design/human-interface-guidelines/documentation/SwiftUI/ButtonBorderShape/capsule) 를 사용하여 모든 버튼을 표시합니다
>

 button shape. In watchOS 10, the buttons are larger and have material backgrounds that adapt to underlying content to ensure legibility.

> 단추 모양. 감시하에OS 10, 버튼은 더 크고 가독성을 보장하기 위해 기본 콘텐츠에 적응하는 재료 배경을 가지고 있다.
>



![An illustration that represents a screen on Apple Watch, which includes capsule-shaped Primary and Secondary buttons.](https://docs-assets.developer.apple.com/published/8bf040bdd7aefb683943471f12ca3f26/button-watch@2x.png)



**Use the [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars)

 to place buttons in the corners.** The system automatically moves the time and title to accommodate toolbar buttons.

> 단추를 모서리에 끼우다.** 시스템이 자동으로 시간과 제목을 이동하여 도구 모음 버튼을 수용합니다.
>



![An illustration showing toolbar buttons in the top leading and trailing corners, as well as three toolbar buttons across the bottom of the screen.](https://docs-assets.developer.apple.com/published/5107ebed76f98c154a803845ad4c7a60/button-watch-corners@2x.png)



Toolbar buttons automatically inherit the app’s tint color. Only change the tint color when you need to convey important information, such as when a button performs a destructive action.

> 도구 모음 버튼은 앱의 틴트 색상을 자동으로 상속합니다. 단추가 파괴적인 작업을 수행하는 경우와 같이 중요한 정보를 전달해야 할 때만 틴트 색상을 변경하십시오.
>



**Prefer buttons that span the width of the screen for primary actions in your app.** Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.

> **앱에서 기본 작업을 수행하려면 화면 너비에 걸쳐 있는 버튼을 선호합니다.** 전체 너비 버튼이 더 좋아 보이고 사람들이 탭하기에 더 쉽습니다. 두 개의 단추가 동일한 수평 공간을 공유해야 하는 경우 두 단추 모두에 동일한 높이를 사용하고 각 단추의 내용에 이미지 또는 짧은 텍스트 제목을 사용합니다.
>



**Use toolbar buttons to provide either navigation to related areas or contextual actions for the view’s content.** These buttons provide access to additional information or secondary actions for the view’s content.

> **도구 모음 단추를 사용하여 관련 영역으로 이동하거나 보기 내용에 대한 상황별 작업을 제공합니다.** 이 단추를 사용하면 보기 내용에 대한 추가 정보 또는 보조 작업에 액세스할 수 있습니다.
>



**Use the same height for vertical stacks of one- and two-line text buttons.** As much as possible, use identical button heights for visual consistency.

> **1줄 및 2줄 텍스트 버튼의 수직 스택에는 동일한 높이를 사용하십시오.** 시각적 일관성을 위해 가능한 한 동일한 버튼 높이를 사용하십시오.
>



[Resources](/design/human-interface-guidelines/buttons#Resources)

-----------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/buttons#Related)



[Pop-up buttons](/design/human-interface-guidelines/pop-up-buttons)





[Pull-down buttons](/design/human-interface-guidelines/pull-down-buttons)





[Toggles](/design/human-interface-guidelines/toggles)





[Segmented controls](/design/human-interface-guidelines/segmented-controls)





[Location button](/design/human-interface-guidelines/privacy#Location-button)





#### [Developer documentation](/design/human-interface-guidelines/buttons#Developer-documentation)



[`Button`](/documentation/SwiftUI/Button)





[`UIButton`](/documentation/uikit/uibutton)





[`NSButton`](/documentation/appkit/nsbutton)





#### [Videos](/design/human-interface-guidelines/buttons#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/4445FCE4-AF6C-435D-BEF8-7A5A73D51270/4954_wide_250x141_1x.jpg) Meet the UIKit button system](https://developer.apple.com/videos/play/wwdc2021/10064) 

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/9CCE8A5D-A751-441C-B88F-FB91E2D1958E/4949_wide_250x141_1x.jpg) What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059) 

[Change log](/design/human-interface-guidelines/buttons#Change-log)

-------------------------------------------------------------------







| Date | Changes |

| --- | --- |

| June 21, 2023 | Updated to include guidance for visionOS. |

| June 5, 2023 | Updated guidance for using buttons in watchOS. |



