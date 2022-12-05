# **[components-status] the-menu-bar**

## On a Mac, the menu bar at the top of the screen displays the top-level menus in your app or game, which typically include both system-provided menus and custom ones.
> Mac에서는 화면 상단의 메뉴 표시줄에 앱 또는 게임의 최상위 메뉴가 표시되며, 일반적으로 시스템에서 제공하는 메뉴와 사용자 지정 메뉴가 모두 포함됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/the-menu-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/the-menu-bar-intro-dark_2x.png)

Mac users are very familiar with the macOS menu bar, and they rely on it to help them learn what an app does and find the commands they need. To help your app or game feel at home in macOS, it’s essential to provide a consistent menu bar experience.
> Mac 사용자들은 MacOS 메뉴 모음에 매우 익숙하며, 앱이 무엇을 하는지 배우고 필요한 명령을 찾는 데 도움을 주기 위해 Mac OS 메뉴 모음에 의존합니다. MacOS에서 앱이나 게임이 집에 있는 것처럼 느끼도록 하려면 일관된 메뉴 모음 경험을 제공하는 것이 필수적이다.
>




**NOTE**In iPadOS, an app’s keyboard shortcuts can appear in the shortcut interface that displays when people hold the Command key on an attached hardware keyboard. The shortcut interface is similar in appearance and organization to the menu bar in macOS — and it can contain familiar menu items like New Window and Copy — but unlike the menu bar, it doesn’t contain every command an app supports. For guidance, see [Keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/#keyboard-shortcuts).
> 참고 iPadOS에서 앱의 바로 가기 키는 연결된 하드웨어 키보드에서 명령 키를 누를 때 표시되는 바로 가기 인터페이스에 나타날 수 있습니다. 바로 가기 인터페이스는 MacOS의 메뉴 모음과 모양과 구성이 비슷하며 새 창 및 복사와 같은 친숙한 메뉴 항목을 포함할 수 있지만 메뉴 모음과 달리 앱이 지원하는 모든 명령을 포함하지는 않습니다. 자세한 내용은 바로 가기 키를 참조하십시오.
>




Menus in the menu bar share most of the appearance and behavior characteristics that all menu types have. To learn about menus in general — and how organize and label menu items — see [Menus](../components/menus-and-actions/menus).
> 메뉴 모음의 메뉴는 모든 메뉴 유형이 가지는 모양 및 동작 특성의 대부분을 공유합니다. 메뉴에 대한 일반적인 내용과 메뉴 항목 구성 및 레이블 지정 방법에 대한 자세한 내용은 메뉴를 참조하십시오.
>




# **Anatomy**

The Apple menu, which is always the first item on the leading side of the menu bar, includes system-defined menu items that are always available. You can’t modify or remove the Apple menu.
> 항상 메뉴 모음의 맨 앞에 있는 첫 번째 항목인 Apple 메뉴에는 항상 사용할 수 있는 시스템 정의 메뉴 항목이 포함되어 있습니다. Apple 메뉴는 수정하거나 제거할 수 없습니다.
>




When present in the menu bar, the following menus appear after the Apple menu in the order listed below.
> 메뉴 표시줄에 표시되면 아래 나열된 순서대로 Apple 메뉴 뒤에 다음 메뉴가 나타납니다.
>




- *AppName* (you supply a short version of your app’s name for this menu’s title)
- >  AppName(이 메뉴의 제목에 대한 앱 이름의 짧은 버전을 제공합니다.)

- File
- Edit
- Format
- View
- App-specific menus, if any
- Window
- Help

Space permitting, the system can display menu bar extras in the trailing end of the menu bar. A *menu bar extra* provides a menu of app- or system-defined items that people can access in most contexts. With the exception of essential menu bar extras, like Clock, people choose the menu bar extras they want to keep in the menu bar. For example, people might want to include the system-provided Bluetooth menu bar extra to help them manage Bluetooth connections at any time. For guidance, see [Menu bar extras](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#menu-bar-extras).
> 공간이 허용되면 시스템은 메뉴 모음의 뒤쪽 끝에 추가 메뉴 모음을 표시할 수 있습니다. 메뉴 모음 추가 기능은 대부분의 컨텍스트에서 사용자가 액세스할 수 있는 앱 또는 시스템 정의 항목의 메뉴를 제공합니다. 시계와 같은 필수 메뉴 모음 추가 기능을 제외하고, 사람들은 메뉴 모음에서 보관할 메뉴 모음 추가 기능을 선택합니다. 예를 들어 언제든지 Bluetooth 연결을 관리할 수 있도록 시스템에서 제공하는 Bluetooth 메뉴 모음을 추가로 포함할 수 있습니다. 자세한 내용은 추가 메뉴 모음을 참조하십시오.
>




