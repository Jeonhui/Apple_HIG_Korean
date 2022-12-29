# **[inputs] keyboards**

## A physical keyboard can be an essential input device for entering text, navigating, performing actions, and more.
> 실제 키보드는 텍스트 입력, 탐색, 작업 수행 등에 필수적인 입력 장치가 될 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-keyboard-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-keyboard-intro_2x.png)

On a Mac, some people prefer using a keyboard instead of a mouse or a trackpad, and VoiceOver users require it. People can also connect an external keyboard to their iPhone, iPad, or TV.
> Mac에서 일부 사용자는 마우스나 트랙패드 대신 키보드를 사용하는 것을 선호하며 VoiceOver 사용자는 이를 필요로 합니다. 사람들은 또한 외부 키보드를 그들의 아이폰, 아이패드, TV에 연결할 수도 있다.
>




When a physical keyboard is available, people often rely on *keyboard shortcuts*, which offer efficient ways to initiate actions without using a mouse or trackpad to navigate a menu or click a button.
> 실제 키보드를 사용할 수 있는 경우 사용자는 마우스나 트랙패드를 사용하여 메뉴를 탐색하거나 단추를 클릭하지 않고도 작업을 시작할 수 있는 효율적인 방법을 제공하는 바로 가기 키에 의존하는 경우가 많습니다.
>




# **Best practices**

**Support keyboard-only interaction where possible.** As the name suggests, full keyboard-access mode lets people navigate and activate windows, menus, controls, and system features using only the keyboard. To learn more, see [Navigate your app using Full Keyboard Access](https://support.apple.com/guide/mac-help/navigate-your-mac-using-full-keyboard-access-mchlc06d1059/mac) and [Adjust the onscreen and external keyboard settings on iPad](https://support.apple.com/guide/ipad/keyboards-ipad424a3e13/ipados). In iPadOS, you can enhance the experience of using a connected keyboard with your app by customizing visual effects that help people focus on individual items as they navigate your interface. For guidance, see [Keyboard navigation on iPad](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#keyboard-navigation-on-ipad).
> 이름에서 알 수 있듯이 전체 키보드 액세스 모드를 사용하면 키보드만 사용하여 창, 메뉴, 컨트롤 및 시스템 기능을 탐색하고 활성화할 수 있습니다. 자세한 내용은 전체 키보드 액세스를 사용하여 앱 탐색 및 iPad의 화면 및 외부 키보드 설정 조정의 정보를 참조하십시오. iPadOS에서는 사용자가 인터페이스를 탐색할 때 개별 항목에 집중할 수 있도록 시각적 효과를 사용자 지정하여 앱과 연결된 키보드를 사용하는 경험을 향상시킬 수 있습니다. 자세한 내용은 iPad의 키보드 탐색을 참조하십시오.
>




# **Keyboard shortcuts**

Most keyboard shortcuts consist of a combination of keys: a single primary key and one or more of the modifier keys (Command, Shift, Control, and Option). A rare exception is the Esc (Escape) key, which people can use as a shortcut to invoke a cancel action in various contexts.
> 대부분의 바로 가기 키는 단일 기본 키와 하나 이상의 한정자 키(명령, Shift, 제어 및 옵션)의 조합으로 구성됩니다. 드문 예외는 Esc(Escape) 키로, 사람들은 다양한 컨텍스트에서 취소 작업을 호출하는 바로 가기로 사용할 수 있습니다.
>




People discover keyboard shortcuts in a couple of ways. For example, a macOS app lists its keyboard shortcuts in its menu bar menus (to learn more, see [The menu bar](../components/system-experiences/the-menu-bar)).
> 사람들은 몇 가지 방법으로 키보드 단축키를 발견한다. 예를 들어, macOS 앱은 메뉴 모음 메뉴에 키보드 단축키를 나열합니다(자세한 내용은 메뉴 모음 참조).
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/menus-in-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/menus-in-macos_2x.png)

The keyboard shortcuts in an iPadOS app appear in the shortcut interface that displays when people hold the Command key on a connected keyboard. Similar in organization to an app’s menu bar menus on a Mac, the shortcut interface on iPad displays app commands in familiar system-defined menu categories such as File, Edit, and View. Unlike menu bar menus, the iPad interface displays all relevant categories in one view, listing within each category only available commands that also have shortcuts.
> iPadOS 앱의 바로 가기 키는 연결된 키보드에서 명령 키를 누를 때 표시되는 바로 가기 인터페이스에 나타납니다. Mac의 앱 메뉴 모음 메뉴와 유사하게 iPad의 바로 가기 인터페이스는 파일, 편집 및 보기와 같은 친숙한 시스템 정의 메뉴 범주에 앱 명령을 표시합니다. 메뉴 모음 메뉴와 달리 iPad 인터페이스는 모든 관련 범주를 하나의 보기에 표시하며, 각 범주 내에 바로 가기가 있는 사용 가능한 명령만 나열합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/keyboard-shortcut-interface_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/keyboard-shortcut-interface_2x.png)

**Respect standard keyboard shortcuts.** People expect the standard keyboard shortcuts to work, regardless of the app they’re using. You can also help people learn your app quickly by supporting the [system-defined keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards#reserved-keyboard-shortcuts) that make sense in your app.
> 표준 키보드 단축키를 존중합니다. 사람들은 사용 중인 앱에 관계없이 표준 키보드 단축키가 작동하기를 기대합니다. 또한 앱에서 의미 있는 시스템 정의 키보드 단축키를 지원하여 사용자가 앱을 빠르게 학습할 수 있도록 지원할 수 있습니다.
>




**In general, don’t repurpose standard keyboard shortcuts for custom actions.** People can get confused when the shortcuts they know work differently in your app. Only consider redefining a standard shortcut if its action doesn’t make sense in your app. For example, an app that doesn’t support text editing doesn’t need a text-styling command like Italic, so it might use Command–I for an action that has more relevance in the app, such as Get Info.
> 일반적으로 사용자 지정 작업을 위해 표준 키보드 단축키의 용도를 변경하지 마십시오. 앱에서 사용자가 알고 있는 단축키가 다르게 작동하면 사용자가 혼동할 수 있습니다. 앱에서 해당 작업이 의미가 없는 경우에만 표준 바로 가기를 재정의하는 것을 고려하십시오. 예를 들어 텍스트 편집을 지원하지 않는 앱은 이탈릭과 같은 텍스트 스타일 명령이 필요하지 않으므로 Get Info와 같이 앱에서 더 관련성이 높은 작업에 Command-I를 사용할 수 있습니다.
>




**Define custom keyboard shortcuts for only the most common actions in your app.** People appreciate using keyboard shortcuts for app-specific actions they perform frequently, but defining too many new shortcuts risks making your app seem difficult to learn and can clutter the shortcut interface in an iPadOS app. Minimizing app-specific keyboard shortcuts also helps avoid potential conflicts with system-defined shortcuts that may be in place.
> 앱에서 가장 일반적인 작업에 대해서만 사용자 지정 키보드 바로 가기를 정의합니다. 사람들은 자주 수행하는 앱별 작업에 키보드 바로 가기를 사용하는 것을 좋아하지만, 너무 많은 새로운 바로 가기를 정의하면 앱을 학습하기 어려워 보이고 iPadOS 앱의 바로 가기 인터페이스가 혼란스러울 수 있습니다. 또한 앱별 바로 가기 키를 최소화하면 시스템 정의 바로 가기와 충돌할 가능성을 방지할 수 있습니다.
>




**Let people use modifier and other keys to adjust the behavior of some interactions.** For example, pressing Command while dragging moves items as a group, and pressing Shift while drag-resizing constrains resizing to the item’s aspect ratio. In addition, holding an arrow key moves the selected item by the smallest app-defined unit of distance until people release the key.
> 예를 들어 끌면서 명령을 누르면 항목이 그룹으로 이동하고 끌어서 크기를 조정하면 항목의 가로 세로 비율로 크기가 조정됩니다. 또한 화살표 키를 누르면 사용자가 키를 놓을 때까지 선택한 항목이 가장 작은 앱 정의 거리 단위만큼 이동합니다.
>




# **Custom keyboard shortcuts**

It’s important for custom keyboard shortcuts to use modifier keys in ways that people expect.
> 사용자 지정 바로 가기 키는 사람들이 예상하는 방식으로 수정자 키를 사용하는 것이 중요합니다.
>




Here are the modifier keys and the symbols that represent them.
> 다음은 수식자 키와 이를 나타내는 기호입니다.
>




[제목 없음](https://www.notion.so/f4f77f527d9e44ae9000234f5b840435)

**Prefer the Command key as the main modifier key in a custom keyboard shortcut.** Most standard keyboard shortcuts use the Command key, so people are familiar with it.
> 대부분의 표준 키보드 단축키는 명령 키를 사용하기 때문에 사용자 지정 키보드 단축키의 주 수정자 키로 사용합니다.
>




**Prefer the Shift key as a secondary modifier when the shortcut complements another shortcut.** For example, Command-P displays the Print dialog in most apps. The standard shortcut for the Page Setup dialog, which complements printing, is typically Shift-Command-P.
> 바로 가기가 다른 바로 가기를 보완할 때 Shift 키를 보조 수정자로 사용합니다. 예를 들어 Command-P는 대부분의 앱에서 인쇄 대화 상자를 표시합니다. 인쇄를 보완하는 페이지 설정 대화상자의 표준 바로 가기는 일반적으로 Shift-Command-P입니다.
>




**Use the Option modifier sparingly.** For example, you might use Option in the shortcut for a less-common command or a convenience or power feature. For example, the Finder uses Option-Command-W for Close All Windows and Option-Command-M for Minimize All Windows.
> 옵션 한정자를 사용하지 마십시오. 예를 들어, 일반적이지 않은 명령이나 편리한 기능 또는 전원 기능을 위해 바로 가기에서 옵션을 사용할 수 있습니다. 예를 들어, Finder는 모든 창 닫기에 Option-Command-W를 사용하고 모든 창 최소화에 Option-Command-M을 사용합니다.
>




**As much as possible, avoid using the Control key as a modifier.** The system uses Control in many systemwide features, like moving focus or capturing screenshots.
> 가능한 한 제어 키를 수식어로 사용하지 마십시오. 시스템은 포커스 이동 또는 스크린샷 캡처와 같은 많은 시스템 전체 기능에서 제어를 사용합니다.
>




