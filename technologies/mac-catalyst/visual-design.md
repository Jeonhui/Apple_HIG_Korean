# **[technologies-mac-catalyst] visual-design**

To help the Mac version of your app look great, address platform differences in the following areas of visual design.
> Mac 버전의 앱이 멋지게 보이도록 하려면 다음과 같은 시각적 디자인 영역의 플랫폼 차이를 해결하십시오.
>




# **Layout**

Mac users expect to resize app windows to just about any size, from full screen to as small as the app permits. To support this type of infinite resizability — and to take advantage of the wider Mac display — use the regular-width and regular-height size classes and consider reflowing elements in your window’s content area to a side-by-side arrangement when necessary.
> Mac 사용자들은 앱 창 크기를 전체 화면에서 앱이 허용하는 한 작은 크기까지 거의 모든 크기로 조정하기를 기대합니다. 이러한 무한 확장 가능한 크기를 지원하고 더 넓은 Mac 디스플레이를 활용하려면 일반 너비 및 일반 높이 크기 클래스를 사용하고 필요한 경우 창의 콘텐츠 영역에 있는 요소를 나란히 정렬하는 것을 고려하십시오.
>




**As much as possible, adopt a top-down user flow.** Mac apps place the most important actions and content near the top of the window. If your iOS app provides controls in a toolbar or navigation bar, put these controls in the window toolbar of the macOS version of your app.
> 가능한 한 하향식 사용자 흐름을 채택하십시오. Mac 앱은 가장 중요한 작업과 콘텐츠를 창 위쪽에 배치합니다. iOS 앱에서 도구 모음이나 탐색 모음에 컨트롤을 제공하는 경우 해당 컨트롤을 앱의 macOS 버전의 창 도구 모음에 넣습니다.
>




**Consider moving controls from the main UI of your iPad app to your Mac app’s toolbar.**Additionally, list the commands associated with these controls in the menus of your macOS app’s menu bar.
> iPad 앱의 기본 UI에서 Mac 앱의 도구 모음으로 컨트롤을 이동하는 것을 고려해 보십시오.또한 macOS 앱의 메뉴 모음에 이러한 컨트롤과 관련된 명령을 나열합니다.
>




**NOTE**In macOS, a toolbar button is always visible, but the current context might make it unavailable; in iOS, a toolbar button is always available, but the current context might remove it from the toolbar. For example, if your iOS app includes a toolbar button that works in only one tab, the macOS version displays the button as unavailable in all other tabs.
> 참고 MacOS에서는 도구 모음 단추를 항상 볼 수 있지만 현재 컨텍스트에서는 사용할 수 없게 만들 수 있습니다. iOS에서는 도구 모음 단추를 항상 사용할 수 있지만 현재 컨텍스트에서는 도구 모음 단추를 제거할 수 있습니다. 예를 들어 iOS 앱에 한 탭에서만 작동하는 도구 모음 단추가 포함되어 있는 경우 macOS 버전에는 다른 모든 탭에서 해당 단추를 사용할 수 없음으로 표시됩니다.
>




**Relocate buttons from the left or right edge of the screen.** On iPad, placing buttons on the middle-left or middle-right screen edges can help people reach them, but on a Mac, this ergonomic consideration doesn’t apply. You may want to relocate controls to the top or bottom edge of the content area or put them in the toolbar of your macOS window.
> 화면 왼쪽이나 오른쪽 가장자리에서 단추를 재배치합니다. iPad에서는 왼쪽 중간 또는 오른쪽 화면 가장자리에 단추를 배치하면 사람들이 단추에 도달하는 데 도움이 될 수 있지만 Mac에서는 이러한 인체공학적 고려 사항이 적용되지 않습니다. 컨트롤을 콘텐츠 영역의 위쪽 또는 아래쪽 가장자리로 재배치하거나 macOS 창의 도구 모음에 배치할 수 있습니다.
>




# **Color**

**Use the system’s accent color on both platforms.** iOS apps define the colors used to tint buttons and to indicate selection. In contrast, Mac users expect apps to use the accent color they chose in System Settings.
> 두 플랫폼 모두에서 시스템의 액센트 색상을 사용합니다. iOS 앱은 버튼을 틴팅하고 선택 항목을 표시하는 데 사용되는 색상을 정의합니다. 이와 대조적으로 Mac 사용자들은 앱이 시스템 설정에서 선택한 액센트 색상을 사용하기를 기대합니다.
>




The [dynamic system colors](https://developer.apple.com/design/human-interface-guidelines/foundations/color#ios-ipados) designed for iOS backgrounds automatically map to appropriate macOS equivalents, as shown below.
> iOS 배경을 위해 설계된 동적 시스템 색상은 아래와 같이 적절한 macOS에 자동으로 매핑됩니다.
>




| iOS color | Equivalent macOS color |
| --- | --- |
| https://developer.apple.com/documentation/uikit/uicolor/3173140-systembackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173137-secondarysystembackground | https://developer.apple.com/documentation/appkit/nscolor/1528630-windowbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173154-tertiarysystembackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor (overlaid with https://developer.apple.com/documentation/appkit/nscolor/1534635-quaternarylabelcolor) |
| https://developer.apple.com/documentation/uikit/uicolor/3173145-systemgroupedbackground | https://developer.apple.com/documentation/appkit/nscolor/1528630-windowbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173138-secondarysystemgroupedbackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor |
| https://developer.apple.com/documentation/uikit/uicolor/3173155-tertiarysystemgroupedbackground | https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor (overlaid with https://developer.apple.com/documentation/appkit/nscolor/1534635-quaternarylabelcolor) |

Other semantically defined iOS colors — such as the and the label and separator colors — map to similarly named macOS colors. For guidance, see [macOS](https://developer.apple.com/design/human-interface-guidelines/foundations/color#macos).
> 다른 의미론적으로 정의된 iOS 색상(및 레이블 및 구분 기호 색상)은 비슷한 이름의 macOS 색상에 매핑됩니다. 자세한 내용은 macOS를 참조하십시오.
>




**Don’t tint buttons in table rows.** In your iOS app, you use a tint to show that buttons in table rows are active, but in macOS, tinted buttons in table rows look out of place.
> iOS 앱에서는 테이블 행의 단추가 활성 상태임을 표시하기 위해 색인을 사용하지만, MacOS에서는 테이블 행의 색인 단추가 적합하지 않은 것처럼 보입니다.
>




# **Typography**

With the iPad idiom, the system automatically scales text to achieve good results without requiring you to specify different font values on each platform. However, you might not get the best results in every situation.
> iPad 관용구를 사용하면 각 플랫폼에서 다른 글꼴 값을 지정할 필요 없이 텍스트 크기를 자동으로 조정하여 좋은 결과를 얻을 수 있습니다. 그러나 모든 상황에서 최상의 결과를 얻지 못할 수도 있습니다.
>




**Make sure small type is legible on the Mac.** Be prepared to increase some of the smallest font sizes you use in your iOS app so that all text remains legible in the macOS version. Also, note that macOS doesn’t support Dynamic Type.
> Mac에서 작은 글꼴을 읽을 수 있는지 확인하십시오. iOS 앱에서 사용하는 가장 작은 글꼴 크기 중 일부를 늘려서 MacOS 버전에서 모든 텍스트를 읽을 수 있도록 준비하십시오. 또한 macOS는 동적 유형을 지원하지 않습니다.
>




**If you adopt the Mac idiom, adjust your text’s font size.** With the iPad idiom, the system scales text to 77% of its size. For example, the system scales text that uses the iOS baseline font size of 17pt down to 13pt in macOS. With the Mac idiom, text renders at 100% of its configured size, which can appear too large without adjustment. When possible, use text styles and avoid fixed font sizes. For guidance, see [Adopting the Mac idiom](../technologies/mac-catalyst/mac-idiom).
> Mac 사자성어를 사용하는 경우 텍스트의 글꼴 크기를 조정하십시오. iPad 사자성어를 사용하면 텍스트 크기가 77%로 조정됩니다. 예를 들어, 시스템은 iOS 기준 글꼴 크기인 17pt를 사용하는 텍스트를 macOS에서 13pt로 축소합니다. Mac 관용구를 사용하면 텍스트가 구성된 크기의 100%로 렌더링되므로 조정하지 않으면 너무 크게 보일 수 있습니다. 가능한 경우 텍스트 스타일을 사용하고 글꼴 크기를 고정하지 마십시오. 자세한 내용은 Mac 관용구 채택을 참조하십시오.
>




# **Custom icons and glyphs**

**Create a macOS version of your app icon.** Great macOS app icons showcase the lifelike rendering style that people expect in macOS while presenting a harmonious user experience across all platforms. For guidance, see [App icons](../foundations/app-icons).
> 앱 아이콘의 macOS 버전을 만듭니다. 훌륭한 macOS 앱 아이콘은 모든 플랫폼에서 조화로운 사용자 경험을 제공하면서 사람들이 macOS에서 기대하는 실제와 같은 렌더링 스타일을 보여줍니다. 자세한 내용은 앱 아이콘을 참조하십시오.
>




**Prefer using symbols offered by SF symbols.** SF Symbols provides a set of consistent, highly configurable symbols you can use to offer consistent iconography across platforms. You can also create your own custom symbol images to use in your iOS and macOS apps. In addition, macOS 11 and later automatically maps AppKit shared images — such as control icons for Action, Add, and Bookmarks — to specific symbols. As a result, your app may already display symbol images offered by SF Symbols in interface elements like the toolbar on Macs that run macOS 11 or later. Using SF symbols ensures that your app’s iconography aligns with the general iconography of macOS.
> SF 기호가 제공하는 기호를 사용하는 것을 선호합니다. SF 기호는 플랫폼 간에 일관된 아이콘을 제공하는 데 사용할 수 있는 일관되고 구성 가능한 기호 집합을 제공합니다. iOS 및 MacOS 앱에서 사용할 사용자 지정 기호 이미지를 만들 수도 있습니다. 또한 macOS 11 이상은 액션, 추가 및 북마크의 제어 아이콘과 같은 AppKit 공유 이미지를 특정 기호에 자동으로 매핑합니다. 결과적으로, 당신의 앱은 이미 macOS 11 이상을 실행하는 Mac의 툴바와 같은 인터페이스 요소에 SF 심볼이 제공하는 심볼 이미지를 표시할 수 있다. SF 기호를 사용하면 앱의 아이콘 구조가 MacOS의 일반 아이콘 구조와 일치합니다.
>




For guidance, see [SF Symbols](../foundations/sf-symbols).

**Create platform-specific glyphs, if necessary.** If your iOS app uses custom glyphs that reference the platform in some way, create new glyphs that feel at home on the Mac. Xcode provides a separate asset catalog you can use in your iOS app for macOS-specific glyphs.
> 필요한 경우 플랫폼별 글리프를 만듭니다. iOS 앱에서 플랫폼을 참조하는 사용자 지정 글리프를 사용하는 경우 Mac에서 편안한 느낌의 새 글리프를 만듭니다. Xcode는 iOS 앱에서 MacOS별 글리프에 사용할 수 있는 별도의 자산 카탈로그를 제공합니다.
>




# **Settings**

If you supply app settings that appear in the iOS Settings app, your macOS app automatically displays a Settings menu item and a Settings window. If your iOS app uses child panes to hierarchically organize settings, macOS automatically adds a toolbar to the Settings window with a tab for each child pane. Each tab uses the standard system settings icon and the child pane’s title. When a user clicks the tab, they see the child pane’s settings items.
> iOS 설정 앱에 나타나는 앱 설정을 제공하면 macOS 앱에 설정 메뉴 항목과 설정 창이 자동으로 표시됩니다. iOS 앱이 하위 창을 사용하여 계층적으로 설정을 구성하는 경우 MacOS는 자동으로 각 하위 창에 대한 탭이 있는 설정 창에 도구 모음을 추가합니다. 각 탭에는 표준 시스템 설정 아이콘과 하위 창 제목이 사용됩니다. 사용자가 탭을 클릭하면 하위 창의 설정 항목이 표시됩니다.
>




As Mac users expect, your settings window appears when they choose the Settings menu item in your app menu. However, there are a few ways you can refine the display of your child panes and settings items and make your app’s settings experience feel more at home on the Mac.
> Mac 사용자의 예상대로 앱 메뉴에서 설정 메뉴 항목을 선택하면 설정 창이 나타납니다. 그러나 하위 창 및 설정 항목의 표시를 세분화하고 Mac에서 앱의 설정 경험을 보다 편안하게 느낄 수 있는 몇 가지 방법이 있습니다.
>




**Customize the icon for each tab.** Because macOS automatically uses the standard system-settings icon for your settings items, people will have to read each toolbar button’s title to distinguish among multiple items. To improve this experience, supply a custom icon for each settings item so that each tab displays a different icon.
> 각 탭의 아이콘을 사용자 지정합니다. MacOS는 자동으로 설정 항목에 표준 시스템 설정 아이콘을 사용하기 때문에 여러 항목을 구분하기 위해 각 도구 모음 단추의 제목을 읽어야 합니다. 이 환경을 개선하려면 각 설정 항목에 대해 사용자 지정 아이콘을 제공하여 각 탭에 다른 아이콘이 표시되도록 합니다.
>




**Make switch controls easier for macOS users to understand.** A switch in iOS Settings can include a small amount of text that provides more information about how the switch affects the user experience. Additionally, Mac apps, unlike iOS apps, often display a confirmation alert when the user uses a switch to make changes to a setting. To follow macOS platform conventions for app settings, provide a brief description to accompany a switch and specify content to display in a confirmation alert when people change a setting. For developer guidance, see [Displaying a Settings window](https://developer.apple.com/documentation/uikit/creating_a_mac_version_of_your_ipad_app/displaying_a_preferences_window).
> macOS 사용자가 쉽게 스위치 컨트롤을 이해할 수 있도록 합니다. iOS 설정의 스위치에는 스위치가 사용자 환경에 미치는 영향에 대한 자세한 정보를 제공하는 텍스트가 소량 포함될 수 있습니다. 또한 iOS 앱과 달리 Mac 앱은 사용자가 스위치를 사용하여 설정을 변경할 때 확인 알림을 표시하는 경우가 많습니다. 앱 설정에 대한 macOS 플랫폼 규칙을 따르려면 스위치와 함께 제공되는 간단한 설명을 제공하고 사용자가 설정을 변경할 때 확인 알림에 표시할 콘텐츠를 지정하십시오. 개발자 지침은 설정 창 표시를 참조하십시오.
>



