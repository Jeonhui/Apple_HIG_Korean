# **[components-status] status-bars**

## A status bar appears along the upper edge of the screen and displays information about the device’s current state, like the time, cellular carrier, and battery level.
> 상태 표시줄은 화면 상단 가장자리를 따라 나타나며 시간, 휴대 전화 캐리어 및 배터리 수준과 같은 장치의 현재 상태에 대한 정보를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/status-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/status-bar-intro-dark_2x.png)

# **Best practices**

**Obscure content under the status bar.** By default, the background of the status bar is transparent, allowing content beneath to show through. This can make it difficult to see the information presented in the status bar. If controls are visible behind the status bar, people may attempt to interact with them and be unable to do so. Be sure to keep the status bar readable and don’t imply that content behind it is interactive. There are several common techniques for doing this:
> 상태 표시줄 아래의 내용을 알 수 없습니다. 기본적으로 상태 표시줄의 배경은 투명하므로 아래의 내용을 볼 수 있습니다. 이로 인해 상태 표시줄에 표시된 정보를 보기 어려울 수 있습니다. 상태 표시줄 뒤에 컨트롤이 표시되면 사용자가 컨트롤과 상호 작용을 시도하여 컨트롤과 상호 작용하지 못할 수 있습니다. 상태 표시줄을 읽기 쉬운 상태로 유지하고, 그 뒤에 있는 내용이 대화형임을 암시하지 마십시오. 이를 수행하기 위한 몇 가지 일반적인 기술이 있습니다.
>




- Use a navigation bar that automatically displays a status bar background.
- >  상태 표시줄 배경을 자동으로 표시하는 탐색 모음을 사용합니다.

- Display a custom image, like a gradient or solid color, behind the status bar.
- >  상태 표시줄 뒤에 그라데이션 또는 단색과 같은 사용자 정의 이미지를 표시합니다.

- Place a blurred view behind the status bar. For developer guidance, see [UIBlurEffect](https://developer.apple.com/documentation/uikit/uiblureffect).
- >  흐릿한 보기를 상태 표시줄 뒤에 놓습니다. 개발자 지침은 UIBlurEffect를 참조하십시오.


**Consider temporarily hiding the status bar when displaying full-screen media.** A status bar can be distracting when people are trying to focus on media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when people browse full-screen photos.
> 전체 화면 미디어를 표시할 때는 일시적으로 상태 표시줄을 숨기는 것이 좋습니다. 사람들이 미디어에 집중하려고 할 때 상태 표시줄은 주의를 산만하게 할 수 있습니다. 이러한 요소를 일시적으로 숨겨 더욱 몰입감 있는 경험을 제공합니다. 예를 들어, 사진 앱은 사람들이 전체 화면 사진을 볼 때 상태 표시줄 및 기타 인터페이스 요소를 숨깁니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/status-bars/images/status-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/status-bars/images/status-bar_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/status-bars/images/hidden-status-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/status-bars/images/hidden-status-bar_2x.png)

**Avoid permanently hiding the status bar.** Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in the Photos app, a single tap shows the status bar again. For developer guidance, see [statusBar(hidden:)](https://developer.apple.com/documentation/swiftui/path/statusbar(hidden:)).
> 상태 표시줄을 영구적으로 숨기지 마십시오. 상태 표시줄이 없으면 시간을 확인하거나 Wi-Fi 연결이 있는지 확인하기 위해 앱을 떠나야 합니다. 사람들이 간단하고 검색 가능한 제스처로 숨겨진 상태 표시줄을 다시 표시할 수 있습니다. 예를 들어 사진 앱에서 전체 화면 사진을 검색할 때 한 번만 누르면 상태 표시줄이 다시 표시됩니다. 개발자 지침은 상태 표시줄(숨김:)을 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, or watchOS.*
> iOS 또는 iPadOS에 대한 추가 고려 사항은 없습니다. macOS, tvOS 또는 watch에서 지원되지 않음운영 체제
>



