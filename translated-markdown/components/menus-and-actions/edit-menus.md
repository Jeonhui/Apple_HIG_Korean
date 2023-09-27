# **[components-menus-and-actions] edit-menus**

## An edit menu lets people make changes to selected content in the current view, in addition to offering related commands like Copy, Select, Translate, and Look Up.
> 편집 메뉴를 사용하면 복사, 선택, 변환 및 조회와 같은 관련 명령을 제공할 뿐만 아니라 현재 보기에서 선택한 내용을 변경할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/edit-menu-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/edit-menu-intro-dark_2x.png)

In addition to text, an edit menu’s commands can apply to many types of selectable content, such as images, files, and objects like contact cards, charts, or map locations. Beginning in iOS 16 and iPadOS 16, the system automatically detects the data type of a selected item, enabling the addition of a related action to the edit menu. For example, selecting an address can enable an edit-menu item like Get directions.
> 편집 메뉴의 명령은 텍스트 외에도 이미지, 파일 및 연락처 카드, 차트 또는 지도 위치와 같은 개체와 같은 다양한 유형의 선택 가능한 콘텐츠에 적용할 수 있습니다. iOS 16과 iPad OS 16부터는 시스템이 선택한 항목의 데이터 유형을 자동으로 감지하여 편집 메뉴에 관련 작업을 추가할 수 있습니다. 예를 들어 주소를 선택하면 길찾기와 같은 편집 메뉴 항목을 사용할 수 있습니다.
>




Edit menus can look and behave slightly differently in different platforms.
> 편집 메뉴는 플랫폼마다 조금씩 다르게 보일 수 있습니다.
>




- In iOS, the edit menu displays commands in a compact, horizontal list that appears when people touch and hold or double-tap to select content in a view.
- >  iOS에서 편집 메뉴는 사람들이 보기의 콘텐츠를 선택하기 위해 길게 누르거나 두 번 탭할 때 나타나는 작고 수평인 목록으로 명령을 표시합니다.

- In iPadOS, the edit menu looks different depending on how people reveal it. When people use touch interactions to reveal the menu, it uses the familiar compact, horizontal appearance. In contrast, when people use a keyboard or pointing device to reveal it, the edit menu uses a vertical layout in which three or four important commands can display in a row at the top.
- >  아이패드OS에서 편집 메뉴는 사람들이 그것을 어떻게 공개하느냐에 따라 다르게 보인다. 사람들이 메뉴를 드러내기 위해 터치 인터랙션을 사용할 때, 그것은 익숙한 컴팩트하고 수평적인 외관을 사용한다. 대조적으로, 사람들이 그것을 드러내기 위해 키보드나 포인팅 장치를 사용할 때, 편집 메뉴는 세 개 또는 네 개의 중요한 명령이 맨 위에 일렬로 표시될 수 있는 수직 레이아웃을 사용한다.

- In macOS, people can access editing commands in a context menu they can reveal while in an editing task, as well as through the app’s [Edit menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/#edit-menu)in the menu bar.
- >  macOS에서 사람들은 메뉴바에 있는 앱의 편집 메뉴뿐만 아니라 편집 작업을 하는 동안 표시할 수 있는 상황에 맞는 메뉴에서 편집 명령에 액세스할 수 있다.


Editing content is rare in tvOS and watchOS experiences, so the system doesn’t provide an edit menu in these platforms.
> tvOS와 시청에서는 콘텐츠 편집이 드물다.OS 경험이 있기 때문에 시스템은 이러한 플랫폼에서 편집 메뉴를 제공하지 않습니다.
>




# **Best practices**

**Prefer the system-provided edit menu.** People are familiar with the contents and behavior of the system-provided component, so creating a custom menu that presents the same commands is redundant and likely to be confusing. For a list of standard edit menu commands, see [UIResponderStandardEditActions](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions?language=objc).
> 시스템 제공 편집 메뉴를 선호합니다. 사람들은 시스템 제공 구성 요소의 내용과 동작에 익숙하기 때문에 동일한 명령을 제시하는 사용자 지정 메뉴를 만드는 것은 중복되고 혼란스러울 수 있습니다. 표준 편집 메뉴 명령 목록은 UI 응답기 표준 편집 작업을 참조하십시오.
>




**Let people reveal an edit menu using the system-defined interactions they already know.** For example, people expect to touch and hold on a touchscreen or use a secondary click with an attached trackpad or keyboard. Although the interactions to reveal an edit menu can differ based on platform, people don’t appreciate having to learn a custom interaction to perform a standard task.
> 이미 알고 있는 시스템 정의 상호 작용을 사용하여 편집 메뉴를 표시하도록 합니다. 예를 들어, 터치스크린을 길게 터치하거나 연결된 트랙패드 또는 키보드로 보조 클릭을 사용할 것으로 예상합니다. 편집 메뉴를 드러내기 위한 상호 작용은 플랫폼에 따라 다를 수 있지만, 사람들은 표준 작업을 수행하기 위해 사용자 지정 상호 작용을 배워야 하는 것을 좋아하지 않는다.
>




**Enable commands that are relevant in the current context, removing or dimming commands that don’t apply.** For example, if nothing is selected, avoid showing options that require a selection, such as Copy or Cut. Similarly, avoid showing a Paste option when there’s nothing to paste.
> 현재 컨텍스트와 관련된 명령을 활성화하여 적용되지 않는 명령을 제거하거나 흐리게 합니다. 예를 들어 아무것도 선택하지 않은 경우 복사 또는 잘라내기 같은 선택 항목이 필요한 옵션을 표시하지 않도록 합니다. 마찬가지로 붙여넣을 것이 없을 때는 붙여넣기 옵션을 표시하지 않도록 합니다.
>




**List custom commands near relevant system-provided ones.** For example, if you offer custom formatting commands, you can help maintain the ordering people expect by listing them after the system-provided commands in the format section. Be sure to avoid overwhelming people with too many custom commands.
> 관련 시스템에서 제공한 명령 근처에 사용자 지정 명령을 나열합니다. 예를 들어, 사용자 지정 형식 명령을 제공하는 경우 형식 섹션의 시스템에서 제공한 명령 뒤에 나열하여 사용자가 기대하는 순서를 유지 관리하는 데 도움이 될 수 있습니다. 너무 많은 사용자 지정 명령으로 사람을 압도하지 않도록 하십시오.
>




**When it makes sense, let people select and copy noneditable text.**People appreciate being able to paste static content — such as an image caption or social media status — into a message, note, or web search. In general, let people copy content text, but not control labels.
> 그것이 말이 되면, 사람들이 편집 불가능한 텍스트를 선택하고 복사하도록 하세요.사람들은 이미지 캡션 또는 소셜 미디어 상태와 같은 정적 콘텐츠를 메시지, 노트 또는 웹 검색에 붙여넣을 수 있다는 점을 높이 평가합니다. 일반적으로 사용자가 내용 텍스트를 복사하도록 허용하지만 제어 레이블은 복사하지 않습니다.
>




**Support undo and redo when possible.** Like all menus, an edit menu doesn’t require confirmation before performing its actions, so people can easily use undo and redo to recover a previous state. For guidance, see [Undo and redo](../patterns/undo-and-redo).
> 실행 취소 및 재실행 지원. 모든 메뉴와 마찬가지로 편집 메뉴도 작업을 수행하기 전에 확인하지 않아도 되므로 실행 취소 및 재실행을 통해 이전 상태를 쉽게 복구할 수 있습니다. 자세한 내용은 실행 취소 및 다시 실행을 참조하십시오.
>




**In general, avoid implementing other controls that perform the same functions as edit menu items.** People typically expect to choose familiar edit commands in an edit menu, or use standard keyboard shortcuts. Offering redundant controls can crowd your interface, giving you less space for presenting actions that people might not already know about.
> 일반적으로 편집 메뉴 항목과 동일한 기능을 수행하는 다른 컨트롤은 구현하지 마십시오. 사람들은 일반적으로 편집 메뉴에서 익숙한 편집 명령을 선택하거나 표준 키보드 단축키를 사용합니다. 중복 컨트롤을 제공하면 인터페이스가 혼잡해져 사용자가 아직 알지 못하는 작업을 표시할 수 있는 공간이 줄어들 수 있습니다.
>




**Differentiate different types of deletion commands when necessary.**For example, a Delete menu item behaves the same as pressing a Delete key, but a Cut menu item copies the selected content to the system pasteboard before deleting it.
> 필요한 경우 다른 유형의 삭제 명령을 구분합니다.예를 들어 Delete 메뉴 항목은 Delete 키를 누르는 것과 동일하게 동작하지만 Cut 메뉴 항목은 선택한 내용을 삭제하기 전에 시스템 페이스트보드에 복사합니다.
>




# **Content**

**Create short labels for custom commands.** Use verbs or short verb phrases that succinctly describe the action your command performs. For guidance, see [Labels](../components/layout-and-organization/labels).
> 사용자 지정 명령에 대한 짧은 레이블을 만듭니다. 명령이 수행하는 작업을 간략하게 설명하는 동사 또는 짧은 동사 구문을 사용하십시오. 자세한 내용은 레이블을 참조하십시오.
>




# **Platform considerations**

*Not supported in tvOS or watchOS.*
> tvOS 또는 시계에서 지원되지 않음OS.
>




# **iOS, iPadOS**

**Ensure your edit menu works well in both styles.** The system displays the compact, horizontal style when people use Multi-Touch gestures to reveal the edit menu, and the vertical style when people use a keyboard or pointing device to reveal it. For guidance using the vertical menu layout, see [Menus > iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/menus#ios-ipados).
> 편집 메뉴가 두 가지 스타일에서 모두 잘 작동하는지 확인합니다. 시스템은 멀티터치 제스처를 사용하여 편집 메뉴를 표시할 때 가로로 표시되는 콤팩트한 스타일과 키보드 또는 포인팅 장치를 사용하여 편집 메뉴를 표시할 때 세로 방향으로 표시됩니다. 수직 메뉴 레이아웃을 사용한 지침은 메뉴 > iOS, iPadOS를 참조하십시오.
>




**Adjust an edit menu’s placement, if necessary.** Depending on available space, the default menu position is above or below the insertion point or selection. The system also displays a visual indicator that points to the targeted content. Although you can’t change the shape of the menu or its pointer, you can change the menu’s position. For example, you might need to move the menu to prevent it from covering important content or parts of your interface.
> 필요한 경우 편집 메뉴의 위치를 조정합니다. 사용 가능한 공간에 따라 기본 메뉴 위치는 삽입 지점 또는 선택 영역의 위 또는 아래에 있습니다. 또한 시스템은 대상 콘텐츠를 가리키는 시각적 표시기를 표시합니다. 메뉴 모양이나 포인터는 변경할 수 없지만 메뉴 위치는 변경할 수 있습니다. 예를 들어, 메뉴를 이동하여 인터페이스의 중요한 내용이나 부분을 포함하지 않도록 해야 할 수 있습니다.
>




# **macOS**

To learn about the order of items in a macOS app’s Edit menu, see [Edit menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar/#edit-menu).
> MacOS 앱의 편집 메뉴에서 항목 순서에 대해 알아보려면 편집 메뉴를 참조하십시오.
>



