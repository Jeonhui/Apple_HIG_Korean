# **[technologies-mac-catalyst] introduction**

# When you use Mac Catalyst to create a Mac version of your iOS app, you make your app available to a new audience and give existing users the opportunity to enjoy it in a new environment.
> Mac Catalyst를 사용하여 iOS 앱의 Mac 버전을 만들 때 새로운 사용자가 앱을 사용할 수 있도록 하고 기존 사용자가 새로운 환경에서 즐길 수 있는 기회를 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Mac-Catalyst-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Mac-Catalyst-intro_2x.png)

# **Before you start**

Many iOS apps are great candidates for creating a Mac app with Mac Catalyst. This is especially true for iOS apps that already work well on iPad and support key iPad features; for example:
> 많은 iOS 앱은 Mac Catalyst로 Mac 앱을 만들 수 있는 좋은 후보입니다. 이는 iPad에서 이미 잘 작동하고 주요 iPad 기능을 지원하는 iOS 앱의 경우 특히 그렇습니다. 예:
>




**Drag and drop.** When you support drag and drop in your iOS app, you also get support for drag and drop in the Mac version.
> 드래그 앤 드롭 iOS 앱에서 드래그 앤 드롭을 지원하면 Mac 버전에서도 드래그 앤 드롭을 지원합니다.
>




**Keyboard shortcuts.** Even though a physical keyboard may not always be available on iPad, iPad users appreciate using keyboard shortcuts to streamline their interaction with your app. On the Mac, users always expect apps to offer keyboard shortcuts. By supporting keyboard shortcuts in your iOS app, you make it easy to add support for common macOS shortcuts to your Mac app.
> 키보드 단축키 iPad에서 물리적 키보드를 항상 사용할 수 있는 것은 아니지만, iPad 사용자는 키보드 단축키를 사용하여 앱과의 상호 작용을 간소화하는 것을 좋아합니다. 맥에서 사용자들은 앱이 키보드 단축키를 제공하기를 항상 기대한다. iOS 앱에서 바로 가기 키를 지원하면 Mac 앱에 일반 MacOS 바로 가기를 쉽게 추가할 수 있습니다.
>




**Multitasking.** Apps that do a good job scaling the interface to support Split View, Slide Over, and Picture in Picture lay the necessary groundwork to support the extensive window resizability that Mac users expect.
> 멀티태스킹. 인터페이스를 잘 확장하여 스플릿 뷰, 슬라이드 오버 및 그림을 지원하는 앱은 Mac 사용자가 기대하는 광범위한 창 크기 조정 기능을 지원하는 데 필요한 기반을 마련합니다.
>




**Support for multiple windows.** By supporting multiple scenes on iPad, you also get support for multiple windows in the macOS version.
> 여러 창 지원. iPad에서 여러 장면을 지원하면 MacOS 버전에서도 여러 창을 지원할 수 있습니다.
>




An iOS app that works well on iPad is a solid foundation for creating a Mac App with Mac Catalyst. However, some apps rely on frameworks or features that don’t exist on a Mac. For example, if your app’s essential features require capabilities like gyroscope, accelerometer, or rear camera, frameworks like HealthKit or ARKit, or if the app’s main function is something like navigation, it might not be suitable for the Mac.
> 아이패드에서 잘 작동하는 iOS 앱은 Mac Catalyst로 Mac App을 만들 수 있는 견고한 기반입니다. 그러나 일부 앱은 Mac에 없는 프레임워크나 기능에 의존합니다. 예를 들어, 앱의 필수 기능이 자이로스코프, 가속도계 또는 후면 카메라와 같은 기능, HealthKit 또는 ARKit와 같은 프레임워크를 필요로 하거나 앱의 주요 기능이 탐색과 같은 것이라면 Mac에 적합하지 않을 수 있습니다.
>




For developer guidance, see [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst). For Mac app–design guidance, see [Designing for macOS](../platforms/designing-for-macos).
> 개발자 지침은 Mac Catalyst를 참조하십시오. Mac 앱 설계 지침은 MacOS용 설계를 참조하십시오.
>




# **Planning enhancements for your Mac app**
> Mac 앱의 향상된 기능 계획
>




Creating a Mac version of your iOS app with Mac Catalyst gives the app automatic support for fundamental macOS features such as:
> Mac Catalyst를 사용하여 iOS 앱의 Mac 버전을 만들면 앱에서 다음과 같은 기본적인 MacOS 기능을 자동으로 지원합니다:
>




- Keyboard, trackpad, mouse, and Touch Bar input, including key focus and keyboard navigation
- >  키 포커스 및 키보드 탐색을 포함한 키보드, 트랙패드, 마우스 및 터치 바 입력

- Window management
- Toolbar support
- Rich text interaction, including copy and paste as well as contextual menus for editing
- >  편집을 위한 상황별 메뉴뿐만 아니라 복사 및 붙여넣기를 포함한 리치 텍스트 상호 작용

- File management
- Pull-down menus
- App-specific settings in the system-provided Settings app
- >  시스템에서 제공하는 설정 앱의 앱별 설정


System-provided UI elements take on a more Mac-like appearance, too, for example:
> 시스템에서 제공하는 UI 요소는 다음과 같이 Mac과 유사한 모양을 취합니다:
>




- Split view
- File browser
- Activity view
- Form sheet
- Contextual actions
- Color picker

**DEVELOPER NOTE**To get an overview of how views and controls change when you create a Mac app with Mac Catalyst, download [UIKit Catalog: creating and customizing views and controls](https://developer.apple.com/documentation/uikit/mac_catalyst/uikit_catalog_creating_and_customizing_views_and_controls) and build the macOS target.
> 개발자 참고 Mac Catalyst로 Mac 앱을 만들 때 보기와 컨트롤이 어떻게 변하는지 개요를 보려면 UIKit Catalog를 다운로드하십시오. 보기와 컨트롤을 만들고 사용자 지정하며 MacOS 대상을 구축하십시오.
>




When you first create a Mac app with Mac Catalyst, Xcode defaults to the "Scale Interface to Match iPad" setting, or *iPad idiom*. This setting allows you to create a Mac app without making big changes to your app’s layout. By choosing the iPad idiom, standard iOS interface elements retain their appearance in the Mac version of your iOS app; for example, the switch control retains its iOS appearance. In addition, the system scales the app’s interface to ensure that text and interface elements are consistent with the macOS display environment without requiring you to update your app’s layout.
> Mac Catalyst로 Mac 앱을 처음 만들 때 Xcode는 기본적으로 "iPad에 맞게 인터페이스 크기 조정" 설정 또는 iPad 관용구로 설정됩니다. 이 설정을 사용하면 앱 레이아웃을 크게 변경하지 않고 Mac 앱을 만들 수 있습니다. iPad 관용구를 선택하면 표준 iOS 인터페이스 요소는 iOS 앱의 Mac 버전에서 모양을 유지합니다. 예를 들어, 스위치 컨트롤은 iOS 모양을 유지합니다. 또한 시스템은 앱의 레이아웃을 업데이트할 필요 없이 텍스트 및 인터페이스 요소가 MacOS 디스플레이 환경과 일관되도록 앱의 인터페이스를 조정합니다.
>




As an alternative to choosing the iPad idiom, you can choose the "Optimize Interface for Mac" setting, or *Mac idiom*, in Xcode. With the Mac idiom, your app takes on an even more Mac-like appearance and the system doesn’t scale your app’s layout. As a result, text and graphics appear sharper, making your app look its best on the Mac. However, adopting the Mac idiom often requires you to do additional work on your app’s layout.
> iPad 관용구를 선택하는 대신 Xcode에서 "Optimize Interface for Mac" 설정 또는 Mac 관용구를 선택할 수 있습니다. Mac 관용구를 사용하면 앱이 Mac과 훨씬 더 유사한 모양을 하고 시스템은 앱의 레이아웃을 조정하지 않습니다. 결과적으로, 텍스트와 그래픽이 더 선명하게 나타나며, Mac에서 당신의 앱을 가장 잘 보이게 한다. 그러나 Mac 관용구를 채택하려면 앱 레이아웃에 대한 추가 작업이 필요한 경우가 많습니다.
>




When you create a Mac version of your iOS app, initially choose the iPad idiom and make the app feel at home on the Mac by adopting macOS app structure, navigation conventions, and design patterns. After you complete this work, consider switching to the Mac idiom, especially if your app displays a lot of text, detailed artwork, or uses animations.
> iOS 앱의 Mac 버전을 만들 때는 먼저 iPad 관용구를 선택하고 Mac OS 앱 구조, 탐색 규칙 및 디자인 패턴을 채택하여 Mac에서 앱을 편안하게 느끼십시오. 이 작업을 완료한 후 Mac 관용구로 전환하는 것을 고려해 보십시오. 특히 앱에 많은 텍스트가 표시되거나 자세한 그림이 표시되거나 애니메이션이 사용되는 경우에는 더욱 그렇습니다.
>




For guidance, see [Mac idiom](../technologies/mac-catalyst/mac-idiom).

# **Reviewing platform conventions and design patterns**
> 플랫폼 규칙 및 설계 패턴 검토
>




When you create a Mac version of your iOS app with Mac Catalyst, you need to ensure that your Mac app gives people a rich Mac experience. No matter whether you adopt the iPad idiom or the Mac idiom, it’s essential to go beyond simply displaying your iOS layout in a macOS window. iOS and macOS each define design patterns and conventions for user interaction that are rooted in the different ways people use their devices. Before you dive in and update specific views and controls, become familiar with the main differences between the platforms so you can create a great Mac app.
> Mac Catalyst로 iOS 앱의 Mac 버전을 만들 때 Mac 앱이 사람들에게 풍부한 Mac 경험을 제공하는지 확인해야 합니다. iPad 관용구를 채택하든 Mac 관용구를 채택하든 단순히 iOS 레이아웃을 macOS 창에 표시하는 것을 넘어서야 합니다. iOS와 macOS는 각각 사람들이 기기를 사용하는 다양한 방식에 뿌리를 둔 사용자 상호 작용을 위한 디자인 패턴과 규칙을 정의합니다. 특정 보기와 컨트롤을 탐색하고 업데이트하기 전에 플랫폼 간의 주요 차이점을 숙지하여 훌륭한 Mac 앱을 만들 수 있습니다.
>




Differences in conventions and design patterns with the biggest impact on the Mac version of your iOS app exist in the following key areas:
> iOS 앱의 Mac 버전에 가장 큰 영향을 미치는 규칙과 디자인 패턴의 차이는 다음과 같은 주요 영역에 있습니다:
>




**Navigation.** Many iOS and macOS apps organize data in similar ways, but they use different controls and visual indicators to help people understand and navigate through the data. For guidance, see [App structure and navigation](../technologies/mac-catalyst/app-structure).
> 내비게이션. 많은 iOS와 macOS 앱들은 비슷한 방식으로 데이터를 구성하지만, 사람들이 데이터를 이해하고 탐색하는 것을 돕기 위해 서로 다른 컨트롤과 시각적 표시기를 사용한다. 자세한 내용은 앱 구조 및 탐색을 참조하십시오.
>




**User input and interactions.** Although both iPad and Mac accept user input from a range of devices — such as the Multi-Touch display, keyboard, mouse, and trackpad — touch interactions are the basis for iOS conventions. In contrast, keyboard and mouse interactions are key for macOS conventions. For guidance, see [User interaction](../mac-catalyst/overview/user-interaction).
> iPad와 Mac 모두 Multi-Touch 디스플레이, 키보드, 마우스 및 트랙패드와 같은 다양한 장치의 사용자 입력을 허용하지만 터치 상호 작용은 iOS 규칙의 기본입니다. 대조적으로, 키보드와 마우스의 상호작용은 macOS 규칙의 핵심이다. 자세한 내용은 사용자 상호 작용을 참조하십시오.
>




**Menus.** Mac users are familiar with the persistent menu bar and expect to find all app commands in menu-bar menus. iOS, on the other hand, doesn’t have a persistent menu bar, and iOS users expect to find app commands in the app’s UI. For guidance, see [App menus](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/user-interaction#app-menus).
> 메뉴. Mac 사용자는 영구 메뉴 모음에 익숙하며 모든 앱 명령을 메뉴 모음 메뉴에서 찾을 수 있기를 기대합니다. 반면 iOS는 영구 메뉴 모음이 없으며 iOS 사용자는 앱 UI에서 앱 명령을 찾을 수 있기를 기대합니다. 자세한 내용은 앱 메뉴를 참조하십시오.
>




**Visual design and layout.** To take advantage of the wider Mac screen in ways that give Mac users a great experience, update your app’s visual design and layout; for example:
> 시각적 디자인 및 레이아웃. Mac 사용자에게 좋은 경험을 제공하는 방식으로 더 넓은 Mac 화면을 활용하려면 다음과 같이 앱의 시각적 디자인 및 레이아웃을 업데이트하십시오:
>




- Divide a single column of content and actions into multiple columns.
- >  내용 및 작업의 단일 열을 여러 열로 나눕니다.

- Present an inspector UI next to the main content instead of using a popover.
- >  팝업을 사용하는 대신 기본 콘텐츠 옆에 검사기 UI를 표시합니다.

- Simultaneously show two or more levels of an app’s hierarchy.
- >  두 개 이상의 앱 계층 수준을 동시에 표시합니다.

- Adopt the Mac idiom to make your app’s appearance even more Mac-like.
- >  Mac 관용구를 채택하여 앱의 모양을 Mac과 더욱 유사하게 만드십시오.


For guidance, see [Visual design](../technologies/mac-catalyst/visual-design).

Viewing your iPad app from the perspective of macOS design conventions can also suggest ways to also improve the iPad version, especially if your iPad app originate on iPhone. As you reassess the ways you lay out views and controls in your Mac app, consider this as an opportunity to see if there are places where you can improve your iOS app to make better use of the large iPad screen.
> 또한 iPad 앱을 macOS 디자인 규칙의 관점에서 보는 것은 iPad 버전을 개선하는 방법을 제안할 수 있습니다. 특히 iPad 앱이 iPhone에서 시작되는 경우에는 더욱 그렇습니다. Mac 앱에서 보기와 컨트롤을 배치하는 방법을 다시 평가할 때, iOS 앱을 개선하여 대형 iPad 화면을 더 잘 활용할 수 있는 곳이 있는지 확인할 수 있는 기회로 여기십시오.
>



