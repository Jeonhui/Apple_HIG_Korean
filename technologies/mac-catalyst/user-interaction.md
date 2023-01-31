# **[technologies-mac-catalyst] user-interaction**

Both iPad and Mac accept user input from a range of devices — such as the Multi-Touch display, keyboard, mouse, and trackpad. Typically, touch interactions inform iOS conventions, whereas keyboard and mouse interactions inform macOS conventions. When you create your Mac app with Mac Catalyst, first review differences between user interactions on iPad and Mac. Then, think about how users interact with your Mac app and make changes to follow macOS conventions.
> iPad와 Mac 모두 멀티 터치 디스플레이, 키보드, 마우스 및 트랙패드와 같은 다양한 장치의 사용자 입력을 허용합니다. 일반적으로 터치 상호 작용은 iOS 규칙을 알려주는 반면 키보드와 마우스 상호 작용은 MacOS 규칙을 알려줍니다. Mac Catalyst를 사용하여 Mac 앱을 만들 때는 먼저 iPad와 Mac의 사용자 상호 작용 간의 차이를 검토하십시오. 그런 다음 사용자가 Mac 앱과 어떻게 상호 작용하는지 생각하고 MacOS 규칙을 따르도록 변경하십시오.
>




For example, Mac users typically use a two-step process to interact with content and controls: they first select an object and then perform an action on it. Because time passes between these steps, the object’s selected state must persist until people finish choosing the action. Mac users expect this behavior — referred to as *selection persistence* — regardless of the input device they use.
> 예를 들어, Mac 사용자는 일반적으로 콘텐츠 및 컨트롤과 상호 작용하기 위해 2단계 프로세스를 사용합니다. 이러한 단계 사이에 시간이 경과하므로 사용자가 작업을 선택할 때까지 개체의 선택된 상태가 유지되어야 합니다. Mac 사용자는 사용하는 입력 장치에 관계없이 이 동작(선택 지속성이라고 함)을 기대합니다.
>




On the other hand, iPad users can perform actions either through gestures — which rarely depend on selection persistence — or by using a keyboard, mouse, or trackpad.
> 반면에 iPad 사용자는 제스처(선택 지속성에 거의 의존하지 않음) 또는 키보드, 마우스 또는 트랙패드를 사용하여 작업을 수행할 수 있습니다.
>




Here are some other examples that show how per-platform conventions can affect the user experience:
> 다음은 플랫폼별 규칙이 사용자 경험에 어떤 영향을 미칠 수 있는지 보여주는 몇 가지 다른 예입니다:
>




- Mac users appreciate Next and Previous buttons in place of iPad or trackpad gestures such as swiping among pages, especially if they use a mouse.
- >  Mac 사용자들은 특히 마우스를 사용할 때 아이패드 대신 다음과 이전 버튼을 사용하거나 페이지 사이를 스와이프하는 것과 같은 트랙패드 제스처를 좋아한다.

- Mac users expect to use the Delete key or choose a Delete command in a menu, so displaying a Delete button in the UI is usually unnecessary.
- >  Mac 사용자는 Delete 키를 사용하거나 메뉴에서 Delete 명령을 선택해야 하므로 UI에 Delete 버튼을 표시할 필요가 없습니다.

- Mac users expect a menu command or a button in a toolbar to load new content, while iPad users are accustomed to pulling down on a view to refresh its contents.
- >  Mac 사용자들은 메뉴 명령이나 도구 모음의 버튼이 새로운 콘텐츠를 로드하기를 기대하는 반면, iPad 사용자들은 보기를 내려 콘텐츠를 새로 고치는 데 익숙합니다.


As you translate iOS user interactions to Mac interactions, focus on letting people manipulate objects in ways that adhere to platform conventions. Take advantage of the fact that Mac users can easily use the keyboard and the mouse or trackpad at the same time. For example, let people select multiple cells in a collection view, change a persistent selection by using arrow keys or by pressing letter and number keys, or use keyboard shortcuts.
> iOS 사용자 상호 작용을 Mac 상호 작용으로 변환할 때 플랫폼 규칙을 준수하는 방식으로 사람들이 객체를 조작할 수 있도록 하는 데 초점을 맞춥니다. Mac 사용자는 키보드와 마우스 또는 트랙패드를 동시에 쉽게 사용할 수 있습니다. 예를 들어, 사용자가 모음 보기에서 여러 셀을 선택하거나, 화살표 키를 사용하거나, 문자 및 숫자 키를 눌러 영구 선택을 변경하거나, 바로 가기 키를 사용할 수 있습니다.
>




# **App menus**

On a Mac, the menu bar at the top of the screen gives people a consistent location for commands that control both apps and the system. The menu bar contains the current app’s standard and custom menus, in addition to the Apple menu, which lists system-level commands that are always available. Mac users expect every Mac app to make most commands available in the menu bar. Because iOS apps use controls to display commands in the main UI, finding a logical and intuitive menu bar location for every app command is a key part of the adaptation process.
> Mac에서 화면 상단의 메뉴 표시줄은 사람들에게 앱과 시스템을 모두 제어하는 명령을 위한 일관된 위치를 제공합니다. 메뉴 모음에는 항상 사용할 수 있는 시스템 수준 명령이 나열된 Apple 메뉴 외에 현재 앱의 표준 및 사용자 지정 메뉴가 포함되어 있습니다. Mac 사용자들은 모든 Mac 앱이 메뉴 모음에서 대부분의 명령어를 사용할 수 있기를 기대합니다. iOS 앱은 컨트롤을 사용하여 메인 UI에서 명령을 표시하기 때문에 모든 앱 명령에 대해 논리적이고 직관적인 메뉴 모음 위치를 찾는 것이 적응 과정의 핵심 부분입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/mac-catalyst-app-menu_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/mac-catalyst-app-menu_2x.png)

To design the menu bar menus for the Mac version of your app, start by listing all actions that people can perform and grouping them into the categories defined by the standard menu bar menus.
> 앱의 Mac 버전에 대한 메뉴 모음 메뉴를 설계하려면 먼저 사용자가 수행할 수 있는 모든 작업을 나열하고 표준 메뉴 모음 메뉴에서 정의한 범주로 그룹화합니다.
>




**NOTE**Most Mac apps include a View menu and a Window menu. Although these menus may seem similar, they have different purposes. People use the View menu to customize the appearance of app windows and to move among different functional areas, whereas they use the Window menu to navigate, organize, and manage the collection of windows in an app. For guidance, see [The menu bar](../components/system-experiences/the-menu-bar/).
> 참고대부분의 Mac 앱에는 보기 메뉴와 창 메뉴가 포함되어 있습니다. 이 메뉴들은 비슷해 보일 수 있지만, 다른 목적을 가지고 있다. 사람들은 보기 메뉴를 사용하여 앱 창의 모양을 사용자 지정하고 다른 기능 영역 간을 이동하는 반면, 창 메뉴를 사용하여 앱의 창 모음을 탐색, 구성 및 관리합니다. 자세한 내용은 메뉴 모음을 참조하십시오.
>




If some actions on your list don’t make sense in the standard menu bar menus, you might need to add a custom menu. Mac apps often add a custom menu bar menu for commands that are associated with either a core app object or a core app workflow. For example, Mail in macOS uses the Message and Mailbox menus to list commands that operate on these fundamental app objects. In contrast, Keynote uses the Arrange menu to list commands associated with the core workflow of arranging objects in a slide deck.
> 목록의 일부 작업이 표준 메뉴 모음 메뉴에서 의미가 없는 경우 사용자 지정 메뉴를 추가해야 할 수도 있습니다. Mac 앱은 종종 코어 앱 개체 또는 코어 앱 워크플로우와 관련된 명령에 대한 사용자 지정 메뉴 모음 메뉴를 추가합니다. 예를 들어 macOS의 메일은 메시지 및 편지함 메뉴를 사용하여 이러한 기본 앱 개체에서 작동하는 명령을 나열합니다. 반대로 키노트는 배열 메뉴를 사용하여 슬라이드 데크에서 객체를 배열하는 핵심 워크플로우와 관련된 명령을 나열합니다.
>




After you group your app’s actions into menus, order the items in each menu in a way that makes sense. Each standard menu defines a recommended order for items, so it’s important to follow this order for the items that you support. For example, Mac users expect the File menu to present items in this order:
> 앱의 작업을 메뉴로 그룹화한 후 각 메뉴의 항목을 합리적인 방법으로 정렬합니다. 각 표준 메뉴는 항목에 대한 권장 순서를 정의하므로 지원하는 항목에 대해 이 순서를 따르는 것이 중요합니다. 예를 들어 Mac 사용자는 파일 메뉴에서 다음 순서로 항목을 표시해야 합니다:
>




- New...
- Open...
- Open Recent
- Close

In a custom menu bar menu, order the items according to importance, frequency of use, or another scheme that makes sense in your app. Menu bar menus can also contain submenus and separators that help group items in logical ways. For guidance, see [Menus](../components/menus-and-actions/menus).
> 사용자 지정 메뉴 모음 메뉴에서 중요도, 사용 빈도 또는 앱에서 적합한 다른 구성표에 따라 항목을 정렬합니다. 메뉴 모음 메뉴에는 항목을 논리적으로 그룹화하는 데 도움이 되는 하위 메뉴 및 구분 기호가 포함될 수도 있습니다. 자세한 내용은 메뉴를 참조하십시오.
>




**DEVELOPER NOTE**To add and remove custom menus, use [UIMenuBuilder](https://developer.apple.com/documentation/uikit/uimenubuilder) and add menu items that represent your iOS app’s commands as menu items with [UICommand](https://developer.apple.com/documentation/uikit/uicommand).
> 개발자 참고 사용자 지정 메뉴를 추가 및 제거하려면 UIMenuBuilder를 사용하고 iOS 앱의 명령을 나타내는 메뉴 항목을 UI 명령을 사용하여 메뉴 항목으로 추가하십시오.
>




# **Keyboard input**

Mac users expect apps to support macOS keyboard conventions like keyboard shortcuts for common commands, and each key command usually comes with a corresponding men item in the menu bar.
> 맥 사용자들은 앱들이 공통 명령어를 위한 키보드 단축키와 같은 맥 OS 키보드 규칙을 지원하기를 기대하며, 각 키 명령어는 보통 메뉴 바에 해당하는 메뉴 항목과 함께 제공된다.
>




**Allow users to navigate your Mac app using the keyboard.** For example, map each major view area, such as each tab, to the keyboard shortcuts ⌘1, ⌘2, and so on. Then, add the key commands the View menu.
> 사용자가 키보드를 사용하여 Mac 앱을 탐색할 수 있도록 합니다. 예를 들어, 각 탭과 같은 각 주요 보기 영역을 키보드 단축키 ⌘1, ⌘2 등에 매핑합니다. 그런 다음 보기 메뉴에 키 명령을 추가합니다.
>




**DEVELOPER NOTE**To add menu items that support keyboard shortcuts for commands, use [UIKeyCommand](https://developer.apple.com/documentation/uikit/uikeycommand). For developer guidance, see [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/uicommand/adding_menus_and_shortcuts_to_the_menu_bar_and_user_interface).
> 개발자 참고명령에 대한 바로 가기 키를 지원하는 메뉴 항목을 추가하려면 UIKeyCommand를 사용하십시오. 개발자 지침은 메뉴 모음 및 사용자 인터페이스에 메뉴 및 바로 가기 추가를 참조하십시오.
>




**Support keyboard shortcuts for all common commands in your menus.** Both Mac users and iPad users who use keyboards can benefit from this change; for example:
> 메뉴의 모든 일반적인 명령에 대해 바로 가기 키를 지원합니다. 키보드를 사용하는 Mac 사용자와 iPad 사용자 모두 이 변경 사항의 혜택을 받을 수 있습니다. 예:
>




- Allow users who use keyboards to undo a previous action with a keyboard shortcut and a corresponding menu item instead of displaying an Undo button in the UI of your Mac app.
- >  키보드를 사용하는 사용자가 Mac 앱의 UI에 실행 취소 단추를 표시하는 대신 키보드 바로 가기 및 해당 메뉴 항목을 사용하여 이전 작업을 실행 취소할 수 있습니다.

- Remove the Delete button from the macOS version of your app and let people use the Delete key or the app’s Edit > Delete menu command instead.
- >  당신의 앱의 macOS 버전에서 삭제 버튼을 제거하고 사람들이 삭제 키나 앱의 편집 > 삭제 메뉴 명령을 대신 사용하도록 하세요.


For guidance, see [Custom keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#custom-keyboard-shortcuts).

For developer guidance, see [Accessing actions using menu elements](https://developer.apple.com/tutorials/mac-catalyst/accessing-actions-using-menu-elements) and [Take advantage of the delete menu element](https://developer.apple.com/tutorials/mac-catalyst/accessing-actions-using-menu-elements#Take-Advantage-of-the-Delete-Menu-Element).
> 개발자 지침은 메뉴 요소를 사용하여 작업 액세스 및 삭제 메뉴 요소 활용을 참조하십시오.
>




# **Help**

iOS apps usually offer help by directing users to an information section in the app or a website, whereas Mac users expect apps to offer onscreen help documentation through the Help menu bar menu. For guidance, see [Help menu](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#custom-keyboard-shortcuts) and [Offering help](../patterns/offering-help).
> iOS 앱은 일반적으로 사용자를 앱이나 웹사이트의 정보 섹션으로 안내함으로써 도움을 제공하는 반면, Mac 사용자들은 앱이 도움말 메뉴 모음 메뉴를 통해 화면에 나타나는 도움말 문서를 제공하기를 기대한다. 자세한 내용은 도움말 메뉴 및 제공 도움말을 참조하십시오.
>




# **Contextual menus**

Contextual menus help people discover actions they can perform on an object without opening a menu bar menu. If you support [context menus](../components/menus-and-actions/context-menus) in your iOS app, the system automatically converts them to contextual menus in the macOS version of your app.
> 상황에 맞는 메뉴를 사용하면 메뉴 모음 메뉴를 열지 않고도 개체에 대해 수행할 수 있는 작업을 찾을 수 있습니다. iOS 앱에서 상황별 메뉴를 지원하는 경우, 시스템은 자동으로 앱의 MacOS 버전에서 상황별 메뉴로 변환합니다.
>




To give Mac users the best experience, look for additional places to support contextual menus. For example, if there are common actions that people can perform on an object in your app, add a contextual menu that lists these actions. You can also add a contextual menu to a view that represents an object — for example, folder objects in the Finder support contextual menus that offer actions like Open in New Tab, Rename, and Duplicate.
> Mac 사용자에게 최상의 환경을 제공하려면 상황에 맞는 메뉴를 지원할 수 있는 추가 위치를 찾아보십시오. 예를 들어, 앱의 개체에 대해 사용자가 수행할 수 있는 일반적인 작업이 있는 경우 이러한 작업을 나열하는 상황에 맞는 메뉴를 추가합니다. 또한 개체를 나타내는 보기에 상황에 맞는 메뉴를 추가할 수도 있습니다. 예를 들어, 새 탭에서 열기, 이름 바꾸기 및 복제와 같은 작업을 제공하는 Finder의 폴더 개체가 상황에 맞는 메뉴를 지원합니다.
>




