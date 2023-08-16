### [[Components - System experiences](./translated-human-interface-guidelines-markdown/components/system-experiences.md)]  
  
# **The menu bar**  

----------------------------------------------------------------------



The Help menu — located at the trailing end of the menu bar — provides access to an app’s help documentation. When you use the Help Book format for this documentation, macOS automatically includes a search field at the top of the Help menu.

> 도움말 메뉴 - 메뉴 모음의 맨 끝에 있는 도움말 메뉴 - 앱의 도움말 문서에 액세스할 수 있습니다. 이 설명서에 도움말 북 형식을 사용하면 macOS가 도움말 메뉴 상단에 검색 필드를 자동으로 포함합니다.
>







| Menu item | Action | Guidance |

| --- | --- | --- |

| Send *YourAppName* Feedback to Apple | Opens the Feedback Assistant, in which people can provide feedback. |  |

| *YourAppName* Help | When the content uses the Help Book format, opens the content in the built-in Help Viewer. |  |

| *Additional Item* |  | Use a separator between your primary help documentation and additional items, which might include registration information or release notes. Keep the total the number of items you list in the Help menu small to avoid overwhelming people with too many choices when they need help. Alternatively, consider linking to additional items from within your help documentation. |



For guidance, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/offering-help)

> 자세한 내용은 [도움말 제공](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/offering-help) 을 참조하십시오
>

; for developer guidance, see [`NSHelpManager`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nshelpmanager)

> ; 개발자 지침은 ['NSHelpManager'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nshelpmanager) 를 참조하십시오
>

.



[Dynamic menu items](/design/human-interface-guidelines/the-menu-bar#Dynamic-menu-items)

----------------------------------------------------------------------------------------



In rare cases, it can make sense to present a *dynamic menu item*, which is a menu item that changes its behavior when people choose it while pressing a modifier key (Control, Option, Shift, or Command). For example, the *Minimize* item in the Window menu changes to *Minimize All* when people press the Option key.

> 드물게 수식어 키(Control, Option, Shift, Command)를 누른 상태에서 사람들이 선택하면 동작이 변경되는 메뉴 항목인 *dynamic menu 항목*을 제시하는 것이 합리적일 수 있습니다. 예를 들어 사용자가 옵션 키를 누르면 Windows 메뉴의 *Minimize* 항목이 *모두 최소화*로 변경됩니다.
>



**Avoid making a dynamic menu item the only way to accomplish a task.** Dynamic menu items are hidden by default, so they’re best suited to offer shortcuts to advanced actions that people can accomplish in other ways. For example, if someone hasn’t discovered the *Minimize All* dynamic menu item in the Window menu, they can still minimize each open window.

> **작업을 수행할 수 있는 유일한 방법은 동적 메뉴 항목을 사용하지 마십시오.** 동적 메뉴 항목은 기본적으로 숨겨져 있으므로 사용자가 다른 방법으로 수행할 수 있는 고급 작업에 대한 바로 가기를 제공하는 데 가장 적합합니다. 예를 들어 창 메뉴에서 *모두 최소화* 동적 메뉴 항목을 발견하지 못한 사용자도 열려 있는 각 창을 최소화할 수 있습니다.
>



**Use dynamic menu items primarily in menu bar menus.** Adding a dynamic menu item to contextual or Dock menus can make the item even harder for people to discover.

> ** 동적 메뉴 항목은 주로 메뉴 모음 메뉴에서 사용합니다.** 상황별 또는 도킹 메뉴에 동적 메뉴 항목을 추가하면 항목을 찾기가 더욱 어려워질 수 있습니다.
>



**Require only a single modifier key to reveal a dynamic menu item.** It can be physically awkward to press more than one key while simultaneously opening a menu and choosing a menu item, in addition to reducing the discoverability of the dynamic behavior. For developer guidance, see [`isAlternate`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsmenuitem/1514823-isalternate)

> **동적인 메뉴 항목을 나타내려면 단일 수정자 키만 필요합니다.** 동적 행동의 발견가능성을 감소시킬 뿐만 아니라, 메뉴를 열고 메뉴 항목을 선택하는 동시에 하나 이상의 키를 누르는 것은 물리적으로 불편할 수 있다. 개발자 지침은 ['is Alternate'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsmenuitem/1514823-isalternate) 를 참조하십시오
>

.



Tip



macOS automatically sets the width of a menu to hold the widest item, including dynamic menu items.

> macOS는 동적 메뉴 항목을 포함하여 가장 넓은 항목을 담을 수 있도록 메뉴 너비를 자동으로 설정합니다.
>



[Menu bar extras](/design/human-interface-guidelines/the-menu-bar#Menu-bar-extras)

----------------------------------------------------------------------------------



A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app. Menu bar extras are on the opposite side of the menu bar from your app’s menus. For developer guidance, see [`MenuBarExtra`](https://developer.apple.com/design/human-interface-guidelines/documentation/SwiftUI/MenuBarExtra)

> 메뉴 모음은 맨 앞에 있는 앱이 아닌 경우에도 앱이 실행 중일 때 메뉴 모음에 나타나는 아이콘을 사용하여 앱별 기능을 추가로 노출합니다. 추가 메뉴 모음은 앱의 메뉴에서 메뉴 모음의 반대쪽에 있습니다. 개발자 지침은 ['메뉴바]를 참조하십시오엑스트라'](https://developer.apple.com/design/human-interface-guidelines/documentation/SwiftUI/MenuBarExtra)
>

.



When necessary, the system hides menu bar extras to make room for app menus. Similarly, if there are too many menu bar extras, the system may hide some to avoid crowding app menus.

> 필요한 경우, 시스템은 앱 메뉴를 위한 공간을 만들기 위해 메뉴 바 추가를 숨깁니다. 마찬가지로, 메뉴 바 여분이 너무 많은 경우, 시스템은 앱 메뉴가 붐비는 것을 피하기 위해 일부를 숨길 수 있다.
>



![A screenshot of the Time Machine menu bar extra and its menu.](https://docs-assets.developer.apple.com/published/6241bbb0173be7b095716e2b46393f9b/menu-bar-extras@2x.png)



**Consider using a symbol to represent your menu bar extra.** You can create an [icon](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/icons)

> **메뉴 바를 추가로 나타내는 기호를 사용하는 것을 고려해 보십시오.** [아이콘](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/icons) 을 생성할 수 있습니다
>

 or you can choose one of the [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/sf-symbols)

> 또는 [SF 심볼](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/sf-symbols) 중 하나를 선택할 수 있습니다
>

, using it as-is or customizing it to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu bars, and when your menu bar extra is selected. The menu bar’s height is 24 pt.

> , 현재 상태로 사용하거나 필요에 따라 사용자 정의할 수 있습니다. 인터페이스 아이콘과 기호 모두 검은색과 선명한 색상을 사용하여 모양을 정의합니다. 시스템은 각 이미지의 검은색 영역에 다른 색상을 적용할 수 있으므로 어두운 메뉴 표시줄과 밝은 메뉴 표시줄에 모두 적합하고 메뉴 표시줄을 추가로 선택할 때도 적합합니다. 메뉴 바의 높이는 24pt입니다.
>



**Display a menu — not a popover — when people click your menu bar extra.** Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [popover](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/popovers)

> **사람들이 메뉴 표시줄을 추가로 클릭할 때 팝업이 아닌 메뉴를 표시합니다.** 노출하려는 앱 기능이 메뉴에 비해 너무 복잡하지 않다면 [팝오버](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/popovers) 에 표시하지 마십시오
>

.



**Let people — not your app — decide whether to put your menu bar extra in the menu bar.** Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of doing so during setup.

> **사용자의 앱이 아닌 사용자가 메뉴 바에 추가 메뉴 바를 배치할지 여부를 결정하도록 합니다.** 일반적으로 사람들은 앱의 설정 창에서 설정을 변경하여 메뉴 바에 메뉴 바를 추가합니다. 그러나 검색 가능성을 보장하기 위해 설정 중에 검색할 수 있는 옵션을 사용자에게 제공하는 것을 고려해 보십시오.
>



**Avoid relying on the presence of menu bar extras.** The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.

> **메뉴 바 엑스트라의 존재에 의존하지 마십시오.** 이 시스템은 메뉴 바 추가 기능을 숨기고 정기적으로 표시하며, 사용자가 메뉴 바 추가 기능의 위치를 표시하거나 예측하기 위해 선택한 다른 메뉴 바 추가 기능을 확신할 수 없습니다.
>



**Consider exposing app-specific functionality in other ways, too.** For example, you can provide a [Dock menu](https://developer.apple.com/design/human-interface-guidelines/dock-menus)

> **다른 방법으로도 앱별 기능을 노출하는 것을 고려해 보십시오.** 예를 들어 [Dock] 메뉴(https://developer.apple.com/design/human-interface-guidelines/dock-menus) 를 제공할 수 있습니다
>

 that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra, but a Dock menu is aways available when your app is running.

> 사용자가 앱의 [도크] 아이콘을 [제어] 클릭합니다. 사용자는 메뉴 모음을 숨기거나 추가로 사용하지 않도록 선택할 수 있지만, 앱이 실행 중일 때 도킹 메뉴를 사용할 수 있습니다.
>



[Platform considerations](/design/human-interface-guidelines/the-menu-bar#Platform-considerations)

--------------------------------------------------------------------------------------------------



*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

> *iOS, iPadOS, tvOS, 비전에서 지원되지 않음OS 또는 시계OS.*
>



[Resources](/design/human-interface-guidelines/the-menu-bar#Resources)

----------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/the-menu-bar#Related)



[Menus](/design/human-interface-guidelines/menus)





[Dock menus](/design/human-interface-guidelines/dock-menus)





[Keyboard shortcuts](/design/human-interface-guidelines/keyboards#Keyboard-shortcuts)





#### [Developer documentation](/design/human-interface-guidelines/the-menu-bar#Developer-documentation)



[`CommandMenu`](/documentation/SwiftUI/CommandMenu)





[Adding Menus and Shortcuts to the Menu Bar and User Interface](/documentation/uikit/uicommand/adding_menus_and_shortcuts_to_the_menu_bar_and_user_interface)





[`NSStatusBar`](/documentation/appkit/nsstatusbar)





