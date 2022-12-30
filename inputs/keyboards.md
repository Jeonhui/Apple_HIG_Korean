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




**Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command.** For example, because people are accustomed to using Command-Z for undoing an action, it would be confusing to use Shift-Command-Z as the shortcut for a command that’s unrelated to undo and redo.
> 관련이 없는 명령에 대한 기존 바로 가기에 수정자를 추가하여 새 바로 가기를 만들지 마십시오. 예를 들어, 작업을 실행 취소하는 데 Command-Z를 사용하는 데 익숙하기 때문에 실행 취소 및 다시 실행과 관련이 없는 명령에 대한 바로 가기로 Shift-Command-Z를 사용하면 혼란스러울 수 있습니다.
>




**List modifier keys in the correct order.** If you use more than one modifier key in a custom shortcut, always list them in this order: Control, Option, Shift, Command.
> 수정자 키를 올바른 순서로 나열합니다. 사용자 지정 바로 가기에서 두 개 이상의 수정자 키를 사용하는 경우 항상 다음 순서로 나열하십시오. 제어, 옵션, 시프트, 명령.
>




**Identify a two-character key by its lower character unless Shift is part of the shortcut.** For example, the keyboard shortcut for Hide Status Bar is Command-Slash (/). If the Shift key is part of the keyboard shortcut, identify the key using the upper of the two characters. For example, the keyboard shortcut for Help is Command-Question Mark (?), not Shift-Command-Slash.
> Shift가 바로 가기의 일부가 아닌 경우 두 문자 키를 소문자로 식별합니다. 예를 들어, 상태 숨기기 표시줄의 바로 가기 키는 명령 슬래시(/)입니다. Shift 키가 바로 가기 키의 일부인 경우 두 문자 중 위쪽을 사용하여 키를 식별합니다. 예를 들어, 도움말의 바로 가기 키는 Shift-Command-Slash가 아니라 명령-질문 표시(?)입니다.
>




**TIP**Some languages require modifier keys to generate certain characters. For example, on a French keyboard, Option-5 generates the “{“ character. It’s usually safe to use the Command key as a modifier, but avoid using an additional modifier with characters that aren’t available on all keyboards. If you must use a modifier other than Command, prefer using it only with the alphabetic characters.
> 팁 일부 언어에서는 특정 문자를 생성하기 위해 수식자 키가 필요합니다. 예를 들어 프랑스어 키보드에서 옵션-5는 "{" 문자를 생성합니다. 일반적으로 명령 키를 한정자로 사용하는 것이 안전하지만 일부 키보드에서는 사용할 수 없는 문자와 함께 추가 한정자를 사용하지 않도록 합니다. 명령 이외의 수식어를 사용해야 하는 경우, 영문자로만 사용하는 것을 선호합니다.
>




**Let the system localize and mirror your keyboard shortcuts as needed.**For example, iPadOS automatically localizes a shortcut’s primary key and modifier keys to support the currently connected keyboard. Also, if your app switches to a right-to-left layout, the system automatically mirrors the shortcut. For guidance, see [Right to left](../foundations/right-to-left).
> 시스템이 필요에 따라 키보드 단축키를 현지화하고 미러링하도록 합니다.예를 들어, iPadOS는 자동으로 단축키의 기본 키와 수정자 키를 현지화하여 현재 연결된 키보드를 지원합니다. 또한 앱이 오른쪽에서 왼쪽 레이아웃으로 전환되면 시스템이 자동으로 바로 가기를 미러링합니다. 자세한 내용은 오른쪽에서 왼쪽을 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, macOS, or tvOS. Not supported in watchOS.*
> iOS, macOS 또는 tvOS에 대한 추가 고려사항은 없습니다. 워치에서 지원되지 않음운영 체제
>




# **iPadOS**

**Help people discover available actions in your iPadOS app.** Because the iPad shortcut interface displays a flat list of all items in each category, submenu titles aren’t available to provide context for their child items. For example, the item titles Name and Date Added don’t make sense without the context of the submenu title Sort Bookmarks By. You can enhance each item’s title by including the necessary context, such as Sort Bookmarks by Name and Sort Bookmarks by Date Added. For developer guidance, see [discoverabilityTitle](https://developer.apple.com/documentation/uikit/uikeycommand/1621094-discoverabilitytitle).
> iPad 바로 가기 인터페이스는 각 범주의 모든 항목을 표시하므로 하위 메뉴 제목을 사용하여 하위 항목의 컨텍스트를 제공할 수 없습니다. 예를 들어, 항목 제목 이름 및 추가된 날짜는 하위 메뉴 제목 정렬 기준의 컨텍스트 없이는 의미가 없습니다. 이름별 책갈피 정렬 및 추가된 날짜별 책갈피 정렬과 같은 필요한 컨텍스트를 포함하여 각 항목의 제목을 향상시킬 수 있습니다. 개발자 지침은 검색 가능성을 참조하십시오.제목.
>




### **Keyboard navigation on iPad**

By default, iPadOS 15 and later enables keyboard navigation in text fields, text views, and sidebars, providing APIs you can use to enable it in various types of collection views and other custom views in your app. For developer guidance, see [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based_navigation).
> 기본적으로 iPadOS 15 이상은 텍스트 필드, 텍스트 보기 및 사이드바에서 키보드 탐색을 활성화하여 앱의 다양한 유형의 컬렉션 보기 및 기타 사용자 지정 보기에서 활성화하는 데 사용할 수 있는 API를 제공합니다. 개발자 지침은 포커스 기반 탐색을 참조하십시오.
>




**IMPORTANT**Avoid enabling keyboard navigation for controls, such as buttons, segmented controls, and switches. Full keyboard-access mode already helps people activate controls, navigate to all onscreen components, and even perform gesture-based interactions like drag and drop.
> 중요 단추, 세그먼트화된 컨트롤 및 스위치와 같은 컨트롤에 대해 키보드 탐색을 활성화하지 마십시오. 전체 키보드 액세스 모드는 이미 사용자가 컨트롤을 활성화하고 모든 화면 구성 요소로 이동하며 드래그 앤 드롭과 같은 제스처 기반 상호 작용을 수행하는 데 도움이 됩니다.
>




The iPadOS and tvOS focus systems are similar. People perform actions by moving a focus indicator to an item and then selecting it (for guidance, see [Focus and selection](../inputs/focus-and-selection)). Although the underlying system is the same, the user experiences are a little different. tvOS uses *directional focus*, which means that people can use the same interaction — that is, swiping the Siri Remote or using only the arrow keys on a connected keyboard — to navigate to every onscreen component. In contrast, iPadOS defines *focus groups*, which represent specific areas within an app, like a sidebar, grid, or list. Using focus groups, iPadOS can support two different keyboard interactions.
> 아이패드OS와 TVOS 포커스 시스템은 비슷하다. 사용자는 포커스 표시기를 항목으로 이동한 다음 선택하여 작업을 수행합니다(자세한 내용은 포커스 및 선택 참조). 기본 시스템은 동일하지만 사용자 경험은 약간 다릅니다. 즉, 사람들은 동일한 상호 작용, 즉 연결된 키보드의 화살표 키만 사용하여 모든 화면 구성 요소로 이동할 수 있습니다. 대조적으로, iPadOS는 사이드바, 그리드 또는 목록과 같은 앱 내의 특정 영역을 나타내는 포커스 그룹을 정의합니다. 포커스 그룹을 사용하여 iPadOS는 두 가지 다른 키보드 상호 작용을 지원할 수 있습니다.
>




- Pressing the Tab key moves focus among focus groups, letting people navigate to sidebars, grids, and other app areas.
- >  Tab 키를 누르면 포커스 그룹 간에 포커스가 이동하여 사이드바, 그리드 및 기타 앱 영역으로 이동할 수 있습니다.

- Pressing an arrow key enables a directional focus interaction that’s similar to tvOS, but limited to navigation among items in the same focus group. For example, people can use an arrow key to move through the items in a list or a sidebar.
- >  화살표 키를 누르면 TVOS와 유사하지만 동일한 포커스 그룹의 항목 간 탐색으로 제한되는 방향 포커스 상호 작용이 가능합니다. 예를 들어, 사용자는 화살표 키를 사용하여 목록이나 사이드바의 항목을 이동할 수 있습니다.


Onscreen components can indicate focus by using the halo effect or the highlighted appearance.
> 화면 구성 요소는 후광 효과 또는 강조 표시된 모양을 사용하여 초점을 나타낼 수 있습니다.
>




The *halo* focus effect — also known as the *focus ring* — displays a customizable outline around the component. You can apply the halo effect to custom views and to fully opaque content within a collection or list cell, such as an image.
> 초점 링이라고도 하는 후광 초점 효과는 구성 요소 주위에 사용자 정의 가능한 윤곽선을 표시합니다. 이미지와 같은 컬렉션 또는 목록 셀 내의 완전히 불투명한 내용과 사용자 정의 보기에 후광 효과를 적용할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/halo-focus-effect_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/halo-focus-effect_2x.png)

Photos uses the halo effect to indicate the focused photo in a collection.
> 사진은 컬렉션에서 초점을 맞춘 사진을 나타내기 위해 후광 효과를 사용합니다.
>




**Customize the halo focus effect when necessary.** By default, the system uses an item’s shape to infer the shape of its halo. If the system-provided halo doesn’t give you the appearance you want, you can refine it to match contours like rounded corners or shapes defined by Bézier paths. You can also adjust a halo’s position if another component occludes or clips it. For example, you might need to ensure that a badge appears above the halo or that a parent view doesn’t clip it. For developer guidance, see [UIFocusHaloEffect](https://developer.apple.com/documentation/uikit/uifocushaloeffect).
> 필요한 경우 후광 초점 효과를 사용자 지정합니다. 기본적으로 시스템은 항목의 모양을 사용하여 후광의 모양을 유추합니다. 시스템에서 제공한 후광이 원하는 모양을 제공하지 않는 경우 둥근 모서리나 Bézier 경로에서 정의한 모양과 같은 윤곽선에 맞게 다듬을 수 있습니다. 다른 구성 요소가 후광을 막거나 잘라내는 경우 후광의 위치를 조정할 수도 있습니다. 예를 들어 배지가 후광 위에 나타나는지 또는 상위 보기가 배지를 클리핑하지 않는지 확인해야 할 수 있습니다. 개발자 지침은 UIFocus HaloEffect를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/customized-halo_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/customized-halo_2x.png)

Photos uses a rounded-corner halo to match the corners of the focused album’s thumbnail.
> 사진은 초점이 맞춰진 앨범 썸네일의 모서리와 일치하도록 둥근 모서리의 후광을 사용한다.
>




The *highlighted* appearance — in which the component’s background uses the app’s accent color — also indicates focus, but it’s not a focus effect. The highlight appearance occurs automatically when people select a collection view cell on which you’ve set background and content configurations (for developer guidance, see [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)).
> 구성 요소의 배경에서 앱의 액센트 색상을 사용하는 강조 표시된 모양도 포커스를 나타내지만 포커스 효과는 아닙니다. 사용자가 배경 및 내용 구성을 설정한 컬렉션 보기 셀을 선택하면 사용자가 강조 표시됩니다(개발자 지침은 UICollection ViewCell 참조).
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/highlighted-appearance_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/keyboards/images/highlighted-appearance_2x.png)

Photos uses the highlighted appearance to indicate the selected item in the sidebar.
> 사진은 사이드바에서 선택한 항목을 나타내기 위해 강조 표시된 모양을 사용합니다.
>




**Ensure that focus moves through your custom views in ways that make sense.** As people continue pressing the Tab key, focus moves through focus groups in reading order: leading to trailing, and top to bottom. Although focus moves through system-provided views in ways that people expect, you might need to adjust the order in which the focus system visits your custom views. For example, if you want focus to move down through a vertical stack of custom views before it moves in the trailing direction to the next view, you need to identify the stack container as a single focus group. For developer guidance, see [focusGroupIdentifier](https://developer.apple.com/documentation/uikit/uifocusenvironment/3601224-focusgroupidentifier).
> 포커스가 사용자 정의 보기를 통해 적절한 방식으로 이동하는지 확인하십시오. 사람들이 Tab 키를 계속 누르면 포커스 그룹에서 읽기 순서로 이동합니다. 포커스는 사람들이 예상하는 방식으로 시스템에서 제공한 보기를 통해 이동하지만 포커스 시스템이 사용자 정의 보기를 방문하는 순서를 조정해야 할 수도 있습니다. 예를 들어, 포커스가 다음 뷰의 후행 방향으로 이동하기 전에 사용자 정의 뷰의 수직 스택을 통해 아래로 이동하려면 스택 컨테이너를 단일 포커스 그룹으로 식별해야 합니다. 개발자 지침은 focusGroupIdentifier를 참조하십시오.
>




**Adjust the priority of an item to reflect its importance within a focus group.** When a group receives focus, its *primary item* automatically receives focus too, making it easy for people to select the item they’re most likely to want. You can make an item primary by increasing its priority. For developer guidance, see [UIFocusGroupPriority](https://developer.apple.com/documentation/uikit/uifocusgrouppriority/).
> 포커스 그룹 내에서 중요도를 반영하도록 항목의 우선 순위를 조정합니다. 그룹이 포커스를 받으면 기본 항목도 자동으로 포커스를 받아 사람들이 원하는 항목을 쉽게 선택할 수 있습니다. 우선 순위를 높여 항목을 주 항목으로 만들 수 있습니다. 개발자 지침은 UIFocusGroupPriority를 참조하십시오.
>




# **Specifications**

# **Reserved keyboard shortcuts**

The following keyboard shortcuts are either reserved by the system or well-known to people.
> 다음 키보드 단축키는 시스템에 의해 예약되었거나 사람들에게 잘 알려져 있습니다.
>




| Primary Key | Keyboard Shortcut | Used by the System | Action |
| --- | --- | --- | --- |
| Space | Command-Space | ● | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | ● | Varies. Apple reserved. |
|  | Option-Command-Space | ● | Show the Spotlight search results window. |
|  | Control-Command-Space | ● | Show the Special Characters window. |
| Tab | Shift-Tab | ● | Navigate through controls in a reverse direction. |
|  | Command-Tab | ● | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | ● | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | ● | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | ● | Move focus to the previous group of controls. |
| Esc | Option-Command-Esc | ● | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | ● | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | ● | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | ● | Toggle full keyboard access on or off. |
| F2 | Control-F2 | ● | Move focus to the menu bar. |
| F3 | Control- F3 | ● | Move focus to the Dock. |
| F4 | Control-F4 | ● | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | ● | Move focus to the previously active window. |
| F5 | Control-F5 | ● | Move focus to the toolbar. |
|  | Command-F5 | ● | Turn VoiceOver on or off. |
| F6 | Control-F6 | ● | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | ● | Move focus to the previous panel. |
| F7 | Control-F7 | ● | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | ● | Varies. Apple reserved. |
| F9 |  | ● | Varies. Apple reserved. |
| F10 |  | ● | Varies. Apple reserved. |
| F11 |  | ● | Show desktop. |
| F12 |  | ● | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | ● | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | ● | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | ● | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | ● | Decrease the size of the selection. |
|  | Option-Command-Hyphen | ● | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket |  | Left-align a selection. |
| Right bracket (}) | Command-Right bracket |  | Right-align a selection. |
| Pipe (|) | Command-Pipe |  | Center-align a selection. |
| Colon (:) | Command-Colon |  | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon |  | Find misspelled words in the document. |
| Comma (,) | Command-Comma |  | Open the app’s settings window. |
|  | Control-Option-Command-Comma | ● | Decrease screen contrast. |
| Period (.) | Control-Option-Command-Period | ● | Increase screen contrast. |
| Question mark (?) | Command-Question mark |  | Open the app’s Help menu. |
| Forward slash (/) | Option-Command-Forward slash | ● | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | ● | Increase the size of the selection. |
|  | Option-Command-Equal sign | ● | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | ● | Capture the screen to a file. |
|  | Control-Shift-Command-3 | ● | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | ● | Capture a selection to a file. |
|  | Control-Shift-Command-4 | ● | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | ● | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | ● | Invert the screen colors. |
| A | Command-A |  | Selects every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A |  | Deselects all selections or characters. |
| B | Command-B |  | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C |  | Copy the selection to the Clipboard. |
|  | Shift-Command-C |  | Display the Colors window. |
|  | Option-Command-C |  | Copy the style of the selected text. |
|  | Control-Command-C |  | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | ● | Show or hide the Dock. |
|  | Control-Command-D |  | Display the definition of the selected word in the Dictionary app. |
| E | Command-E |  | Use the selection for a find operation. |
| F | Command-F |  | Open a Find window. |
|  | Option-Command-F |  | Jump to the search field control. |
|  | Control-Command-F |  | Enter full screen. |
| G | Command-G |  | Find the next occurrence of the selection. |
|  | Shift-Command-G |  | Find the previous occurrence of the selection. |
| H | Command-H |  | Hide the windows of the currently running app. |
|  | Option-Command-H |  | Hide the windows of all other running apps. |
| I | Command-I |  | Italicize the selected text or toggle italic text on or off. |
|  | Command-I |  | Display an Info window. |
|  | Option-Command-I |  | Display an inspector window. |
| J | Command-J |  | Scroll to a selection. |
| M | Command-M |  | Minimize the active window to the Dock. |
|  | Option-Command-M |  | Minimize all windows of the active app to the Dock. |
| N | Command-N |  | Open a new document. |
| O | Command-O |  | Display a dialog for choosing a document to open. |
| P | Command-P |  | Display the Print dialog. |
|  | Shift-Command-P |  | Display the Page Setup dialog. |
| Q | Command-Q |  | Quit the app. |
|  | Shift-Command-Q | ● | Log out the current user. |
|  | Option-Shift-Command-Q | ● | Log out the current user without confirmation. |
| S | Command-S |  | Save a new document or save a version of a document. |
|  | Shift-Command-S |  | Duplicate the active document or initiate a Save As. |
| T | Command-T |  | Display the Fonts window. |
|  | Option-Command-T |  | Show or hide a toolbar. |
| U | Command-U |  | Underline the selected text or turn underlining on or off. |
| V | Command-V |  | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V |  | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V |  | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V |  | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V |  | Apply formatting settings to the selection. |
| W | Command-W |  | Close the active window. |
|  | Shift-Command-W |  | Close a file and its associated windows. |
|  | Option-Command-W |  | Close all windows in the app. |
| X | Command-X |  | Remove the selection and store on the Clipboard. |
| Z | Command-Z |  | Undo the previous operation. |
|  | Shift-Command-Z |  | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | ● | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | ● | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | ● | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | ● | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | ● | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | ● | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | ● | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | ● | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | ● | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | ● | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | ● | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | ● | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | ● | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | ● | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | ● | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | ● | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | ● | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | ● | Move focus to another value or cell within a view, such as a table. |

# **Reserved international keyboard shortcuts**

The system reserves several key combinations for use with localized versions of the system, localized keyboard, keyboard layouts, and input methods. These shortcuts don’t correspond directly to menu commands.
> 시스템은 현지화된 버전의 시스템, 현지화된 키보드, 키보드 레이아웃 및 입력 방법과 함께 사용하기 위해 몇 가지 키 조합을 예약합니다. 이러한 바로 가기는 메뉴 명령과 직접 일치하지 않습니다.
>




| Keyboard shortcut | Action |
| --- | --- |
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. Apple reserved. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |
